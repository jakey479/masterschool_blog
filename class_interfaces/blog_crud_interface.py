from typing import Protocol


# as long as subclasses adhere to protocol contract, subclasses can have different implementations
# and can be referred to by protocol class instead
class CrudBlogFile(Protocol):
    def initialize_blog_file(self):
        ...

    def read_blog_posts(self):
        ...

    def write_to_blog(self):
        ...

    def update_blog(self):
        ...

    def delete_from_blog(self):
        ...
