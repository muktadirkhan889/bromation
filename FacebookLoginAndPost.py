from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException
import time

driver = webdriver.Chrome('C:/Users/Muktadir Khan/Downloads/chromedriver.exe')

# driver.get('https://www.facebook.com/')
driver.get('https://www.facebook.com/login.php?login_attempt=1&lwv=110')
print("Opened Facebook")
email = driver.find_element_by_xpath("//input[@id='email' or @name='email']")

email.send_keys('your email goes here')
print("Email entered")

password = driver.find_element_by_xpath("//input[@id='pass']")
password.send_keys('your password goes here')
print("Password entered")

button = driver.find_element_by_xpath("//button[@id='loginbutton']")
button.click()

status= driver.find_element_by_xpath("//textarea[@name='xhpc_message']")
status.send_keys("Hello from Python");

#You need to click on the Share button manually after this

