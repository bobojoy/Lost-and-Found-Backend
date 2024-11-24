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
# app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')

# Import models
from models import db, bcrypt, User, Admin, LostItem, FoundItem, Claim, Comment

db.init_app(app)
bcrypt.init_app(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)
api = Api(app)

# Enable CORS
CORS(app)

class Home(Resource):
    def __init__(self):
        self.name = "Home"
        self.description = "Welcome to the Lost and Found System"
        
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
            user.password = data['password']
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

        # Retrieve the user by email
        user = User.query.filter_by(email=data["email"]).first()

        if user and user.authenticate(data["password"]):
            # Generate the JWT token
            access_token = create_access_token(identity=user.id)
            return make_response({"message": f"{user.username} logged in", "access_token": access_token}, 200)
        
        return {"error": "Invalid credentials"}, 401
# LostItem Resource
class LostItemResource(Resource):
    def get(self, item_id=None):
        if item_id:
            item = LostItem.query.get(item_id)
            if not item:
                return {"error": "Lost item not found"}, 404
            return item.to_dict(), 200
        items = LostItem.query.all()
        return [item.to_dict() for item in items], 200

    # @jwt_required()
    def post(self):
        data = request.get_json()
        user_id = data.get('user_id')
        
        if not user_id:
            
            return {"error": "User ID is required"},
        # user_id = get_jwt_identity()
        lost_item = LostItem(
            name=data['name'],
            description=data['description'],
            place_lost=data['place_lost'],
            reward=data.get('reward'),
            image_url=data['image_url'],
            user_id=user_id
        )
        db.session.add(lost_item)
        db.session.commit()
        return lost_item.to_dict(), 201

    # @jwt_required()
    def delete(self, item_id):
        lost_item = LostItem.query.get(item_id)
        if not lost_item:
            return {"error": "Lost item not found"}, 404
        db.session.delete(lost_item)
        db.session.commit()
        return {"message": "Lost item deleted"}, 200

# FoundItem Resource
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
        user_id = get_jwt_identity()
        found_item = FoundItem(
            name=data['name'],
            description=data['description'],
            place_found=data['place_found'],
            reward=data.get('reward'),
            user_id=user_id
        )
        db.session.add(found_item)
        db.session.commit()
        return found_item.to_dict(), 201

# Claim Resource
class ClaimItemResource(Resource):
    @jwt_required()
    def post(self, item_type, item_id):
        user_id = get_jwt_identity()
        item = None
        if item_type == 'lost':
            item = LostItem.query.get(item_id)
        elif item_type == 'found':
            item = FoundItem.query.get(item_id)

        if not item:
            return {"error": f"{item_type.capitalize()} item not found"}, 404

        claim = Claim(user_id=user_id, founditem_id=item_id if item_type == 'found' else None, lostitem_id=item_id if item_type == 'lost' else None)
        db.session.add(claim)
        item.status = 'claimed'
        db.session.commit()
        return claim.to_dict(), 201

# Comment Resource
class CommentResource(Resource):
     
    
    
    
     def post(self, item_type, item_id):
        data = request.get_json()
        user_id = get_jwt_identity()
        comment = Comment(
            user_id=user_id,
            lost_item_id=item_id if item_type == 'lost' else None,
            found_item_id=item_id if item_type == 'found' else None,
            content=data['content']
        )
        db.session.add(comment)
        db.session.commit()
        return comment.to_dict(), 201

# Admin Approve Claim
class AdminApproveClaim(Resource):
    @jwt_required()
    def post(self, claim_id):
        user_id = get_jwt_identity()
        admin = Admin.query.get(user_id)
        if not admin:
            return {"error": "Admin privileges required"}, 403

        claim = Claim.query.get(claim_id)
        if not claim:
            return {"error": "Claim not found"}, 404

        claim.is_approved = True
        db.session.commit()
        return claim.to_dict(), 200
    
class UserResource(Resource):
    def get(self, user_id=None):
        if user_id:
            user = User.query.get(user_id)
            if not user:
                return {"error": "Lost item not found"}, 404
            return user.to_dict(), 200
        users = User.query.all()
        return [user.to_dict() for user in users], 200
    
class AdminResource(Resource):
    def get(self, admin_id=None):
        if admin_id:
            admin = Admin.query.get(admin_id)
            if not admin:
                return {"error": "Lost item not found"}, 404
            return admin.to_dict(), 200
        admins = Admin.query.all()
        return [admin.to_dict() for admin in admins], 200  
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
class Example(Resource):
 
    def get(self, item_id=None):
        if item_id:
            item = LostItem.query.get(item_id)
            if not item:
                return {"error": "Lost item not found"}, 404
            return item.to_dict(), 200
        items = LostItem.query.all()
        return [item.to_dict() for item in items], 200

    # @jwt_required()
    def post(self):
        data = request.get_json()
        user_id = data.get('user_id')
        
        if not user_id:
            
            return {"error": "User ID is required"},
        # user_id = get_jwt_identity()
        lost_item = LostItem(
            name=data['name'],
            description=data['description'],
            place_lost=data['place_lost'],
            reward=data.get('reward'),
            user_id=user_id
        )
        db.session.add(lost_item)
        db.session.commit()
        return lost_item.to_dict(), 201

    # @jwt_required()
    def delete(self, item_id):
        lost_item = LostItem.query.get(item_id)
        if not lost_item:
            return {"error": "Lost item not found"}, 404
        db.session.delete(lost_item)
        db.session.commit()
        return {"message": "Lost item deleted"}, 200

    

# Register API Resources
api.add_resource(Example, '/admins/lostitems', '/admins/lostitems/<int:item_id>')

api.add_resource(Home, '/')
api.add_resource(UserRegister, '/signup')
api.add_resource(UserResource, '/users')
api.add_resource(AdminResource, '/admins')
api.add_resource(UserLogin, '/login')
api.add_resource(LostItemResource, '/lostitems', '/lostitems/<int:item_id>')
api.add_resource(FoundItemResource, '/founditems', '/founditems/<int:item_id>')
api.add_resource(ClaimItemResource, '/claim/<string:item_type>/<int:item_id>')
api.add_resource(CommentResource, '/comments/<string:item_type>/<int:item_id>')
api.add_resource(AdminApproveClaim, '/admin/claims/<int:claim_id>/approve')
api.add_resource(AdminApproveLostItem, '/admin/lostitems/<int:item_id>/approve')


# Run the app
if __name__ == "__main__":
    app.run(debug=True)
