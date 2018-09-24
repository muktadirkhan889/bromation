from selenium import webdriver
from time import sleep
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#path to your Chrome webdriver if using Chrome
driver = webdriver.Chrome('C:/Users/Muktadir Khan/Downloads/chromedriver.exe')

driver.get('https://mail.google.com')
email = driver.find_element_by_id('identifierId')
email.send_keys('your email goes here')

next_button = driver.find_element(By.XPATH,'//*[@id="identifierNext"]/content/span')
next_button.click()

time.sleep(2)
password = driver.find_element_by_name('password')
password.send_keys('your password goes here')

signin_button = driver.find_element(By.XPATH,'//*[@id="passwordNext"]/content/span')
signin_button.click()
