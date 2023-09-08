from flask import Flask, render_template, request, redirect, url_for
from crud_json_blog_class import CrudJsonBlogFile
from utils import helpers
import os
import json
from uuid import uuid4

app = Flask(__name__, template_folder='templates', static_folder='static')
BLOG_POSTS_JSON_FILEPATH = os.path.join('data', 'blog_posts.json')
JSON_BLOG_HANDLER = CrudJsonBlogFile(
    json_filepath=BLOG_POSTS_JSON_FILEPATH
)
BLOG = JSON_BLOG_HANDLER.read_blog_posts()


@app.route('/')
def homepage():
    try:
        blog_posts = JSON_BLOG_HANDLER.read_blog_posts()
    except json.decoder.JSONDecodeError:
        JSON_BLOG_HANDLER.initialize_blog_file()
        blog_posts = JSON_BLOG_HANDLER.read_blog_posts()
    return render_template(
        'display_homepage.html',
        blog_posts=blog_posts
    )


@app.route('/add_blog_post', methods=['GET', 'POST'])
def add_blog_post():
    blog_post_title = request.form['title']
    blog_post_author = request.form['author']
    blog_post_content = request.form['content']
    blog_post_timestamp = helpers.return_timestamp()
    blog_post_id = uuid4()
    blog_post = {"title": blog_post_title,
                 "author": blog_post_author,
                 "content": blog_post_content,
                 "timestamp": blog_post_timestamp,
                 "id": f"{blog_post_id}"
                 }
    JSON_BLOG_HANDLER.write_to_blog(
        blog_post=blog_post,
        blog=BLOG
    )
    return redirect(url_for('homepage'))


@app.route('/delete_blog_post/<post_id>', methods=['GET', 'POST'])
def delete_blog_post(post_id: str):
    JSON_BLOG_HANDLER.delete_from_blog(
        post_id=post_id,
        blog=BLOG
    )
    return redirect(url_for('homepage'))


@app.route('/update_blog_post/<post_id>', methods=['GET', 'POST'])
def update_blog_post(post_id):
    updated_blog_post_content = request.form.get("updated_blog_post_content")
    JSON_BLOG_HANDLER.update_blog_post(
        post_id=post_id,
        blog=BLOG,
        new_blog_post_content=updated_blog_post_content
    )
    return redirect(url_for('homepage'))


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
