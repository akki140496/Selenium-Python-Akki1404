from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
import time
import random

# Setup the driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.google.com/")

time.sleep(5)

google_search_xpath = "//textarea[@name='q']"


driver.implicitly_wait(30)
Tic_Tac_Toe = driver.find_element(By.XPATH,google_search_xpath)
Tic_Tac_Toe.send_keys("Tic Tac Toe")
driver.implicitly_wait(30)
actions = ActionChains(driver)
actions.send_keys(Keys.ENTER).perform()
time.sleep(10)

