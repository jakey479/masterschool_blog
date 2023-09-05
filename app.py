from flask import Flask, render_template
from json_file_handler_class import JsonFileHandler
import os
import json

app = Flask(__name__, template_folder='templates', static_folder='static')
BLOG_POSTS_FILEPATH = os.path.join('data', 'blog_posts.json')
# initialize an empty json array to a json file if it is empty or contains invalid json
try:
    BLOG_POSTS = JsonFileHandler.return_python_object_from_json(
        filepath=BLOG_POSTS_FILEPATH
    )
except json.decoder.JSONDecodeError as e:
    BLOG_POSTS = []
    JsonFileHandler.write_python_object_to_json(
        python_object=BLOG_POSTS,
        filepath=BLOG_POSTS_FILEPATH
    )


@app.route('/')
def return_blog_posts():
    return render_template(
        'display_blog_posts.html',
        blog_posts=BLOG_POSTS
    )


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
