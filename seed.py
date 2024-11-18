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

    # Creating Admins...
    print("Creating admins...")

    admin1 = Admin(username="admin1", email="admin1@admin.com", password="adminpass")
    admin2 = Admin(username="admin2", email="admin2@admin.com", password="adminpass")

    admins = [admin1, admin2]
    db.session.add_all(admins)
    db.session.commit()

    # Creating LostItems...
    print("Creating lost items...")

    l1 = LostItem(name="Lost Phone", description="A smartphone, black color.", reward=100, place_lost="Nairobi", user=u1, image_url="https://example.com/lost_phone.jpg")
    l2 = LostItem(name="Lost Wallet", description="A leather wallet with ID cards.", reward=50, place_lost="Mombasa", user=u2, image_url="https://example.com/lost_wallet.jpg")
    l3 = LostItem(name="Lost Watch", description="A gold wristwatch.", reward=200, place_lost="Kisumu", user=u3, image_url="https://example.com/lost_watch.jpg")
    l4 = LostItem(name="Lost Bag", description="A large brown bag with clothes.", reward=150, place_lost="Nakuru", user=u4, image_url="https://example.com/lost_bag.jpg")
    l5 = LostItem(name="Lost Keys", description="A set of house keys.", reward=20, place_lost="Eldoret", user=u5, image_url="https://example.com/lost_keys.jpg")
    l6 = LostItem(name="Lost Phone", description="A smartphone, black color.", reward=100, place_lost="kajiado", user=u6, image_url="https://example.com/lost_phone.jpg")
    l7 = LostItem(name="Lost Wallet", description="A leather wallet with ID cards.", reward=50, place_lost="Voi", user=u7, image_url="https://example.com/lost_wallet.jpg")
    l8 = LostItem(name="Lost Watch", description="A gold wristwatch.", reward=200, place_lost="Kapsabet", user=u8, image_url="https://example.com/lost_watch.jpg")
    l9 = LostItem(name="Lost Bag", description="A large brown bag with clothes.", reward=150, place_lost="Limuru", user=u9, image_url="https://example.com/lost_bag.jpg")
    l10 = LostItem(name="Lost Bottle", description="A set of blue bottles.", reward=20, place_lost="Kinangop", user=u10, image_url="https://example.com/lost_keys.jpg")
    l11 = LostItem(name="Lost AirPods", description="A white Oraimo pods .", reward=100, place_lost="Muranga", user=u11, image_url="https://example.com/lost_phone.jpg")
    l12 = LostItem(name="Lost Cable", description="A 5m cable .", reward=50, place_lost="Nyeri", user=u12, image_url="https://example.com/lost_wallet.jpg")
    l13 = LostItem(name="Lost Charger", description="A yellow fancy charger", reward=200, place_lost="Kilifi", user=u13, image_url="https://example.com/lost_watch.jpg")
    l14 = LostItem(name="Lost Extension", description="A white extension.", reward=150, place_lost="", user=u14, image_url="https://example.com/lost_bag.jpg")
    l15 = LostItem(name="Lost Jacket", description="A brown leather jacket.", reward=20, place_lost="Garissa", user=u15, image_url="https://example.com/lost_keys.jpg")
    l16 = LostItem(name="Lost Chairs", description="Grey fancy chair .", reward=100, place_lost="Wajir", user=u16, image_url="https://example.com/lost_phone.jpg")
    l17 = LostItem(name="Lost Laptop", description="A black Hp laptop.", reward=50, place_lost="Marsabit", user=u17, image_url="https://example.com/lost_wallet.jpg")
    l18 = LostItem(name="Lost Speaker", description="A black speaker.", reward=200, place_lost="Nandi", user=u18, image_url="https://example.com/lost_watch.jpg")
    l19 = LostItem(name="Lost Table", description="An orange grey table .", reward=150, place_lost="Narok", user=u19, image_url="https://example.com/lost_bag.jpg")
    l20 = LostItem(name="Lost Wifi", description="A white wifi .", reward=20, place_lost="Turkana", user=u20, image_url="https://example.com/lost_keys.jpg")
    

    lost_items = [l1, l2, l3, l4, , l6, l7, l8, l9, l10, l11, l12, l13, l14, l15, l16, l17, l18, l19, l20]
    db.session.add_all(lost_items)
    db.session.commit()
    
     # Creating Claims...
    print("Creating claims...")

    claim1 = Claim(user=u1, found_item=f1, lost_item=l1, is_approved=True)
    claim2 = Claim(user=u2, found_item=f2, lost_item=l2, is_approved=False)
    claim3 = Claim(user=u3, found_item=f3, lost_item=l3, is_approved=True)
    claim4 = Claim(user=u4, found_item=f4, lost_item=l4, is_approved=True)
    claim5 = Claim(user=u5, found_item=f5, lost_item=l5, is_approved=False)
     claims = [claim1, claim2, claim3, claim4, claim5]
    db.session.add_all(claims)
    db.session.commit()
    
    
     # Creating Rewards...
    print("Creating rewards...")

    r1 = Reward(title="Reward for Lost Phone", description="Reward for returning a lost phone.", points=100)
    r2 = Reward(title="Reward for Lost Wallet", description="Reward for returning a lost wallet.", points=50)
    r3 = Reward(title="Reward for Lost Watch", description="Reward for returning a lost watch.", points=200)
    r4 = Reward(title="Reward for Lost Bag", description="Reward for returning a lost bag.", points=150)
    r5 = Reward(title="Reward for Lost Keys", description="Reward for returning lost keys.", points=20)

    rewards = [r1, r2, r3, r4, r5]
    db.session.add_all(rewards)
    db.session.commit()



   