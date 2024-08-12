from app import db, User

user4 = User("konton@mimic.com", "Konton User", "konton")
db.session.add(user4)
db.session.commit() #DBにデータを追加

# 全レコードの取得
all_users = User.query.all()
print(all_users)

# レコードの取得（ID指定）
userid_1 = User.query.get(1)
print(userid_1.username)

# レコードの取得
username_user2 = User.query.filter_by(username="Hitokui User")
print(username_user2.all())

# レコードの更新
userid_1 = User.query.get(1)
userid_1.username = "MimicBs User"
db.session.add(userid_1)
db.session.commit()

# レコードの削除
userid_2 = User.query.get(2)
db.session.delete(userid_2)
db.session.commit()

# 全レコードの取得
all_users = User.query.all()
print(all_users)