from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

#initialization db
db = SQLAlchemy()
bcrypt = Bcrypt()