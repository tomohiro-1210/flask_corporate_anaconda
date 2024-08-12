from app import db, User
from werkzeug.security import check_password_hash, generate_password_hash

# db.drop_all()
db.create_all()

pw = "12345"
pw_hash = generate_password_hash(pw)

user1 = User(email="admin_user@test.com", username="Admin User1", password_hash=pw_hash, administrator="1")
db.session.add(user1)
db.session.commit()