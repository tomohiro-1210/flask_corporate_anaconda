import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


# シークレットキーの設定
app.config['SECRET_KEY'] = 'hoshitetsukey'

# DBの設定
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# テーブルの設定
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))

    def __init__(self, email, username, password_hash):
        self.email = email
        self.username = username
        self.password_hash = password_hash

    def __repr__(self):
        return f"Username: {self.username}"
    
if __name__ == '__main__':
    app.run(debug=True)