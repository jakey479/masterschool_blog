from utils.json_file_handler_class import JsonFileHandler


class CrudJsonBlogFile:
    def __init__(self, json_filepath: str):
        self.filepath = json_filepath

    def initialize_blog_file(self):
        json_array = []
        JsonFileHandler.write_python_object_to_json(
            json_filepath=self.filepath,
            python_object=json_array
        )

    def read_blog_posts(self) -> list[dict]:
        return JsonFileHandler.return_python_object_from_json(
            json_filepath=self.filepath
        )

    def write_to_blog(self, blog_post: dict):
        blog = JsonFileHandler.return_python_object_from_json(
            json_filepath=self.filepath
        )
        blog.append(blog_post)
        JsonFileHandler.write_python_object_to_json(
            json_filepath=self.filepath,
            python_object=blog
        )

    def update_blog(self):
        pass

    def delete_from_blog(self):
        pass
