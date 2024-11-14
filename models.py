from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_bcrypt import Bcrypt
from datetime import datetime

# Initialize db and bcrypt here (do not reinitialize them in app.py)
db = SQLAlchemy()
bcrypt = Bcrypt()

# User model
class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    
    claims = db.relationship('Claim', backref='user', lazy=True)
    items = db.relationship('Item', backref='user', lazy=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def authenticate(self, password):
        return check_password_hash(self.password_hash, password)

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "is_admin": self.is_admin
        }

# Other models follow in similar structure...


# Item model
class Item(db.Model):
    __tablename__ = 'items'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    status = db.Column(db.String(50), default='lost')  # lost, claimed, etc.
    reward = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    claims = db.relationship('Claim', backref='item', lazy=True)
    comments = db.relationship('Comment', backref='item', lazy=True)
    images = db.relationship('ItemImage', backref='item', lazy=True)

    def __init__(self, title, description, user_id, status='lost', reward=None):
        self.title = title
        self.description = description
        self.user_id = user_id
        self.status = status
        self.reward = reward
    
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "status": self.status,
            "reward": self.reward,
            "user_id": self.user_id
        }

# Claim model
class Claim(db.Model):
    __tablename__ = 'claims'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'), nullable=False)
    is_approved = db.Column(db.Boolean, default=False)
    
    def __init__(self, user_id, item_id):
        self.user_id = user_id
        self.item_id = item_id
    
    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "item_id": self.item_id,
            "is_approved": self.is_approved
        }

# Reward model (optional)
class Reward(db.Model):
    __tablename__ = 'rewards'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    points = db.Column(db.Integer, nullable=False)

    def __init__(self, title, description, points):
        self.title = title
        self.description = description
        self.points = points

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "points": self.points
        }

# Comment model
class Comment(db.Model):
    __tablename__ = 'comments'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'), nullable=False)
    content = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __init__(self, user_id, item_id, content):
        self.user_id = user_id
        self.item_id = item_id
        self.content = content
    
    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "item_id": self.item_id,
            "content": self.content,
            "created_at": self.created_at
        }

# ItemImage model
class ItemImage(db.Model):
    __tablename__ = 'item_images'
    
    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'), nullable=False)
    url = db.Column(db.String(255), nullable=False)
    
    def __init__(self, item_id, url):
        self.item_id = item_id
        self.url = url
    
    def to_dict(self):
        return {
            "id": self.id,
            "item_id": self.item_id,
            "url": self.url
        }
