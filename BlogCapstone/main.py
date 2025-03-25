from flask import Flask, render_template
import requests
from post import Post

blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
response = requests.get(url=blog_url)
all_posts = response.json()
posts = [Post(post["id"], post["title"], post["subtitle"], post["body"]) for post in all_posts]
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", posts=posts)

@app.route('/post/<int:num>')
def get_post(num):
    for blog_post in posts:
        requested_post = None
        if blog_post.id == num:
            requested_post = blog_post
        return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
