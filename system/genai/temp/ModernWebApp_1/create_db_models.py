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

class User(Base):
    """description: Represents a user in the system."""
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)
    date_joined = Column(DateTime)

class Profile(Base):
    """description: Holds additional information about a user."""
    __tablename__ = 'profile'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    first_name = Column(String)
    last_name = Column(String)
    bio = Column(String)
    profile_pic_url = Column(String)

class Category(Base):
    """description: Categories for organizing content on the website."""
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)

class Template(Base):
    """description: Represents a website template including HTML, CSS, and JS code."""
    __tablename__ = 'template'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    html = Column(String)
    css = Column(String)
    js = Column(String)

class Page(Base):
    """description: Website pages content storage."""
    __tablename__ = 'page'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

class Post(Base):
    """description: Blog posts or articles published by users."""
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(String)
    author_id = Column(Integer, ForeignKey('user.id'))
    created_at = Column(DateTime)

class Comment(Base):
    """description: Comments on blog posts by users."""
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    content = Column(String)
    post_id = Column(Integer, ForeignKey('post.id'))
    author_id = Column(Integer, ForeignKey('user.id'))
    created_at = Column(DateTime)

class Tag(Base):
    """description: Tags for labeling content."""
    __tablename__ = 'tag'
    id = Column(Integer, primary_key=True)
    name = Column(String)

class PostTag(Base):
    """description: Association table for many-to-many relationship between posts and tags."""
    __tablename__ = 'post_tag'
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('post.id'))
    tag_id = Column(Integer, ForeignKey('tag.id'))

