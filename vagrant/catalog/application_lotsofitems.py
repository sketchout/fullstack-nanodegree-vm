from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# database_setup
from application_database_setup import Base, Category, Item, User

engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# Create dummy user
User1 = User(name="Robo Barista", email="tinnyTim@udacity.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User1)
session.commit()

###

category1 = Category(name="Soccer")
session.add(category1)
session.commit()

item11 = Item(name="Two shinguards", description="This is description of Two shinguards.",category=category1,user_id=1)
session.add(item11)
session.commit()

item12 = Item(name="Shinguards", description="This is description of singuards.",category=category1,user_id=1)
session.add(item12)
session.commit()

item13 = Item(name="Jersey", description="This is description of Jersey.",category=category1,user_id=1)
session.add(item13)
session.commit()

item14 = Item(name="Soccker Cleats", description="This is description of Soccker Cleats.",category=category1,user_id=1)
session.add(item14)
session.commit()

###

category2 = Category(name="Basketball")
session.add(category2)
session.commit()


###
#

category3 = Category(name="Baseball")
session.add(category3)
session.commit()

item31 = Item(name="Bat", description="This is description of Bat.",category=category3,user_id=1)
session.add(item31)
session.commit()

###
#
category4 = Category(name="Frisbee")
session.add(category4)
session.commit()


item41 = Item(name="Frisbee", description="This is description of Frisbee.",category=category4,user_id=1)
session.add(item41)
session.commit()


category5 = Category(name="Snowboarding")
session.add(category5)
session.commit()

item51 = Item(name="Snowboard", description="This is description of Snowboard.",category=category5,user_id=1)
session.add(item51)
session.commit()

item52 = Item(name="Googgles", description="This is description of Googgles.",category=category5,user_id=1)
session.add(item52)
session.commit()

###
#
category6 = Category(name="Rock Climbing")
session.add(category6)
session.commit()

category7 = Category(name="Foosball")
session.add(category7)
session.commit()

category8 = Category(name="Sketing")
session.add(category8)
session.commit()

category9 = Category(name="Hockey")
session.add(category9)
session.commit()