# using resolved_model self.resolved_model FIXME
# created from response, to create create_db_models.sqlite, with test data
#    that is used to create project
# should run without error in manager 
#    if not, check for decimal, indent, or import issues

import decimal
import logging
import sqlalchemy
from sqlalchemy.sql import func 
from decimal import Decimal
from logic_bank.logic_bank import Rule
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, Date, DateTime, Numeric, Boolean, Text, DECIMAL
from sqlalchemy.types import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from datetime import date   
from datetime import datetime
from typing import List


logging.getLogger('sqlalchemy.engine.Engine').disabled = True  # remove for additional logging

Base = declarative_base()  # from system/genai/create_db_models_inserts/create_db_models_prefix.py


from sqlalchemy.dialects.sqlite import *

class User(db.Model):
    """description: Handles user account data"""
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)
    date_joined = Column(DateTime)

class Profile(db.Model):
    """description: Contains additional user profile information"""
    __tablename__ = 'profile'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    bio = Column(String)
    website = Column(String)
    location = Column(String)

class Post(db.Model):
    """description: Stores blog or content posts"""
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    title = Column(String)
    content = Column(Text)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

class Comment(db.Model):
    """description: Contains comments on posts"""
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True, autoincrement=True)
    post_id = Column(Integer, ForeignKey('post.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
    content = Column(Text)
    created_at = Column(DateTime)

class Category(db.Model):
    """description: Represents categories for posts"""
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    description = Column(String)

class PostCategory(db.Model):
    """description: Associates posts with categories"""
    __tablename__ = 'post_category'
    id = Column(Integer, primary_key=True, autoincrement=True)
    post_id = Column(Integer, ForeignKey('post.id'))
    category_id = Column(Integer, ForeignKey('category.id'))

class Tag(db.Model):
    """description: Represents tags that can be applied to posts"""
    __tablename__ = 'tag'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)

class PostTag(db.Model):
    """description: Associates posts with tags"""
    __tablename__ = 'post_tag'
    id = Column(Integer, primary_key=True, autoincrement=True)
    post_id = Column(Integer, ForeignKey('post.id'))
    tag_id = Column(Integer, ForeignKey('tag.id'))

class Like(db.Model):
    """description: Stores likes/endorsements for posts"""
    __tablename__ = 'like'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))

class Image(db.Model):
    """description: Stores images associated with posts"""
    __tablename__ = 'image'
    id = Column(Integer, primary_key=True, autoincrement=True)
    post_id = Column(Integer, ForeignKey('post.id'))
    url = Column(String)
    description = Column(String)

class Notification(db.Model):
    """description: Represents notifications for users"""
    __tablename__ = 'notification'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    message = Column(String)
    created_at = Column(DateTime)

class Message(db.Model):
    """description: Handles messages between users"""
    __tablename__ = 'message'
    id = Column(Integer, primary_key=True, autoincrement=True)
    sender_id = Column(Integer, ForeignKey('user.id'))
    receiver_id = Column(Integer, ForeignKey('user.id'))
    content = Column(Text)
    sent_at = Column(DateTime)


# end of model classes


try:
    
    
    # ALS/GenAI: Create an SQLite database
    import os
    mgr_db_loc = True
    if mgr_db_loc:
        print(f'creating in manager: sqlite:///system/genai/temp/create_db_models.sqlite')
        engine = create_engine('sqlite:///system/genai/temp/create_db_models.sqlite')
    else:
        current_file_path = os.path.dirname(__file__)
        print(f'creating at current_file_path: {current_file_path}')
        engine = create_engine(f'sqlite:///{current_file_path}/create_db_models.sqlite')
    Base.metadata.create_all(engine)
    
    
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # ALS/GenAI: Prepare for sample data
    
    
    session.commit()
    user1 = User(username="johndoe", email="johndoe@example.com", password="Johndoe123", date_joined=date(2022, 1, 20))
    user2 = User(username="janedoe", email="janedoe@example.com", password="Janedoe123", date_joined=date(2022, 2, 15))
    profile1 = Profile(user_id=1, bio="Software Developer", website="http://johndoesite.com", location="New York")
    profile2 = Profile(user_id=2, bio="Graphic Designer", website="http://janedoesite.com", location="Los Angeles")
    post1 = Post(user_id=1, title="My First Post", content="This is the body of my first post.", created_at=date(2022, 3, 1), updated_at=date(2022, 3, 1))
    post2 = Post(user_id=2, title="Welcome to My Blog", content="I'm excited to start this new journey.", created_at=date(2022, 3, 5), updated_at=date(2022, 3, 6))
    comment1 = Comment(post_id=1, user_id=2, content="Great post!", created_at=date(2022, 3, 2))
    comment2 = Comment(post_id=2, user_id=1, content="Thank you!", created_at=date(2022, 3, 6))
    
    
    
    session.add_all([user1, user2, profile1, profile2, post1, post2, comment1, comment2])
    session.commit()
    # end of test data
    
    
except Exception as exc:
    print(f'Test Data Error: {exc}')
