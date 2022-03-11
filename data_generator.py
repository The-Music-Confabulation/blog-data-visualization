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
load_dotenv()
import certifi
import json
ca = certifi.where()

config = dotenv_values(".env")

client = pymongo.MongoClient(f"mongodb+srv://" + config['SERVER_USR'] + ":" + config['SERVER_PWD'] +
                             "@cluster0.1wmqh.mongodb.net/blog_content"
                             "?retryWrites=true&w=majority", tlsCAFile=ca)

db = client.blog_content
collection = db['posts']

cursor = collection.find({})
with open('collection.json', 'w') as file:
    file.write(dumps(cursor))


with open('collection.json', 'r') as myfile:
    data=myfile.read()

obj = json.loads(data)


