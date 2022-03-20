from dotenv import dotenv_values
import pymongo
import os
from dotenv import load_dotenv
from bson.json_util import dumps
import time
import certifi
import json

load_dotenv()

ca = certifi.where()
config = dotenv_values(".env")
client = pymongo.MongoClient(f"mongodb+srv://" + config['SERVER_USR'] + ":" + config['SERVER_PWD'] +
                             "@cluster0.1wmqh.mongodb.net/blog_content"
                             "?retryWrites=true&w=majority", tlsCAFile=ca)
db = client.blog_content

# Set up Post data extractions
Post = db['posts']
postSchema = Post.find({}, {'_id': 0, 'approved': 0, '__v':0})
list_cur = list(postSchema)
json_data = dumps(list_cur, indent=4)

print("Working on Post Schema")
if os.path.exists("post.json"):
    print("Remove old and create new Json file")
    # Delete old json
    os.remove("post.json")

    # Export new Json,
    with open('post.json', 'w') as file:
        file.write(json_data)
    time.sleep(10)

else:
    # create new data.json file
    print("Data does not exist. Create new Json file")
    with open('post.json', 'w') as file:
        file.write(json_data)
    time.sleep(10)

print("Finish Post Schema")

# Set up User data extractions
Users = db['users']
userSchema = Users.find({}, {'_id':0, 'email':0, 'info':0, 'fullname':0, 'salt':0, 'hash':0, '__v':0})
list_cur = list(userSchema)
json_data = dumps(list_cur, indent=4)


print("Working on user Schema")
if os.path.exists("user.json"):
    print("Remove old and create new Json file")
    # Delete old json
    os.remove("user.json")

    # Export new Json,
    with open('user.json', 'w') as file:
        file.write(json_data)
    time.sleep(10)

else:
    # create new data.json file
    print("Data does not exist. Create new Json file")
    with open('user.json', 'w') as file:
        file.write(json_data)
    time.sleep(10)

print("Finish User Schema")

