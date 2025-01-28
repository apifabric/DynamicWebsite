import logging
import logging.config
import json
import os
import sys

os.environ["APILOGICPROJECT_NO_FLASK"] = "1"  # must be present before importing models

import traceback
import yaml
from datetime import date, datetime
from pathlib import Path
from decimal import Decimal
from sqlalchemy import (Boolean, Column, Date, DateTime, DECIMAL, Float, ForeignKey, Integer, Numeric, String, Text, create_engine)
from sqlalchemy.dialects.sqlite import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func

current_path = Path(__file__)
project_path = (current_path.parent.parent.parent).resolve()
sys.path.append(str(project_path))

from logic_bank.logic_bank import LogicBank, Rule
from logic import declare_logic
from database.models import *
from database.models import Base

project_dir = Path(os.getenv("PROJECT_DIR",'./')).resolve()

assert str(os.getcwd()) == str(project_dir), f"Current directory must be {project_dir}"

data_log : list[str] = []

logging_config = project_dir / 'config/logging.yml'
if logging_config.is_file():
    with open(logging_config,'rt') as f:  
        config=yaml.safe_load(f.read())
    logging.config.dictConfig(config)
logic_logger = logging.getLogger('logic_logger')
logic_logger.setLevel(logging.DEBUG)
logic_logger.info(f'..  logic_logger: {logic_logger}')

db_url_path = project_dir.joinpath('database/test_data/db.sqlite')
db_url = f'sqlite:///{db_url_path.resolve()}'
logging.info(f'..  db_url: {db_url}')
logging.info(f'..  cwd: {os.getcwd()}')
logging.info(f'..  python_loc: {sys.executable}')
logging.info(f'..  test_data_loader version: 1.1')
data_log.append(f'..  db_url: {db_url}')
data_log.append(f'..  cwd: {os.getcwd()}')
data_log.append(f'..  python_loc: {sys.executable}')
data_log.append(f'..  test_data_loader version: 1.1')

if db_url_path.is_file():
    db_url_path.unlink()

try:
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)  # note: LogicBank activated for this session only
    session = Session()
    LogicBank.activate(session=session, activator=declare_logic.declare_logic)
except Exception as e: 
    logging.error(f'Error creating engine: {e}')
    data_log.append(f'Error creating engine: {e}')
    print('\n'.join(data_log))
    with open(project_dir / 'database/test_data/test_data_code_log.txt', 'w') as log_file:
        log_file.write('\n'.join(data_log))
    print('\n'.join(data_log))
    raise

logging.info(f'..  LogicBank activated')
data_log.append(f'..  LogicBank activated')

restart_count = 0
has_errors = True
succeeded_hashes = set()

