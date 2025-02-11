from user import User
from post import Post

app_user_one = User("admin@mail.com", "admin", "admin", "DevOps engineer")
app_user_one.get_user_info()

app_user_one.change_job_title("senior engineer")
app_user_one.get_user_info()


app_user_two = User("dheeraj@mail.com", "dheeraj", "passw", "Devops Engineer")
app_user_two.get_user_info()


new_post = Post("This is my 1st class", "admin")
new_post.get_post_info()