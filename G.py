from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://example.com")

# 1. IMPLICIT WAIT - waits for element to appear (global)
driver.implicitly_wait(10) # waits max 10 sec for any element

# 2. EXPLICIT WAIT - waits for specific condition (best)
wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.ID, "myButton")))
element.click()

# Common explicit conditions:
# presence_of_element_located
# visibility_of_element_located
# element_to_be_clickable
# title_contains

# FLUENT WAIT - with polling and ignoring exceptions (advanced explicit)
wait2 = WebDriverWait(driver, 10, poll_frequency=1, ignored_exceptions=[Exception])
btn = wait2.until(EC.presence_of_element_located((By.XPATH, "//button")))

# 4. Thread.sleep

driver.quit()