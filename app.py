import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime
from pytz import timezone

app = Flask(__name__)


# シークレットキーの設定
app.config['SECRET_KEY'] = 'hoshitetsukey'

# DBの設定
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)

#Foreign Key（外部キー）の設定？
from sqlalchemy.engine import Engine
from sqlalchemy import event

@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()

# テーブルの設定
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    administrator = db.Column(db.String(1))
    # リレーションシップの設定（lazy='dynamic'で1対多の設定になっている）
    post = db.relationship('BlogPost', backref='author', lazy='dynamic')

    def __init__(self, email, username, password_hash, administrator):
        self.email = email
        self.username = username
        self.password_hash = password_hash
        self.administrator = administrator

    def __repr__(self):
        return f"Username: {self.username}"
    
# ブログ投稿のDBモデル
class BlogPost(db.Model):
    __tableame__ = 'blog_post'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    # ForeignKey('users.id)はUsersテーブルのidと紐づけする設定
    date = db.Column(db.DateTime, default=datetime.now(timezone('Asia/Tokyo')))
    title = db.Column(db.String(140))
    text = db.Column(db.Text)
    summary = db.Column(db.String(140))
    thumbnail = db.Column(db.String(140))

    def __init__(self, title, text, thumbnail, user_id, summary):
        self.title = title 
        self.text = text
        self.thumbnail = thumbnail
        self.user_id = user_id
        self.summary = summary

    def __repr__(self):
        return f"PostId:{self.id}, Title:{self.title}, Author: {self.author} \n"
    
if __name__ == '__main__':
    app.run(debug=True)