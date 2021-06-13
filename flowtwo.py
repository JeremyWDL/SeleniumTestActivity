from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
browser = webdriver.Firefox()

browser.get('https://practiceselenium.com')
button = browser.find_element_by_link_text("Let's Talk Tea")
button.click()

name = browser.find_element_by_name('name')
name.send_keys('Thomas Edison')
email = browser.find_element_by_name('email')
email.send_keys('test@testmail.xyz')
subject = browser.find_element_by_name('subject')
subject.send_keys('The quick brown fox jumped over the lazy dog.')
message = browser.find_element_by_name('message')
message.send_keys('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.')
submit = browser.find_elements_by_class_name('form-submit')
button.click()