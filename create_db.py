from app import app
from models import db, User

with app.app_context():
    db.create_all()
    
    
    user = User.query.filter_by(username='admin').first()
    if not user:
        user = User(username='admin', password='password')
        db.session.add(user)
        db.session.commit()
    else:
        print("User 'admin' already exists.")
