from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
import os
app = Flask(__name__)
CSRFProtect(app)
app.config.update(DEBUG=True, WTF_CSRF_ENABLED=True,SECRET_KEY=os.urandom(32),UPLOAD_FOLDER='/Uploads',SQLALCHEMY_DATABASE_URI='sqlite:///site.db',FILE_TYPES=['txt','doc','docx','odt','pdf','rtf','text','wks','wpd'])
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from LMS import routes