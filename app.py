from flask import Flask, request, jsonify, session, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api, Resource
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from dotenv import load_dotenv
from flask_cors import CORS
import os

# Load environment variables from .env
load_dotenv()

# App setup
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI',)
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')

# Import db and bcrypt from models.py (not initialized again here)
from models import db, bcrypt, User,Item,Claim

# Initialize the database and bcrypt
db.init_app(app)
bcrypt.init_app(app)

# Initialize migrations
migrate = Migrate(app, db)

# Initialize JWT
jwt = JWTManager(app)

# Enable CORS for the frontend
# CORS(app, resources={r"/*": {"origins": "https://yourfrontendapp.com"}})  # Change to your frontend URL

# Initialize API
api = Api(app)


# Import models


# User Registration Resource
class UserRegister(Resource):
    def post(self):
        data = request.get_json() 
        if "username" not in data or "password" not in data:
            return {"error": "Missing inputs required"}, 422
        try:
            user = User(
                username=data['username'],
                email=data['email']
            )
            user.password_hash = data['password']
            db.session.add(user)
            db.session.commit()
            session["user_id"] = user.id
            return make_response(user.to_dict(), 201)
        except IntegrityError:
            return {"error": "Username already exists"}, 422
        except Exception as e:
            print(e)
            return make_response({"error": str(e)}, 422)

# User Login Resource
class UserLogin(Resource):
    def post(self):
        data = request.get_json() 
        if "email" not in data or "password" not in data:
            return {"error": "Missing required fields"}, 422
        
        user = User.query.filter_by(email=data["email"]).first()
        if user and user.authenticate(data["password"]):
            session["user_id"] = user.id
            return make_response({'user':f"{user.username} has logged in"}, 201)
        else:
            return make_response({"error": "Username or password incorrect"}, 401)

class ItemResource(Resource):
    # @jwt_required()  # Ensure the user is authenticated
    def get(self, item_id=None):
        if item_id:
            item = Item.query.get(item_id)
            if not item:
                return {"error": "Item not found"}, 404
            return item.to_dict(), 200
        items = Item.query.all()
        return [item.to_dict() for item in items], 200

    # @jwt_required()
    def post(self):
        data = request.get_json()
        user_id = get_jwt_identity()  # Get the user from the JWT token

        new_item = Item(
            title=data['title'],
            description=data['description'],
            user_id=user_id,
            status='lost',  # Assuming the status is 'lost' by default
            reward=data.get('reward')
        )

        db.session.add(new_item)
        db.session.commit()
        return new_item.to_dict(), 201

    # @jwt_required()
    def put(self, item_id):
        item = Item.query.get(item_id)
        if not item:
            return {"error": "Item not found"}, 404

        data = request.get_json()
        item.title = data.get('title', item.title)
        item.description = data.get('description', item.description)
        item.reward = data.get('reward', item.reward)

        db.session.commit()
        return item.to_dict(), 200

    # @jwt_required()
    def delete(self, item_id):
        item = Item.query.get(item_id)
        if not item:
            return {"error": "Item not found"}, 404

        db.session.delete(item)
        db.session.commit()
        return {"message": "Item deleted successfully"}, 200

class ClaimItemResource(Resource):
    # @jwt_required()
    def post(self, item_id):
        data = request.get_json()
        user_id = get_jwt_identity()

        item = Item.query.get(item_id)
        if not item:
            return {"error": "Item not found"}, 404

        claim = Claim(user_id=user_id, item_id=item.id)
        db.session.add(claim)
        db.session.commit()

        item.status = 'claimed'  # Update item status to 'claimed'
        db.session.commit()

        return claim.to_dict(), 201

# --- Admin Resources ---

class AdminApproveClaim(Resource):
    # @jwt_required()
    def post(self, claim_id):
        user_id = get_jwt_identity()
        user = User.query.get(user_id)
        if not user.is_admin():
            return {"error": "Admin privileges required"}, 403
        
        claim = Claim.query.get(claim_id)
        if not claim:
            return {"error": "Claim not found"}, 404
        
        claim.is_approved = True
        db.session.commit()
        return claim.to_dict(), 200

# --- Register resources with the API ---

api.add_resource(UserRegister, '/signup')
api.add_resource(UserLogin, '/login')
api.add_resource(ItemResource, '/items', '/items/<int:item_id>')
api.add_resource(ClaimItemResource, '/items/<int:item_id>/claim')
api.add_resource(AdminApproveClaim, '/admin/claims/<int:claim_id>/approve')

# --- Running the Flask app ---
if __name__ == "__main__":
    app.run(debug=True)