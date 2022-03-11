from dotenv import load_dotenv
from dotenv import dotenv_values
import pymongo
import os
from pymongo import MongoClient
import pprint
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import os
from dotenv import load_dotenv
from bson.json_util import dumps
import time
import certifi
import json
load_dotenv()


url_list = []


def getURL():
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

        old_num = len(obj)
        print(obj)
        # Delete old json
        print("Delete and create new json")
        os.remove("collection.json")

        # Export new Json,
        with open('collection.json', 'w') as file:
            file.write(dumps(cursor))

        time.sleep(5)

        # Read new Json data,
        with open('collection.json', 'r') as myfile:
            data = myfile.read()
        obj = json.loads(data)
        print(obj)
        # This is the current number of posts
        new_num = len(obj)

        if old_num == new_num:
            return None
        else:
            # 0 1
            # 0 1 2 3
            # get element at 2 3
            print("Getting the url \n")
            for i in range(old_num, new_num):
                url_list.append(str(obj[i]['url']))  # this is the url

            print(url_list)
            print("Done \n")
            return url_list
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

        for i in range(len(obj)):
            url_list.append(str(obj[i]['url']))
        return url_list

