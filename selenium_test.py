from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

def test_home():
	options = Options()
	options.add_argument("--no-sandbox")
	options.add_argument("--headless")
	driver = webdriver.Chrome(chrome_options=options)
	driver.get("http://162.246.157.110:8000/")
	
	assert driver.find_element_by_id("name") != None
	assert driver.find_element_by_id("about") != None
	assert driver.find_element_by_id("education") != None
	assert driver.find_element_by_id("skills") != None
	assert driver.find_element_by_id("work") != None
	assert driver.find_element_by_id("contact") != None

test_home()