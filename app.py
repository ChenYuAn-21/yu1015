from flask import Flask, render_template

app = Flask(__name__)

# 假資料：部落格文章
posts = [
    {
        'id': 1,
        'title': '第一篇文章',
        'author': '小明',
        'content': '這是我的第一篇部落格文章，歡迎留言！'
    },
    {
        'id': 2,
        'title': '第二篇文章',
        'author': '小美',
        'content': '今天分享一下我學 Flask 的心得。'
    }
]

# 首頁：列出所有文章
@app.route('/')
def index():
    return render_template('index.html', posts=posts)

# 單篇文章頁面（根據文章 id 顯示）
@app.route('/post/<int:post_id>')
def post(post_id):
    post = next((p for p in posts if p['id'] == post_id), None)
    if not post:
        return "找不到文章", 404
    return render_template('post.html', post=post)

if __name__ == '__main__':
    app.run(debug=True)
