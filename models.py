from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.hybrid import hybrid_property
from flask_bcrypt import Bcrypt
from datetime import datetime


db = SQLAlchemy() 
bcrypt = Bcrypt()

# User model
class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    _password_hash = db.Column(db.String(128))
    email = db.Column(db.String(100))

    # Relationships
    lost_items = db.relationship('LostItem', back_populates='user', cascade='all, delete-orphan')
    found_items = db.relationship('FoundItem', back_populates='user', cascade='all, delete-orphan')
    claims = db.relationship('Claim', back_populates='user', cascade='all, delete-orphan')
    reward_payments = db.relationship('RewardPayment', back_populates='user', cascade='all, delete-orphan')

    
    
    serialize_rules = (
        "-lost_items",
        "-found_items",
        "-claims",
        "-reward_payments",
        
    )

    @validates('email')
    def validate_email(self, _, value):
        if '@' not in value:
            raise ValueError('@ must be a valid email address')
        return value

    @hybrid_property
    def password_hash(self):
        raise Exception('Password hashes may not be viewed.')

    @password_hash.setter
    def password_hash(self, password):
        password_hash = bcrypt.generate_password_hash(password.encode('utf-8'))
        self._password_hash = password_hash.decode('utf-8')

    @property
    def password(self):
        raise Exception('Password cannot be viewed.')

    @password.setter
    def password(self, password):
        self.password_hash = password

    def authenticate(self, password):
        return bcrypt.check_password_hash(self._password_hash, password.encode('utf-8'))


# Admin model
class Admin(db.Model, SerializerMixin):
    __tablename__ = 'admins'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    _password_hash = db.Column(db.String(128))

    # Relationships
    approved_reports = db.relationship('LostItem', back_populates='approved_by', cascade='all, delete-orphan')

    serialize_rules = ("-approved_reports.approved_by",)

    @validates('email')
    def validate_email(self, key, value):
        if '@' not in value:
            raise ValueError('@ must be a valid email address')
        return value

    @hybrid_property
    def password_hash(self):
        raise Exception('Password hashes may not be viewed.')

    @password_hash.setter
    def password_hash(self, password):
        password_hash = bcrypt.generate_password_hash(password.encode('utf-8'))
        self._password_hash = password_hash.decode('utf-8')

    @property
    def password(self):
        raise Exception('Password cannot be viewed.')

    @password.setter
    def password(self, password):
        self.password_hash = password

    def authenticate(self, password):
        return bcrypt.check_password_hash(self._password_hash, password.encode('utf-8'))


# LostItem model
class LostItem(db.Model, SerializerMixin):
    __tablename__ = 'lostitems'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    status = db.Column(db.String(50), default='lost')  
    
    reward = db.Column(db.Integer)
    place_lost = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    approved_by_id = db.Column(db.Integer, db.ForeignKey('admins.id'))
    image_url = db.Column(db.String(255))

    # Relationships
    user = db.relationship('User', back_populates='lost_items')
    approved_by = db.relationship('Admin', back_populates='approved_reports')
    claims = db.relationship('Claim', back_populates='lost_item')

    
    serialize_rules = (
        "-user",
        "-approved_by",
        "-claims",
    )



# FoundItem model
class FoundItem(db.Model, SerializerMixin):
    __tablename__ = 'founditems'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    status = db.Column(db.String(50), default='found')  # found, claimed, etc.
    reward = db.Column(db.Integer)
    place_lost = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    image_url = db.Column(db.String(255))

    # Relationships
    user = db.relationship('User', back_populates='found_items')
    claims = db.relationship('Claim', back_populates='found_item')

    serialize_rules = ("-user.found_items", "-claims.found_item")


# Claim model
class Claim(db.Model, SerializerMixin):
    __tablename__ = 'claims'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    founditem_id = db.Column(db.Integer, db.ForeignKey('founditems.id'), nullable=False)
    lostitem_id = db.Column(db.Integer, db.ForeignKey('lostitems.id'))
    is_approved = db.Column(db.Boolean, default=False)

    # Relationships
    user = db.relationship('User', back_populates='claims')
    found_item = db.relationship('FoundItem', back_populates='claims')
    lost_item = db.relationship('LostItem', back_populates='claims')

    serialize_rules = ("-user.claims", "-found_item.claims", "-lost_item.claims")


# Reward model
class Reward(db.Model, SerializerMixin):
    __tablename__ = 'rewards'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    points = db.Column(db.Integer, nullable=False)

    reward_payments = db.relationship('RewardPayment', back_populates='reward', cascade='all, delete-orphan')

    serialize_rules = ('-reward_payments.reward',)


# RewardPayment model
class RewardPayment(db.Model, SerializerMixin):
    __tablename__ = 'reward_payments'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    reward_id = db.Column(db.Integer, db.ForeignKey('rewards.id'), nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    date_paid = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationships
    user = db.relationship('User', back_populates='reward_payments')
    reward = db.relationship('Reward', back_populates='reward_payments')

    serialize_rules = ('-user.reward_payments', '-reward.reward_payments')


# Comment model
class Comment(db.Model, SerializerMixin):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    lost_item_id = db.Column(db.Integer, db.ForeignKey('lostitems.id'))
    found_item_id = db.Column(db.Integer, db.ForeignKey('founditems.id'))
    content = db.Column(db.Text, nullable=False)

    user = db.relationship('User')
    lost_item = db.relationship('LostItem', back_populates='comments')
    found_item = db.relationship('FoundItem', back_populates='comments')

    serialize_rules = ("-user.comments", "-lost_item.comments", "-found_item.comments")


LostItem.comments = db.relationship('Comment', back_populates='lost_item', cascade='all, delete-orphan')
FoundItem.comments = db.relationship('Comment', back_populates='found_item', cascade='all, delete-orphan')
