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
    """description: A model representing users of the website, storing basic and essential information for account identification."""
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password_hash = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

class Role(Base):
    """description: Defines different roles for access and management functions within the website."""
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

class UserRole(Base):
    """description: Join table to represent many-to-many relationship between users and roles."""
    __tablename__ = 'user_roles'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    role_id = Column(Integer, ForeignKey('roles.id'))

class Page(Base):
    """description: Stores the different web pages, including their titles and content."""
    __tablename__ = 'pages'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    content = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime)

class Component(Base):
    """description: Defines different reusable components that can be placed within web pages."""
    __tablename__ = 'components'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    css_class = Column(String, nullable=True)

class PageComponent(Base):
    """description: Join table representing many-to-many relationship between pages and components, with order on the page."""
    __tablename__ = 'page_components'
    id = Column(Integer, primary_key=True, autoincrement=True)
    page_id = Column(Integer, ForeignKey('pages.id'))
    component_id = Column(Integer, ForeignKey('components.id'))
    order = Column(Integer)

class Style(Base):
    """description: Stores different styles that can be applied to components."""
    __tablename__ = 'styles'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    css = Column(Text, nullable=False)

class ComponentStyle(Base):
    """description: Join table for association between components and their styles."""
    __tablename__ = 'component_styles'
    id = Column(Integer, primary_key=True, autoincrement=True)
    component_id = Column(Integer, ForeignKey('components.id'))
    style_id = Column(Integer, ForeignKey('styles.id'))

class Script(Base):
    """description: Stores JavaScript blocks or files that enhance interactivity."""
    __tablename__ = 'scripts'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    code = Column(Text, nullable=False)

class PageScript(Base):
    """description: Join table for association between pages and scripts utilized on them."""
    __tablename__ = 'page_scripts'
    id = Column(Integer, primary_key=True, autoincrement=True)
    page_id = Column(Integer, ForeignKey('pages.id'))
    script_id = Column(Integer, ForeignKey('scripts.id'))

class Audit(Base):
    """description: Tracks changes made to different entities for audit purposes."""
    __tablename__ = 'audits'
    id = Column(Integer, primary_key=True, autoincrement=True)
    entity_name = Column(String, nullable=False)
    entity_id = Column(Integer)
    action = Column(String, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)

class Menu(Base):
    """description: Represents navigational menus and their hierarchy."""
    __tablename__ = 'menus'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    parent_id = Column(Integer, ForeignKey('menus.id'), nullable=True)
    page_id = Column(Integer, ForeignKey('pages.id'))


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
    user1 = User(username="user1", email="user1@example.com", password_hash="hashed_pw1", created_at=date(2023, 10, 5))
    user2 = User(username="user2", email="user2@example.com", password_hash="hashed_pw2", created_at=date(2023, 10, 6))
    user3 = User(username="user3", email="user3@example.com", password_hash="hashed_pw3", created_at=date(2023, 10, 7))
    user4 = User(username="user4", email="user4@example.com", password_hash="hashed_pw4", created_at=date(2023, 10, 8))
    role1 = Role(name="Admin")
    role2 = Role(name="Editor")
    role3 = Role(name="Viewer")
    role4 = Role(name="Contributor")
    user_role1 = UserRole(user_id=1, role_id=1)
    user_role2 = UserRole(user_id=2, role_id=2)
    user_role3 = UserRole(user_id=3, role_id=1)
    user_role4 = UserRole(user_id=4, role_id=3)
    page1 = Page(title="HomePage", created_at=date(2023, 10, 5), updated_at=date(2023, 10, 8), content="<p>Hello World!</p>")
    page2 = Page(title="AboutUs", created_at=date(2023, 10, 5), updated_at=date(2023, 10, 8), content="<p>About Us Content</p>")
    page3 = Page(title="Services", created_at=date(2023, 10, 6), updated_at=date(2023, 10, 7), content="<p>Services Content</p>")
    page4 = Page(title="Contact", created_at=date(2023, 10, 7), updated_at=date(2023, 10, 8), content="<p>Contact Content</p>")
    component1 = Component(name="Header", css_class="header-class")
    component2 = Component(name="Footer", css_class="footer-class")
    component3 = Component(name="Sidebar", css_class="sidebar-class")
    component4 = Component(name="MainContent", css_class="main-class")
    page_component1 = PageComponent(page_id=1, component_id=1, order=1)
    page_component2 = PageComponent(page_id=1, component_id=2, order=2)
    page_component3 = PageComponent(page_id=2, component_id=1, order=1)
    page_component4 = PageComponent(page_id=2, component_id=4, order=2)
    style1 = Style(name="BasicStyles", css="body { margin: 0; }")
    style2 = Style(name="HeaderStyle", css="header { background-color: #333; }")
    style3 = Style(name="FooterStyle", css="footer { padding: 20px; }")
    style4 = Style(name="SidebarStyle", css="sidebar { width: 200px; }")
    component_style1 = ComponentStyle(component_id=1, style_id=1)
    component_style2 = ComponentStyle(component_id=2, style_id=2)
    component_style3 = ComponentStyle(component_id=3, style_id=3)
    component_style4 = ComponentStyle(component_id=4, style_id=4)
    script1 = Script(name="AlertScript", code="alert('Welcome to the site!');")
    script2 = Script(name="ValidationScript", code="function validate() { return true; }")
    script3 = Script(name="AnalyticsScript", code="console.log('Page loaded');")
    script4 = Script(name="CarouselScript", code="function startCarousel() { /* carousel code */ }")
    page_script1 = PageScript(page_id=1, script_id=1)
    page_script2 = PageScript(page_id=2, script_id=2)
    page_script3 = PageScript(page_id=3, script_id=3)
    page_script4 = PageScript(page_id=4, script_id=4)
    audit1 = Audit(entity_name="User", entity_id=1, action="Create", timestamp=date(2023, 10, 5))
    audit2 = Audit(entity_name="Page", entity_id=2, action="Update", timestamp=date(2023, 10, 6))
    audit3 = Audit(entity_name="Style", entity_id=3, action="Delete", timestamp=date(2023, 10, 7))
    audit4 = Audit(entity_name="Script", entity_id=4, action="Read", timestamp=date(2023, 10, 8))
    menu1 = Menu(title="Home", parent_id=None, page_id=1)
    menu2 = Menu(title="About", parent_id=None, page_id=2)
    menu3 = Menu(title="Services", parent_id=None, page_id=3)
    menu4 = Menu(title="Contact", parent_id=None, page_id=4)
    
    
    
    session.add_all([user1, user2, user3, user4, role1, role2, role3, role4, user_role1, user_role2, user_role3, user_role4, page1, page2, page3, page4, component1, component2, component3, component4, page_component1, page_component2, page_component3, page_component4, style1, style2, style3, style4, component_style1, component_style2, component_style3, component_style4, script1, script2, script3, script4, page_script1, page_script2, page_script3, page_script4, audit1, audit2, audit3, audit4, menu1, menu2, menu3, menu4])
    session.commit()
    # end of test data
    
    
except Exception as exc:
    print(f'Test Data Error: {exc}')
