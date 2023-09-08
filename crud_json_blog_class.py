from utils.json_file_handler_class import JsonFileHandler
from utils import helpers


class CrudJsonBlogFile:
    def __init__(self, json_filepath: str):
        self.filepath = json_filepath

    def initialize_blog_file(self) -> None:
        json_array = []
        JsonFileHandler.write_python_object_to_json(
            json_filepath=self.filepath,
            python_object=json_array
        )

    def read_blog_posts(self) -> list[dict]:
        return JsonFileHandler.return_python_object_from_json(
            json_filepath=self.filepath
        )

    def write_to_blog(self, blog_post: dict, blog: list[dict]):
        blog.append(blog_post)
        JsonFileHandler.write_python_object_to_json(
            json_filepath=self.filepath,
            python_object=blog
        )

    def update_blog_post(self, post_id: str, new_blog_post_content: str, blog: list[dict]):
        for blog_post in blog:
            if blog_post["id"] == post_id:
                blog_post["content"] = new_blog_post_content
                JsonFileHandler.write_python_object_to_json(
                    json_filepath=self.filepath,
                    python_object=blog
                )

    def delete_from_blog(self, post_id: str, blog: list[dict]) -> None:
        for index_position, blog_post in enumerate(blog):
            if blog_post["id"] == post_id:
                blog.pop(index_position)
                break
        JsonFileHandler.write_python_object_to_json(
            json_filepath=self.filepath,
            python_object=blog
        )
