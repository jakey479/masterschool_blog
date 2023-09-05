from flask import Flask, render_template, request, redirect, url_for
from crud_json_blog_class import CrudJsonBlogFile
from utils import helpers
import os
import json

app = Flask(__name__, template_folder='templates', static_folder='static')
BLOG_POSTS_JSON_FILEPATH = os.path.join('data', 'blog_posts.json')
JSON_BLOG_HANDLER = CrudJsonBlogFile(
    json_filepath=BLOG_POSTS_JSON_FILEPATH
)


@app.route('/')
def return_blog_posts():
    try:
        blog_posts = JSON_BLOG_HANDLER.read_blog_posts()
    except json.decoder.JSONDecodeError as e:
        JSON_BLOG_HANDLER.initialize_blog_file()
        blog_posts = JSON_BLOG_HANDLER.read_blog_posts()
    return render_template(
        'display_blog_posts.html',
        blog_posts=blog_posts
    )


@app.route('/update_blog', methods=['GET', 'POST'])
def update_blog():
    blog_post_title = request.form['title']
    blog_post_author = request.form['author']
    blog_post_content = request.form['content']
    blog_post_timestamp = helpers.return_timestamp()
    blog_post = {"title": blog_post_title,
                 "author": blog_post_author,
                 "content": blog_post_content,
                 "timestamp": blog_post_timestamp
                 }
    JSON_BLOG_HANDLER.write_to_blog(
        blog_post=blog_post
    )
    return redirect(url_for('return_blog_posts'))


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