while restart_count < 5 and has_errors:
    has_errors = False
    restart_count += 1
    data_log.append("print(Pass: " + str(restart_count) + ")" )
    try:
        if not -4229785142934285222 in succeeded_hashes:  # avoid duplicate inserts
            instance = user1 = User(username="user1", email="user1@example.com", password_hash="hashed_pw1", created_at=date(2023, 10, 5))
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-4229785142934285222)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -7332043769798400549 in succeeded_hashes:  # avoid duplicate inserts
            instance = user2 = User(username="user2", email="user2@example.com", password_hash="hashed_pw2", created_at=date(2023, 10, 6))
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-7332043769798400549)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -343225834978986775 in succeeded_hashes:  # avoid duplicate inserts
            instance = user3 = User(username="user3", email="user3@example.com", password_hash="hashed_pw3", created_at=date(2023, 10, 7))
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-343225834978986775)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -4189089725464686630 in succeeded_hashes:  # avoid duplicate inserts
            instance = user4 = User(username="user4", email="user4@example.com", password_hash="hashed_pw4", created_at=date(2023, 10, 8))
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-4189089725464686630)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 4937628186178609033 in succeeded_hashes:  # avoid duplicate inserts
            instance = role1 = Role(name="Admin")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(4937628186178609033)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -2913566362300352810 in succeeded_hashes:  # avoid duplicate inserts
            instance = role2 = Role(name="Editor")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-2913566362300352810)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 7593271661720077113 in succeeded_hashes:  # avoid duplicate inserts
            instance = role3 = Role(name="Viewer")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(7593271661720077113)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 7342899630968703915 in succeeded_hashes:  # avoid duplicate inserts
            instance = role4 = Role(name="Contributor")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(7342899630968703915)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -3208910142315669696 in succeeded_hashes:  # avoid duplicate inserts
            instance = user_role1 = UserRole(user_id=1, role_id=1)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-3208910142315669696)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 825635376102266044 in succeeded_hashes:  # avoid duplicate inserts
            instance = user_role2 = UserRole(user_id=2, role_id=2)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(825635376102266044)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 6066829197989547701 in succeeded_hashes:  # avoid duplicate inserts
            instance = user_role3 = UserRole(user_id=3, role_id=1)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(6066829197989547701)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -962913510157604120 in succeeded_hashes:  # avoid duplicate inserts
            instance = user_role4 = UserRole(user_id=4, role_id=3)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-962913510157604120)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -7535169851507912633 in succeeded_hashes:  # avoid duplicate inserts
            instance = page1 = Page(title="HomePage", created_at=date(2023, 10, 5), updated_at=date(2023, 10, 8), content="<p>Hello World!</p>")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-7535169851507912633)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -4544324279050539680 in succeeded_hashes:  # avoid duplicate inserts
            instance = page2 = Page(title="AboutUs", created_at=date(2023, 10, 5), updated_at=date(2023, 10, 8), content="<p>About Us Content</p>")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-4544324279050539680)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 3205329482357290314 in succeeded_hashes:  # avoid duplicate inserts
            instance = page3 = Page(title="Services", created_at=date(2023, 10, 6), updated_at=date(2023, 10, 7), content="<p>Services Content</p>")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(3205329482357290314)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -5435269230818888167 in succeeded_hashes:  # avoid duplicate inserts
            instance = page4 = Page(title="Contact", created_at=date(2023, 10, 7), updated_at=date(2023, 10, 8), content="<p>Contact Content</p>")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-5435269230818888167)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -8475563875333963744 in succeeded_hashes:  # avoid duplicate inserts
            instance = component1 = Component(name="Header", css_class="header-class")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-8475563875333963744)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 5096116059637729774 in succeeded_hashes:  # avoid duplicate inserts
            instance = component2 = Component(name="Footer", css_class="footer-class")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(5096116059637729774)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 7124134965713880270 in succeeded_hashes:  # avoid duplicate inserts
            instance = component3 = Component(name="Sidebar", css_class="sidebar-class")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(7124134965713880270)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -2019899931497567638 in succeeded_hashes:  # avoid duplicate inserts
            instance = component4 = Component(name="MainContent", css_class="main-class")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-2019899931497567638)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 4423899586330691058 in succeeded_hashes:  # avoid duplicate inserts
            instance = page_component1 = PageComponent(page_id=1, component_id=1, order=1)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(4423899586330691058)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 4690399870275578246 in succeeded_hashes:  # avoid duplicate inserts
            instance = page_component2 = PageComponent(page_id=1, component_id=2, order=2)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(4690399870275578246)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -6225593757571314990 in succeeded_hashes:  # avoid duplicate inserts
            instance = page_component3 = PageComponent(page_id=2, component_id=1, order=1)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-6225593757571314990)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 1492335807015896708 in succeeded_hashes:  # avoid duplicate inserts
            instance = page_component4 = PageComponent(page_id=2, component_id=4, order=2)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(1492335807015896708)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -6423048879955811114 in succeeded_hashes:  # avoid duplicate inserts
            instance = style1 = Style(name="BasicStyles", css="body { margin: 0; }")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-6423048879955811114)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -7251482267635456412 in succeeded_hashes:  # avoid duplicate inserts
            instance = style2 = Style(name="HeaderStyle", css="header { background-color: #333; }")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-7251482267635456412)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 468930372780463522 in succeeded_hashes:  # avoid duplicate inserts
            instance = style3 = Style(name="FooterStyle", css="footer { padding: 20px; }")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(468930372780463522)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 4837049761857258273 in succeeded_hashes:  # avoid duplicate inserts
            instance = style4 = Style(name="SidebarStyle", css="sidebar { width: 200px; }")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(4837049761857258273)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -8812959211949291931 in succeeded_hashes:  # avoid duplicate inserts
            instance = component_style1 = ComponentStyle(component_id=1, style_id=1)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-8812959211949291931)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 6022590990865717235 in succeeded_hashes:  # avoid duplicate inserts
            instance = component_style2 = ComponentStyle(component_id=2, style_id=2)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(6022590990865717235)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 5867103485221831976 in succeeded_hashes:  # avoid duplicate inserts
            instance = component_style3 = ComponentStyle(component_id=3, style_id=3)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(5867103485221831976)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 5804865666505479735 in succeeded_hashes:  # avoid duplicate inserts
            instance = component_style4 = ComponentStyle(component_id=4, style_id=4)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(5804865666505479735)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 7874458135319024605 in succeeded_hashes:  # avoid duplicate inserts
            instance = script1 = Script(name="AlertScript", code="alert('Welcome to the site!');")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(7874458135319024605)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 6279138121364469702 in succeeded_hashes:  # avoid duplicate inserts
            instance = script2 = Script(name="ValidationScript", code="function validate() { return true; }")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(6279138121364469702)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 3013487235861334529 in succeeded_hashes:  # avoid duplicate inserts
            instance = script3 = Script(name="AnalyticsScript", code="console.log('Page loaded');")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(3013487235861334529)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -489660494459500909 in succeeded_hashes:  # avoid duplicate inserts
            instance = script4 = Script(name="CarouselScript", code="function startCarousel() { /* carousel code */ }")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-489660494459500909)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 3953508977745991351 in succeeded_hashes:  # avoid duplicate inserts
            instance = page_script1 = PageScript(page_id=1, script_id=1)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(3953508977745991351)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -8056307436908805985 in succeeded_hashes:  # avoid duplicate inserts
            instance = page_script2 = PageScript(page_id=2, script_id=2)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-8056307436908805985)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -8908880046625387100 in succeeded_hashes:  # avoid duplicate inserts
            instance = page_script3 = PageScript(page_id=3, script_id=3)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-8908880046625387100)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 2874317698897225360 in succeeded_hashes:  # avoid duplicate inserts
            instance = page_script4 = PageScript(page_id=4, script_id=4)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(2874317698897225360)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 5585214465616045891 in succeeded_hashes:  # avoid duplicate inserts
            instance = audit1 = Audit(entity_name="User", entity_id=1, action="Create", timestamp=date(2023, 10, 5))
            session.add(instance)
            session.commit()
            succeeded_hashes.add(5585214465616045891)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 2238285674119277278 in succeeded_hashes:  # avoid duplicate inserts
            instance = audit2 = Audit(entity_name="Page", entity_id=2, action="Update", timestamp=date(2023, 10, 6))
            session.add(instance)
            session.commit()
            succeeded_hashes.add(2238285674119277278)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -4918210921313471783 in succeeded_hashes:  # avoid duplicate inserts
            instance = audit3 = Audit(entity_name="Style", entity_id=3, action="Delete", timestamp=date(2023, 10, 7))
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-4918210921313471783)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 7076649671250477139 in succeeded_hashes:  # avoid duplicate inserts
            instance = audit4 = Audit(entity_name="Script", entity_id=4, action="Read", timestamp=date(2023, 10, 8))
            session.add(instance)
            session.commit()
            succeeded_hashes.add(7076649671250477139)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 6259202330215998153 in succeeded_hashes:  # avoid duplicate inserts
            instance = menu1 = Menu(title="Home", parent_id=None, page_id=1)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(6259202330215998153)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -8010897375413717246 in succeeded_hashes:  # avoid duplicate inserts
            instance = menu2 = Menu(title="About", parent_id=None, page_id=2)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-8010897375413717246)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -8988738206168921752 in succeeded_hashes:  # avoid duplicate inserts
            instance = menu3 = Menu(title="Services", parent_id=None, page_id=3)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-8988738206168921752)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 2324573397503379041 in succeeded_hashes:  # avoid duplicate inserts
            instance = menu4 = Menu(title="Contact", parent_id=None, page_id=4)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(2324573397503379041)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()
print('\n'.join(data_log))
with open(project_dir / 'database/test_data/test_data_code_log.txt', 'w') as log_file:
    log_file.write('\n'.join(data_log))
print('\n'.join(data_log))
