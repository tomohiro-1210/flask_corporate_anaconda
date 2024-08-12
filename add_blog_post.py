from app import db, BlogPost

# def __init__(self, title, text, thumbnail, user_id, summary)のselfを除いた内容を定義していく
# blog_post1 = BlogPost("Mimic Growth", 
#                       "今日もミミックのレベルが１００上がった。スキルもすべてマスターしたようだ", 
#                       "Mimic.png", 1, "Summary1")
# blog_post2 = BlogPost("Pandora Growth", 
#                       "今日はパンドラボックスを育ててみた。ザラキをレベル１で習得したのはビビる。", 
#                       "Pandora.png", 3, "Summary2")
# blog_post3 = BlogPost("Konton Growth", 
#                       "混沌の箱なんて初めて見た。これからどんな育ち方をしてくのだろうか？？", 
#                       "Konton.png", 1, "Summary3")
# blog_post4 = BlogPost("Hitokui Growth", 
#                       "ひとくいばこ。ドラクエ３では驚異的な攻撃力にトラウマになったユーザーも多かろう。", 
#                       "Hitokui.png", 4, "Summary4")
blog_post5 = BlogPost("Mimic Growth2", 
                      "ミミックは対戦環境に出ていったみたいだ。結果は・・・・わからない。", 
                      "Hitokui.png", 1, "Summary1")

# db.session.add_all([blog_post1, blog_post2, blog_post3])
# db.session.add(blog_post4)
db.session.add(blog_post5)
db.session.commit()