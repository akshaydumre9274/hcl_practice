from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/login")

element = driver.find_element(By.XPATH, '//*[@id="username"]')

print(element.get_attribute("id"))

driver.quit()

#555997885555//*/-*/877787\\[]{[]}|545487878963078987987///////*77779