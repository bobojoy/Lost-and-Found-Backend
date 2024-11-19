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

    l1 = LostItem(name="Lost Phone", description="A smartphone, black color.", reward=100, place_lost="Nairobi", user=u1, image_url="https://i.pcmag.com/imagery/reviews/01Tnfpimnk3LJiQtnOa11eJ-10.fit_lim.size_919x518.v1711724157.jpg")
    l2 = LostItem(name="Lost Wallet", description="A leather wallet with ID cards.", reward=50, place_lost="Mombasa", user=u2, image_url="https://godbolegear.com/cdn/shop/files/Hand_Grained_Leather_Wallet_in_Chestnut_Leather.jpg?v=1717913883&width=1946")
    l3 = LostItem(name="Lost Watch", description="A gold wristwatch.", reward=200, place_lost="Kisumu", user=u3, image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRrrvRWDpRts3ffsdJKXCCqzfSaLNGc2Bxc5g&s")
    l4 = LostItem(name="Lost Bag", description="A large brown bag with clothes.", reward=150, place_lost="Nakuru", user=u4, image_url="https://www.purpink.co.ke/cdn/shop/files/3aaf440c-a6dd-48e2-9240-c3ccb345b8c0_enjoy_tote.jpg?v=1720507498")
    l5 = LostItem(name="Lost Keys", description="A set of house keys.", reward=20, place_lost="Eldoret", user=u5, image_url="https://www.welovekeys.co.uk/wp-content/uploads/2021/03/Federal-Keys.jpg")
    l6 = LostItem(name="Lost Glasses", description="A new pair.", reward=100, place_lost="kajiado", user=u6, image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSIUPLOUQCOUu7naEVOwCSE0I7kPyAa8w4-EA&s")
    l7 = LostItem(name="Lost Mouse", description="A white fancy mouse.", reward=50, place_lost="Voi", user=u7, image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQx3qARXQdkyZYhkR35oeGLmLoIWjODSqbNbA&s")
    l8 = LostItem(name="Lost Header", description="A black header.", reward=200, place_lost="Kapsabet", user=u8, image_url="https://res.cloudinary.com/agrimark/image/upload/v1683295833/uploads/assets/673973-1-a-Electricmate-Heavy-Duty-Rubber-Plug-Top-bdc2f5.jpg")
    l9 = LostItem(name="Lost Phone case", description="A white iphone case.", reward=150, place_lost="Limuru", user=u9, image_url="https://i5.walmartimages.com/seo/Clear-with-Silver-Glitter-Phone-Case-for-iPhone-12-iPhone-12-Pro_ab6d059c-6d4c-48ca-82dc-c36a6a5bc3d3.0df8ac93200e691c4862fd8396f743ed.jpeg")
    l10 = LostItem(name="Lost Bottle", description="A set of blue bottles.", reward=20, place_lost="Kinangop", user=u10, image_url="https://oceanbottle.co/cdn/shop/products/OceanBottle_OG_Front_Ocean-Blue_2048px.jpg?v=1653562177")
    l11 = LostItem(name="Lost AirPods", description="A white Oraimo pods .", reward=100, place_lost="Muranga", user=u11, image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRl-oBNK3R0IplEWkHsaXwXlikLPeGanrdf7g&s")
    l12 = LostItem(name="Lost Cable", description="A 5m cable .", reward=50, place_lost="Nyeri", user=u12, image_url="https://t3.ftcdn.net/jpg/01/60/74/74/360_F_160747489_2Y5WQ01DsWtC4o5JnYFd83ueZ7TRafwT.jpg")
    l13 = LostItem(name="Lost Charger", description="A yellow fancy charger", reward=200, place_lost="Kilifi", user=u13, image_url="https://c8.alamy.com/comp/HT5BRM/mobile-phone-charger-cable-isolate-on-white-background-HT5BRM.jpg")
    l14 = LostItem(name="Lost Extension", description="A white extension.", reward=150, place_lost="", user=u14, image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRkqNN68s9LdbQ4EOiZ1qzgahX61swBBo0xLw&s")
    l15 = LostItem(name="Lost Jacket", description="A brown leather jacket.", reward=20, place_lost="Garissa", user=u15, image_url="https://borgo28.com/cdn/shop/products/32005_BROW.jpg?v=1634235833")
    l16 = LostItem(name="Lost Chair", description="Grey fancy chair .", reward=100, place_lost="Wajir", user=u16, image_url="https://img.freepik.com/free-psd/tulip-chair-isolated-transparent-background_191095-13731.jpg")
    l17 = LostItem(name="Lost Laptop", description="A black Hp laptop.", reward=50, place_lost="Marsabit", user=u17, image_url="https://mombasacomputers.b-cdn.net/wp-content/uploads/2022/05/HP-15-dw1174nia-Intel-Core-i5-10th-Gen-8GB-RAM-1TB-HDD-15.6-Inches-HD-Touchscreen-Display-Windows-10-Home-1.jpg")
    l18 = LostItem(name="Lost Speaker", description="A black speaker.", reward=200, place_lost="Nandi", user=u18, image_url="https://www.sencor.com/getmedia/53d54418-3de4-4fe8-a503-5edb74cac646/35059173.jpg.aspx?width=2100&height=2100&ext=.jpg")
    l19 = LostItem(name="Lost Table", description="An orange grey table .", reward=150, place_lost="Narok", user=u19, image_url="https://www.shutterstock.com/image-photo/empty-beautiful-round-wood-table-600nw-2475179749.jpg")
    l20 = LostItem(name="Lost Wifi", description="A white wifi .", reward=20, place_lost="Turkana", user=u20, image_url="https://cdn.thewirecutter.com/wp-content/media/2024/03/reliable-wifi-gear-2048px-4648-3x2-1.jpg?auto=webp&quality=75&crop=3:2&width=1024")
    

    lost_items = [l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11, l12, l13, l14, l15, l16, l17, l18, l19, l20]
    db.session.add_all(lost_items)
    db.session.commit()
    print("Creating Found items...")

    f1 = FoundItem(name="Found Phone", description="A smartphone, black color.", reward=100, place_found="Nairobi", user=u1, image_url="https://i.pcmag.com/imagery/reviews/01Tnfpimnk3LJiQtnOa11eJ-10.fit_lim.size_919x518.v1711724157.jpg")
    f2 = FoundItem(name="Found Wallet", description="A leather wallet with ID cards.", reward=50, place_found="Mombasa", user=u2, image_url="https://godbolegear.com/cdn/shop/files/Hand_Grained_Leather_Wallet_in_Chestnut_Leather.jpg?v=1717913883&width=1946")
    f3 = FoundItem(name="Found Watch", description="A gold wristwatch.", reward=200, place_found="Kisumu", user=u3, image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRrrvRWDpRts3ffsdJKXCCqzfSaLNGc2Bxc5g&s")
    f4 = FoundItem(name="Found Bag", description="A large brown bag with clothes.", reward=150, place_found="Nakuru", user=u4, image_url="https://www.purpink.co.ke/cdn/shop/files/3aaf440c-a6dd-48e2-9240-c3ccb345b8c0_enjoy_tote.jpg?v=1720507498")
    f5 = FoundItem(name="Found Keys", description="A set of house keys.", reward=20, place_found="Eldoret", user=u5, image_url="https://www.welovekeys.co.uk/wp-content/uploads/2021/03/Federal-Keys.jpg")
    f6 = FoundItem(name="Found Glasses", description="A new pair.", reward=100, place_found="kajiado", user=u6, image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSIUPLOUQCOUu7naEVOwCSE0I7kPyAa8w4-EA&s")
    f7 = FoundItem(name="Found Mouse", description="A white fancy mouse.", reward=50, place_found="Voi", user=u7, image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQx3qARXQdkyZYhkR35oeGLmLoIWjODSqbNbA&s")
    f8 = FoundItem(name="Found Header", description="A black header.", reward=200, place_found="Kapsabet", user=u8, image_url="https://res.cloudinary.com/agrimark/image/upload/v1683295833/uploads/assets/673973-1-a-Electricmate-Heavy-Duty-Rubber-Plug-Top-bdc2f5.jpg")
    f9 = FoundItem(name="Found Phone case", description="A white iphone case.", reward=150, place_found="Limuru", user=u9, image_url="https://i5.walmartimages.com/seo/Clear-with-Silver-Glitter-Phone-Case-for-iPhone-12-iPhone-12-Pro_ab6d059c-6d4c-48ca-82dc-c36a6a5bc3d3.0df8ac93200e691c4862fd8396f743ed.jpeg")
    f10 = FoundItem(name="Found Bottle", description="A set of blue bottles.", reward=20, place_found="Kinangop", user=u10, image_url="https://oceanbottle.co/cdn/shop/products/OceanBottle_OG_Front_Ocean-Blue_2048px.jpg?v=1653562177")
    found_items = [f1, f2, f3, f4,f5 , f6, f7, f8, f9, f10]
    db.session.add_all(found_items)
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
    
    
      # Creating RewardPayments...
    print("Creating reward payments...")

    rp1 = RewardPayment(user=u1, reward=r1, amount=100)
    rp2 = RewardPayment(user=u2, reward=r2, amount=50)
    rp3 = RewardPayment(user=u3, reward=r3, amount=200)
    rp4 = RewardPayment(user=u4, reward=r4, amount=150)
    rp5 = RewardPayment(user=u5, reward=r5, amount=20)

    reward_payments = [rp1, rp2, rp3, rp4, rp5]
    db.session.add_all(reward_payments)
    db.session.commit()

    # Creating Comments...
    print("Creating comments...")

    c1 = Comment(user=u1, lost_item=l1, content="I lost my phone, please let me know if you find it.")
    c2 = Comment(user=u2, found_item=f2, content="I found a wallet. Can someone claim it?")
    c3 = Comment(user=u3, lost_item=l3, content="My watch is very precious. Please help me find it.")
    c4 = Comment(user=u4, found_item=f4, content="I found a bag near the park. Let me know if it’s yours.")
    c5 = Comment(user=u5, lost_item=l5, content="I lost my keys! If anyone finds them, please contact me.")

    comments = [c1, c2, c3, c4, c5]
    db.session.add_all(comments)
    db.session.commit()

    print("Seeding done!")



   