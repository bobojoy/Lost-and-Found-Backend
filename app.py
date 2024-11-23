from flask import Flask, request, jsonify, session, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api, Resource
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from dotenv import load_dotenv
from flask_cors import CORS
import os

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.secret_key = os.urandom(24)  
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')  # Ensure you set this in .env file

# Import models
from models import db, bcrypt, User, Admin, LostItem, FoundItem, Claim, Comment

db.init_app(app)
bcrypt.init_app(app)
migrate = Migrate(app, db)
CORS(app)

jwt = JWTManager(app)
api = Api(app)

# Home route
class Home(Resource):
    def get(self):
        return {"message": "Welcome to the Lost and Found System!"}, 200

# User Registration
class UserRegister(Resource):
    def post(self):
        data = request.get_json()
        try:
            user = User(
                username=data['username'],
                email=data['email']
            )
            user.password = data['password']  # This triggers the password setter
            db.session.add(user)
            db.session.commit()
            session["user_id"] = user.id
            return make_response(user.to_dict(), 201)
        except IntegrityError:
            return {"error": "Username or email already exists"}, 422
        except Exception as e:
            return make_response({"error": str(e)}, 422)

# User Login
class UserLogin(Resource):
    def post(self):
        data = request.get_json()
        user = User.query.filter_by(email=data["email"]).first()

        if user and user.authenticate(data["password"]):
            # Generate the JWT token for the user
            access_token = create_access_token(identity=user.id)
            session["user_id"] = user.id
            print(request.headers.get('Authorization'))
            return make_response({"message": f"{user.username} logged in", "access_token": access_token}, 200)
        
        return {"error": "Invalid credentials"}, 401

class UserLogout(Resource):
    @jwt_required()
    def post(self):
        # This will effectively "logout" by removing the JWT token from the client-side
        return {"message": "Successfully logged out"}, 200
# LostItem Resource
class LostItemResource(Resource):
    # Get all or single LostItem
    def get(self, item_id=None):
        if item_id:
            item = LostItem.query.get(item_id)
            if not item:
                return {"error": "Lost item not found"}, 404
            return item.to_dict(), 200
        items = LostItem.query.all()
        return [item.to_dict() for item in items], 200

    # Post a new LostItem (requires JWT authentication)
    @jwt_required()
    def post(self):
        data = request.get_json()
        user_id = get_jwt_identity()  # Get the user ID from the JWT token

        lost_item = LostItem(
            name=data['name'],
            description=data['description'],
            place_lost=data['place_lost'],
            reward=data.get('reward'),
            image_url=data['image_url'],
            user_id=user_id  # Associate the lost item with the signed-in user
            
        )
        db.session.add(lost_item)
        db.session.commit()
        return lost_item.to_dict(), 201


    # Delete a LostItem (requires JWT authentication)
    @jwt_required()
    def delete(self, item_id):
        lost_item = LostItem.query.get(item_id)
        if not lost_item:
            return {"error": "Lost item not found"}, 404
        db.session.delete(lost_item)
        db.session.commit()
        return {"message": "Lost item deleted"}, 200

    # @jwt_required()
    # def put(self, item_id):
    #     # Admin authentication and checking
    #     admin_id = get_jwt_identity()
    #     admin = Admin.query.get(admin_id)

    #     if not admin:
    #         return {"error": "Admin privileges required"}, 403

    #     lost_item = LostItem.query.get(item_id)
    #     if not lost_item:
    #         return {"error": "Lost item not found"}, 404

    #     if lost_item.status == "approved":
    #         return {"error": "Lost item already approved"}, 400

    #     # Change the status to approved
    #     lost_item.status = "approved"
    #     lost_item.approved_by_id = admin.id
    #     lost_item.image_url = request.get_json().get('image_url', lost_item.image_url)
    #     db.session.commit()
        
    #     return lost_item.to_dict(), 200
# FoundItem Resource (example)
class FoundItemResource(Resource):
    
    def get(self, item_id=None):
        if item_id:
            item = FoundItem.query.get(item_id)
            if not item:
                return {"error": "Found item not found"}, 404
            return item.to_dict(), 200
        items = FoundItem.query.all()
        return [item.to_dict() for item in items], 200

    @jwt_required()
    def post(self):
        data = request.get_json()
        user_id = get_jwt_identity()  # Get the user ID from the JWT token
        found_item = FoundItem(
            name=data['name'],
            description=data["description"],
            place_lost=data["place_lost"],
            reward=data.get('reward'),
            user_id=user_id
        )
        db.session.add(found_item)
        db.session.commit()
        return found_item.to_dict(), 201

class AdminLogin(Resource):
    def post(self):
        data = request.get_json()
        admin = Admin.query.filter_by(email=data["email"]).first()

        if admin and admin.authenticate(data["password"]):
            # Generate the JWT token for the user
            access_token = create_access_token(identity=admin.id)
            session["admin_id"] = admin.id
            print(request.headers.get('Authorization'))
            return make_response({"message": f"{admin.username} logged in", "access_token": access_token}, 200)
        
        return {"error": "Invalid credentials"}, 401
class AdminApproveLostItem(Resource):
    @jwt_required()
    def post(self, item_id):
        admin_id = get_jwt_identity()
        admin = Admin.query.get(admin_id)

        if not admin:
            return {"error": "Admin privileges required"}, 403

        lost_item = LostItem.query.get(item_id)
        if not lost_item:
            return {"error": "Lost item not found"}, 404

        if lost_item.status != "pending":
            return {"error": "Lost item already processed"}, 400

        lost_item.status = "approved"
        lost_item.approved_by_id = admin.id
        db.session.commit()
        return lost_item.to_dict(), 200

# API Routes
api.add_resource(Home, '/')
api.add_resource(UserRegister, '/signup')
api.add_resource(UserLogin, '/login')
api.add_resource(AdminLogin, '/admin/login')
api.add_resource(UserLogout, '/logout')
api.add_resource(LostItemResource, '/lostitems', '/lostitems/<int:item_id>')
api.add_resource(FoundItemResource, '/founditems', '/founditems/<int:item_id>')
api.add_resource(AdminApproveLostItem, '/admin/lostitems/<int:item_id>/approve')

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
