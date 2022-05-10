import logging
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
driver = webdriver.Chrome(executable_path = "drivers/chromedriver.exe")
driver.get("http://www.google.com")
assert "Google" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("Greensill News")
elem.send_keys(Keys.RETURN)
button = driver.find_element_by_css_selector(".TbwUpd.NJjxre").click()
time.sleep(5)
driver.close()

