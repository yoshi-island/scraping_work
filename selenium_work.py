from selenium import webdriver
from time import sleep
browser = webdriver.Chrome()
browser.get('http://google.com')
sleep(10)
browser.close()
