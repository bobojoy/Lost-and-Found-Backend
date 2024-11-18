from app import app 
from models import db, User, Admin, LostItem, FoundItem, Claim, Reward, RewardPayment, Comment

with app.app_context(): 
    
    # This will delete any existing rows so you can run the seed file multiple times without having duplicate entries in your database
    print("Deleting data ...")
    RewardPayment.query.delete()
    Claim.query.delete()
    Comment.query.delete()
    Reward.query.delete()
    LostItem.query.delete()
    FoundItem.query.delete()
    User.query.delete()
    Admin.query.delete()
    
    db.session.commit()

    # Creating Users...
    print("Creating users...")

    u1 = User(username="user1", email="user1@gmail.com", password="password123")
    u2 = User(username="user2", email="user2@gmail.com", password="password123")
    u3 = User(username="user3", email="user3@gmail.com", password="password123")
    u4 = User(username="user4", email="user4@gmail.com", password="password123")
    u5 = User(username="user5", email="user5@gmail.com", password="password123")
    u6 = User(username="user6", email="user6@gmail.com", password="password123")
    u7 = User(username="user7", email="user7@gmail.com", password="password123")
    u8 = User(username="user8", email="user8@gmail.com", password="password123")
    u9 = User(username="user9", email="user9@gmail.com", password="password123")
    u10 = User(username="user10", email="user10@gmail.com", password="password123")
    u11 = User(username="user11", email="user11@gmail.com", password="password123")
    u12 = User(username="user12", email="user12@gmail.com", password="password123")
    u13 = User(username="user13", email="user13@gmail.com", password="password123")
    u14 = User(username="user14", email="user14@gmail.com", password="password123")
    u15 = User(username="user15", email="user15@gmail.com", password="password123")
    u16 = User(username="user16", email="user16@gmail.com", password="password123")
    u17 = User(username="user17", email="user17@gmail.com", password="password123")
    u18 = User(username="user18", email="user18@gmail.com", password="password123")
    u19 = User(username="user19", email="user19@gmail.com", password="password123")
    u20 = User(username="user20", email="user20@gmail.com", password="password123")
    
    
              

    users = [u1, u2, u3, u4, u5, u6, u7, u8, u9, u10, u11, u12, u13, u14, u15, u16, u17, u18, u19, u20]
    db.session.add_all(users)
    db.session.commit()

   