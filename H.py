from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://example.com")


driver.implicitly_wait(10)


try:
    element = driver.find_element(By.TAG_NAME, "h1")
    print("Element found:", element.text)
except Exception as e:
    print("Element not found within 10 seconds:", e)

driver.quit()