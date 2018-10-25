from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def test_home():
	driver = webdriver.Chrome()
	driver.get("http://162.246.157.110:8000/")
	assert driver.find_element_by_id("name") != None
	assert driver.find_element_by_id("about") != None
	assert driver.find_element_by_id("education") != None
	assert driver.find_element_by_id("skills") != None
	assert driver.find_element_by_id("work") != None
	assert driver.find_element_by_id("contact") != None

test_home()