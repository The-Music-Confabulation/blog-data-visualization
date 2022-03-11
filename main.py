from dotenv import load_dotenv
from dotenv import dotenv_values
import pymongo
import os
from pymongo import MongoClient
import pprint
import certifi
ca = certifi.where()


load_dotenv()
config = dotenv_values(".env")

client = pymongo.MongoClient(f"mongodb+srv://"+ os.environ.get('SERVER_USR')+":"+os.environ.get('SERVER_PWD')+
                             "@cluster0.1wmqh.mongodb.net/blog_content"
                             "?retryWrites=true&w=majority", tlsCAFile=ca)

db = client.blog_content
collection = db['posts']


pprint.pprint(collection.find_one())



# pprint.pprint(posts.find_one())