class Like(Base):
    """description: Tracks likes on posts by users."""
    __tablename__ = 'like'
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('post.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
    created_at = Column(DateTime)

class Settings(Base):
    """description: User-specific settings configuration."""
    __tablename__ = 'settings'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    receive_emails = Column(Boolean)
    language = Column(String)

class Notification(Base):
    """description: Notifications for user activities."""
    __tablename__ = 'notification'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    content = Column(String)
    is_read = Column(Boolean)
    created_at = Column(DateTime)


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
    user_1 = User(username="john_doe", email="john@example.com", password="securepassword", date_joined=date(2023, 1, 1))
    user_2 = User(username="jane_doe", email="jane@example.com", password="anotherpassword", date_joined=date(2023, 2, 2))
    user_3 = User(username="alice", email="alice@example.com", password="yetanotherpassword", date_joined=date(2023, 3, 3))
    user_4 = User(username="bob", email="bob@example.com", password="password123", date_joined=date(2023, 4, 4))
    profile_1 = Profile(user_id=1, first_name="John", last_name="Doe", bio="Software Developer", profile_pic_url="/images/john.jpg")
    profile_2 = Profile(user_id=2, first_name="Jane", last_name="Doe", bio="Graphic Designer", profile_pic_url="/images/jane.jpg")
    profile_3 = Profile(user_id=3, first_name="Alice", last_name="Smith", bio="Data Scientist", profile_pic_url="/images/alice.jpg")
    profile_4 = Profile(user_id=4, first_name="Bob", last_name="Johnson", bio="Product Manager", profile_pic_url="/images/bob.jpg")
    category_1 = Category(name="Technology", description="All about the latest in technology.")
    category_2 = Category(name="Art", description="Inspiring art from around the world.")
    category_3 = Category(name="Science", description="Exploring scientific discoveries.")
    category_4 = Category(name="Travel", description="Adventures across the globe.")
    template_1 = Template(name="Minimalist", html="<html></html>", css="body { }
    ", js="function() {}")
    template_2 = Template(name="Modern", html="<div></div>", css=".modern { }
    ", js="var x = 10;")
    template_3 = Template(name="Classic", html="<p></p>", css=".classic { }
    ", js="alert('Hello')")
    template_4 = Template(name="Dynamic", html="<span></span>", css=".dynamic { }
    ", js="function dynamic() {}")
    page_1 = Page(title="Home", content="<h1>Welcome</h1>", created_at=date(2023, 1, 1), updated_at=date(2023, 1, 2))
    page_2 = Page(title="Contact Us", content="<h1>Contact Information</h1>", created_at=date(2023, 1, 2), updated_at=date(2023, 1, 3))
    page_3 = Page(title="About", content="<h1>About Us</h1>", created_at=date(2023, 1, 3), updated_at=date(2023, 1, 4))
    page_4 = Page(title="Services", content="<h1>Our Services</h1>", created_at=date(2023, 1, 4), updated_at=date(2023, 1, 5))
    post_1 = Post(title="Intro to SQLAlchemy", content="How to use SQLAlchemy as ORM in Python.", author_id=1, created_at=date(2023, 1, 1))
    post_2 = Post(title="Benefits of Remote Work", content="Exploring the advantages of working remotely.", author_id=2, created_at=date(2023, 2, 1))
    post_3 = Post(title="The Future of AI", content="Understanding AI advancements.", author_id=3, created_at=date(2023, 3, 1))
    post_4 = Post(title="Gardening Tips", content="How to start a successful garden.", author_id=4, created_at=date(2023, 4, 1))
    comment_1 = Comment(content="Great introduction!", post_id=1, author_id=2, created_at=date(2023, 1, 2))
    comment_2 = Comment(content="Totally agree with this.", post_id=2, author_id=3, created_at=date(2023, 2, 10))
    comment_3 = Comment(content="Well written article.", post_id=3, author_id=1, created_at=date(2023, 3, 15))
    comment_4 = Comment(content="Useful tips.", post_id=4, author_id=4, created_at=date(2023, 4, 20))
    tag_1 = Tag(name="Python")
    tag_2 = Tag(name="Remote Work")
    tag_3 = Tag(name="AI")
    tag_4 = Tag(name="Gardening")
    post_tag_1 = PostTag(post_id=1, tag_id=1)
    post_tag_2 = PostTag(post_id=2, tag_id=2)
    post_tag_3 = PostTag(post_id=3, tag_id=3)
    post_tag_4 = PostTag(post_id=4, tag_id=4)
    like_1 = Like(post_id=1, user_id=3, created_at=date(2023, 1, 3))
    like_2 = Like(post_id=2, user_id=4, created_at=date(2023, 2, 12))
    like_3 = Like(post_id=3, user_id=1, created_at=date(2023, 3, 16))
    like_4 = Like(post_id=4, user_id=2, created_at=date(2023, 4, 21))
    settings_1 = Settings(user_id=1, receive_emails=True, language="en")
    settings_2 = Settings(user_id=2, receive_emails=False, language="fr")
    settings_3 = Settings(user_id=3, receive_emails=True, language="es")
    settings_4 = Settings(user_id=4, receive_emails=False, language="de")
    notification_1 = Notification(user_id=1, content="You have a new comment.", is_read=False, created_at=date(2023, 1, 4))
    notification_2 = Notification(user_id=2, content="Your post was liked.", is_read=False, created_at=date(2023, 2, 13))
    notification_3 = Notification(user_id=3, content="Profile updated successfully.", is_read=True, created_at=date(2023, 3, 17))
    notification_4 = Notification(user_id=4, content="New message received.", is_read=False, created_at=date(2023, 4, 22))
    
    
    
    session.add_all([user_1, user_2, user_3, user_4, profile_1, profile_2, profile_3, profile_4, category_1, category_2, category_3, category_4, template_1, template_2, template_3, template_4, page_1, page_2, page_3, page_4, post_1, post_2, post_3, post_4, comment_1, comment_2, comment_3, comment_4, tag_1, tag_2, tag_3, tag_4, post_tag_1, post_tag_2, post_tag_3, post_tag_4, like_1, like_2, like_3, like_4, settings_1, settings_2, settings_3, settings_4, notification_1, notification_2, notification_3, notification_4])
    session.commit()
    # end of test data
    
    
except Exception as exc:
    print(f'Test Data Error: {exc}')
