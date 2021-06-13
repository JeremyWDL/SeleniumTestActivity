from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import csv
browser = webdriver.Firefox()

browser.get('https://practiceselenium.com')
image = browser.find_element_by_id('wsb-element-00000000-0000-0000-0000-000450914916')
print ("This website logo exists")
link = browser.find_element_by_link_text('Welcome')
print ("This link exists")
link = browser.find_element_by_link_text('Our Passion')
print ("This link exists")
link = browser.find_element_by_link_text('Menu')
print ("This link exists")
link = browser.find_element_by_link_text("Let's Talk Tea")
print ("This link exists")
link = browser.find_element_by_link_text('Check Out')
print ("This link exists")
