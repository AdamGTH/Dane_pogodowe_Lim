from flask import Flask
from flask import render_template
from markupsafe import escape
from dane_pogoda import weath_lim
import os

weather = weath_lim
humid = weath_lim["humidity"]

sta = ['jeden', 'dwa', 'trzy', 'cztery']

app = Flask(__name__)

blogposts = {1: "blogpost1", 2: "blogpost2"}

@app.route("/")
def hello_world():
    return render_template("index.html", data = weather)
   # return "<p>Hello, World!</p>"

@app.route("/test")
def another_hello():
    return render_template("blogpost.html", fo=sta)

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    foo = blogposts[post_id]
    return render_template("blogpost.html", foo = foo)

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, use_reloader=True)  