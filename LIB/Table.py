from LMS import app, db, bcrypt
from LMS.models import User,Post
db.create_all(app=app)
user_1=User(username='admin',email='admin@iitd.ac.in',password=bcrypt.generate_password_hash('password').decode('utf-8'),pos='Admin')
db.session.add(user_1)
db.session.commit()
