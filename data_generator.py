from dotenv import dotenv_values
import pymongo
import os
from pymongo import MongoClient
import os
from dotenv import load_dotenv
from bson.json_util import dumps
import time
import certifi
import json

load_dotenv()


def getData():
    ca = certifi.where()
    config = dotenv_values(".env")
    client = pymongo.MongoClient(f"mongodb+srv://" + config['SERVER_USR'] + ":" + config['SERVER_PWD'] +
                                 "@cluster0.1wmqh.mongodb.net/blog_content"
                                 "?retryWrites=true&w=majority", tlsCAFile=ca)
    db = client.blog_content
    collection = db['posts']
    cursor = collection.find({})

    if os.path.exists("collection.json"):
        # if file exists, read and extract length
        with open('collection.json', 'r') as myfile:
            data = myfile.read()
        obj = json.loads(data)

        # Delete old json
        os.remove("collection.json")

        # Export new Json,
        with open('collection.json', 'w') as file:
            file.write(dumps(cursor))

        time.sleep(5)
        # Read new Json data,
        with open('collection.json', 'r') as myfile:
            data = myfile.read()
        obj = json.loads(data)

        return obj
    else:
        # create new data.json file
        print("Data does not exist. Create new Json file")
        with open('collection.json', 'w') as file:
            file.write(dumps(cursor))

        time.sleep(5)

        # Read new Json data,
        with open('collection.json', 'r') as myfile:
            data = myfile.read()
        obj = json.loads(data)

        return obj
