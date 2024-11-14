from app import app, db
from models import User, Item, Claim, Reward, Comment, ItemImage

def seed_data():
    # Add test users
    user1 = User(username="john_doe", email="john@example.com")
    user1.set_password("password123")
    user2 = User(username="jane_doe", email="jane@example.com")
    user2.set_password("password123")
    
    db.session.add(user1)
    db.session.add(user2)
    db.session.commit()
    
    # Add test items
    item1 = Item(title="Lost Wallet", description="A black leather wallet", user_id=user1.id)
    item2 = Item(title="Found Phone", description="An iPhone 12 found on the street", user_id=user2.id)
    
    db.session.add(item1)
    db.session.add(item2)
    db.session.commit()
    
    # Add test claims
    claim1 = Claim(user_id=user2.id, item_id=item1.id)
    db.session.add(claim1)
    db.session.commit()
    
    # Add test reward
    reward1 = Reward(title="Travel Voucher", description="A voucher for free flight tickets", points=100)
    db.session.add(reward1)
    db.session.commit()
    
    # Add comments on items
    comment1 = Comment(user_id=user1.id, item_id=item2.id, content="I lost my wallet, hope I can get it back!")
    db.session.add(comment1)
    db.session.commit()
    
    # Add item images
    image1 = ItemImage(item_id=item1.id, url="https://example.com/wallet.jpg")
    db.session.add(image1)
    db.session.commit()

    print("Seed data added successfully!")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Create all tables if not already created
        seed_data()
