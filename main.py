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

load_dotenv()
import certifi

ca = certifi.where()

config = dotenv_values(".env")

client = pymongo.MongoClient(f"mongodb+srv://" + config['SERVER_USR'] + ":" + config['SERVER_PWD'] +
                             "@cluster0.1wmqh.mongodb.net/blog_content"
                             "?retryWrites=true&w=majority", tlsCAFile=ca)

db = client.blog_content
collection = db['posts']

pprint.pprint(collection.find_one())

username = config['USERNAME'] + '@' + config['DOMAIN']
password = config['PASSWORD']

print(username)

chrome_driver_path = "/Users/ThanhNam/PycharmProjects/yt-manager/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.youtube.com/")
# print(password)
