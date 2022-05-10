import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
#Para menu dropdown
#para probar by cirley.
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import time
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
driver = webdriver.Chrome(executable_path = "drivers/chromedriver.exe")
driver.get("https://ais.usvisa-info.com/es-co/niv/users/sign_in")
user = driver.find_element(by=By.ID, value="user_email")
user.send_keys("jonathan13th@gmail.com")
contra = driver.find_element(by=By.ID, value="user_password")
contra.send_keys("Nirvana1994")
driver.find_element(by=By.CSS_SELECTOR, value="label[for='policy_confirmed']").click()
time.sleep(2)
driver.find_element(by=By.CLASS_NAME, value="button.primary").click()
time.sleep(2)
driver.find_element(by=By.CLASS_NAME, value="button.primary.small").click()
time.sleep(2)
driver.find_element(by=By.LINK_TEXT, value="Reprogramar cita").click()
time.sleep(2)
btn = '/html/body/div[4]/main/div[2]/div[2]/div/section/ul/li[4]/div/div/div[2]/p[2]/a'
driver.find_element(by=By.XPATH, value=btn).click()
time.sleep(2)
driver.refresh()
time.sleep(2)
driver.find_element(by=By.ID, value='appointments_consulate_appointment_date').click()
