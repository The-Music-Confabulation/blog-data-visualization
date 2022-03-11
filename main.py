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
import json
from data_generator import getURL_forYT
load_dotenv()

config = dotenv_values(".env")

username = config['USERNAME'] + '@' + config['DOMAIN']
password = config['PASSWORD']

print(username)
# Get data from mongodb server and export to JSon
getURL_forYT()
# Load data from JSon File
with open('collection.json', 'r') as myfile:
    data = myfile.read()
obj = json.loads(data)

chrome_driver_path = "/Users/ThanhNam/PycharmProjects/yt-manager/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.youtube.com/")
# print(password)
