from user import User
from post import Post



app_user_one = User("nwekemichael53@gmail.com", "Michael Chijioke Nweke", "Badboy123", "Webapp Dev")
app_user_one.get_user_info()

new_post = Post("We are getting better", app_user_one.name)
new_post.get_post_info()
