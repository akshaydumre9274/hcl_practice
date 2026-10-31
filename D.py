from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/login")

username = driver.find_element(By.ID, "username")

username.send_keys("tomsmith")

print("Username entered successfully!")

driver.quit()

