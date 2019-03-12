import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome('/home/kishan/Downloads/chromedriver')

driver.get("http://www.opcito.com")
elem = driver.find_element_by_id("nav-menu-item-26")
elem.click()
elem=driver.find_element_by_name("fname").send_keys("kishan")
elem=driver.find_element_by_name("emailid").send_keys("kishan.tiwari@opcito.com")
elem=driver.find_element_by_name("contact-number").send_keys("8095888475")
elem=driver.find_element_by_name("company").send_keys("Opcito Technology")
elem=driver.find_element_by_name("your-message").send_keys("Testing selenium practice")

time.sleep(20)
elem=driver.find_element_by_id("contact-btn").click()

