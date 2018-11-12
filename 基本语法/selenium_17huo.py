# -*- coding：utf-8-*-
import time
from selenium import webdriver

browser = webdriver.Chrome()

#有多少页商品
browser.get("http://www.17huo.com/newsearch/?k=%E5%A4%A7%E8%A1%A3")
page_info = browser.find_element_by_css_selector('body > div.wrap > div.search_container > div.main_new > div.tcdPageCode.goldPage')
print (page_info)