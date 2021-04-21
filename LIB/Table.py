from LMS import app, db
from LMS.models import User,Post
db.create_all(app=app)
user_1=User(username='admin',email='admin@iitd.ac.in',password='password',pos='Admin')
db.session.add(user_1)
db.session.commit()
User.query.all()