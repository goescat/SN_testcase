# coding=UTF-8

###
# This code for autoinput and submit serial number to some site
# Using Selenium + Chrome Webdriver + python
###

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

import time
import os

browser = webdriver.Chrome('/home/user/dir/chromedriver') #Webdriver Dir
browser.get('Link') #Site Link

## Login ##
elem = browser.find_element_by_id("email ID")
elem.send_keys("Your ID")

elem = browser.find_element_by_id("pass ID")
elem.send_keys("Your PW")

elem.submit()

## get serial numbers file ##
## serial numbers file mustbe one line for one number##
file = open('serialtxt','r')
howtime = 0

for line in file.readlines():
    howtime = howtime+1
    print(howtime)
    code = line

    ## Close Alert ##
    try:
        alert = browser.switch_to_alert()
        print (alert.text)
        alert.accept()
    except:
        print ("no alert to accept")

    time.sleep(2)
## select ##
    select = Select(browser.find_element_by_id('List ID'))
    select.select_by_value("Select Value")
    browser.find_element_by_id("List ID").clear()
    browser.find_element_by_id("List ID").send_keys(code)
    browser.find_element_by_css_selector('.btn_blue').click() #click button to submit
    ## Close Alert ##
    try:
        alert = browser.switch_to_alert()
        print (alert.text)
        alert.accept()
    except:
        print ("no alert to accept")
    ## Wait to site loading element##
    time.sleep(1)

browser.close()
