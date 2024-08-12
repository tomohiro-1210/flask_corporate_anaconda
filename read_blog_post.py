from app import db, User, BlogPost

# blog_postsのデータをすべて取得する
all_posts = BlogPost.query.all()
print(all_posts)


