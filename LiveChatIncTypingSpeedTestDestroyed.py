# The script opens Live Chat Inc Typing Speed Test and completes its typing test all by itself destroying it in 50 seconds.
# The script is able to score a speed of 507 WPM (2259 CPM) with an accuracy of 100%.
# The typing test goes out of words and the script is idle for the last 10-12 seconds of the total 60 seconds because of the scarcity of words. LOL.

import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from time import sleep
import time

driver = webdriver.Chrome('C:/Users/Muktadir Khan/Downloads/chromedriver.exe')

driver.get('https://www.livechatinc.com/typing-speed-test/#/')
time.sleep(5)

clickitem = driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div/span/div[2]/span/div/div[2]/div/span[1]')
clickitem.click()

times=0
while times<=50:
    html = driver.page_source
    soup = bs(html,'lxml')

    for word in soup.find_all('span',class_='test-word undefined'):
        print(word.text)
        actions = ActionChains(driver)
        actions.send_keys(word.text+' ')
        actions.perform()
    times+=1
