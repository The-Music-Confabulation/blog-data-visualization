from dotenv import load_dotenv
from dotenv import dotenv_values
import pymongo
import os
from pymongo import MongoClient
import pprint
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
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
from data_generator import getURL
load_dotenv()

# Get data from mongodb server and export to JSon
# urls = getURL()
urls = 'BUrv5IhE3Og'
if urls is None:
    # There is nothing to add
    pass
else:
    config = dotenv_values(".env")
    username = config['USERNAME'] + '@' + config['DOMAIN']
    password = config['PASSWORD']

    print(urls)
    print(username)
    print(password)

    ser = Service("/Users/ThanhNam/PycharmProjects/yt-manager/chromedriver.exe")
    op = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=ser, options=op)

    driver.get("https://www.youtube.com/")



    #driver.close()
