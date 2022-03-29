from selenium import webdriver                                    #(1)
from selenium.webdriver.common.keys import Keys   #(2)

browser = webdriver.Chrome()                                       #(3)
browser.get('http://localhost:8000')                               #(4)

assert 'install' in browser.title                                       #(5)