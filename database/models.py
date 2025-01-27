# coding: utf-8
from sqlalchemy import DECIMAL, DateTime  # API Logic Server GenAI assist
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

########################################################################################################################
# Classes describing database for SqlAlchemy ORM, initially created by schema introspection.
#
# Alter this file per your database maintenance policy
#    See https://apilogicserver.github.io/Docs/Project-Rebuild/#rebuilding
#
# Created:  January 27, 2025 15:41:50
# Database: sqlite:////tmp/tmp.gOqgObr65a-01JJM6PHJCJHHP3S4M72040Z20/ModernWebApp/database/db.sqlite
# Dialect:  sqlite
#
# mypy: ignore-errors
########################################################################################################################
 
from database.system.SAFRSBaseX import SAFRSBaseX, TestBase
from flask_login import UserMixin
import safrs, flask_sqlalchemy, os
from safrs import jsonapi_attr
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.sql.sqltypes import NullType
from typing import List

db = SQLAlchemy() 
Base = declarative_base()  # type: flask_sqlalchemy.model.DefaultMeta
metadata = Base.metadata

#NullType = db.String  # datatype fixup
#TIMESTAMP= db.TIMESTAMP

from sqlalchemy.dialects.sqlite import *

if os.getenv('APILOGICPROJECT_NO_FLASK') is None or os.getenv('APILOGICPROJECT_NO_FLASK') == 'None':
    Base = SAFRSBaseX   # enables rules to be used outside of Flask, e.g., test data loading
else:
    Base = TestBase     # ensure proper types, so rules work for data loading
    print('*** Models.py Using TestBase ***')



class Audit(Base):  # type: ignore
    """
    description: Tracks changes made to different entities for audit purposes.
    """
    __tablename__ = 'audits'
    _s_collection_name = 'Audit'  # type: ignore

    id = Column(Integer, primary_key=True)
    entity_name = Column(String, nullable=False)
    entity_id = Column(Integer)
    action = Column(String, nullable=False)
    timestamp = Column(DateTime)

    # parent relationships (access parent)

    # child relationships (access children)



class Component(Base):  # type: ignore
    """
    description: Defines different reusable components that can be placed within web pages.
    """
    __tablename__ = 'components'
    _s_collection_name = 'Component'  # type: ignore

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    css_class = Column(String)

    # parent relationships (access parent)

    # child relationships (access children)
    ComponentStyleList : Mapped[List["ComponentStyle"]] = relationship(back_populates="component")
    PageComponentList : Mapped[List["PageComponent"]] = relationship(back_populates="component")



class Page(Base):  # type: ignore
    """
    description: Stores the different web pages, including their titles and content.
    """
    __tablename__ = 'pages'
    _s_collection_name = 'Page'  # type: ignore

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    content = Column(Text)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    # parent relationships (access parent)

    # child relationships (access children)
    MenuList : Mapped[List["Menu"]] = relationship(back_populates="page")
    PageComponentList : Mapped[List["PageComponent"]] = relationship(back_populates="page")
    PageScriptList : Mapped[List["PageScript"]] = relationship(back_populates="page")



class Role(Base):  # type: ignore
    """
    description: Defines different roles for access and management functions within the website.
    """
    __tablename__ = 'roles'
    _s_collection_name = 'Role'  # type: ignore

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    # parent relationships (access parent)

    # child relationships (access children)
    UserRoleList : Mapped[List["UserRole"]] = relationship(back_populates="role")



class Script(Base):  # type: ignore
    """
    description: Stores JavaScript blocks or files that enhance interactivity.
    """
    __tablename__ = 'scripts'
    _s_collection_name = 'Script'  # type: ignore

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    code = Column(Text, nullable=False)

    # parent relationships (access parent)

    # child relationships (access children)
    PageScriptList : Mapped[List["PageScript"]] = relationship(back_populates="script")



class Style(Base):  # type: ignore
    """
    description: Stores different styles that can be applied to components.
    """
    __tablename__ = 'styles'
    _s_collection_name = 'Style'  # type: ignore

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    css = Column(Text, nullable=False)

    # parent relationships (access parent)

    # child relationships (access children)
    ComponentStyleList : Mapped[List["ComponentStyle"]] = relationship(back_populates="style")



class User(Base):  # type: ignore
    """
    description: A model representing users of the website, storing basic and essential information for account identification.
    """
    __tablename__ = 'users'
    _s_collection_name = 'User'  # type: ignore

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password_hash = Column(String, nullable=False)
    created_at = Column(DateTime)

    # parent relationships (access parent)

    # child relationships (access children)
    UserRoleList : Mapped[List["UserRole"]] = relationship(back_populates="user")



class ComponentStyle(Base):  # type: ignore
    """
    description: Join table for association between components and their styles.
    """
    __tablename__ = 'component_styles'
    _s_collection_name = 'ComponentStyle'  # type: ignore

    id = Column(Integer, primary_key=True)
    component_id = Column(ForeignKey('components.id'))
    style_id = Column(ForeignKey('styles.id'))

    # parent relationships (access parent)
    component : Mapped["Component"] = relationship(back_populates=("ComponentStyleList"))
    style : Mapped["Style"] = relationship(back_populates=("ComponentStyleList"))

    # child relationships (access children)



class Menu(Base):  # type: ignore
    """
    description: Represents navigational menus and their hierarchy.
    """
    __tablename__ = 'menus'
    _s_collection_name = 'Menu'  # type: ignore

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    parent_id = Column(ForeignKey('menus.id'))
    page_id = Column(ForeignKey('pages.id'))

    # parent relationships (access parent)
    page : Mapped["Page"] = relationship(back_populates=("MenuList"))
    parent_ : Mapped["Menu"] = relationship(remote_side=[id], back_populates=("MenuList"))

    # child relationships (access children)
    MenuList : Mapped[List["Menu"]] = relationship(back_populates="parent_")



class PageComponent(Base):  # type: ignore
    """
    description: Join table representing many-to-many relationship between pages and components, with order on the page.
    """
    __tablename__ = 'page_components'
    _s_collection_name = 'PageComponent'  # type: ignore

    id = Column(Integer, primary_key=True)
    page_id = Column(ForeignKey('pages.id'))
    component_id = Column(ForeignKey('components.id'))
    order = Column(Integer)

    # parent relationships (access parent)
    component : Mapped["Component"] = relationship(back_populates=("PageComponentList"))
    page : Mapped["Page"] = relationship(back_populates=("PageComponentList"))

    # child relationships (access children)



class PageScript(Base):  # type: ignore
    """
    description: Join table for association between pages and scripts utilized on them.
    """
    __tablename__ = 'page_scripts'
    _s_collection_name = 'PageScript'  # type: ignore

    id = Column(Integer, primary_key=True)
    page_id = Column(ForeignKey('pages.id'))
    script_id = Column(ForeignKey('scripts.id'))

    # parent relationships (access parent)
    page : Mapped["Page"] = relationship(back_populates=("PageScriptList"))
    script : Mapped["Script"] = relationship(back_populates=("PageScriptList"))

    # child relationships (access children)



class UserRole(Base):  # type: ignore
    """
    description: Join table to represent many-to-many relationship between users and roles.
    """
    __tablename__ = 'user_roles'
    _s_collection_name = 'UserRole'  # type: ignore

    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey('users.id'))
    role_id = Column(ForeignKey('roles.id'))

    # parent relationships (access parent)
    role : Mapped["Role"] = relationship(back_populates=("UserRoleList"))
    user : Mapped["User"] = relationship(back_populates=("UserRoleList"))

    # child relationships (access children)
