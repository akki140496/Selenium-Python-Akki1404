from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get("https://poki.com/en/g/tic-tac-toe-3")

driver.maximize_window()
time.sleep(10)  # Allow iframe and game to fully load

# Switch to iframe first
iframe = driver.find_element(By.CSS_SELECTOR, "iframe#game-element")
driver.switch_to.frame(iframe)

# Locate the canvas
canvas = driver.find_element(By.CSS_SELECTOR, "canvas.ani_hack")

# Get canvas position and size
canvas_location = canvas.location
canvas_size = canvas.size

print("Canvas location:", canvas_location)
print("Canvas size:", canvas_size)

# Let's say we want to click the center cell of the 3x3 grid
canvas_width = canvas_size['width']
canvas_height = canvas_size['height']

# Compute coordinates for the center cell
cell_x = canvas_width // 3
cell_y = canvas_height // 3

# Move to the cell and click
actions = ActionChains(driver)
actions.move_to_element_with_offset(canvas, cell_x, cell_y).click().perform()

time.sleep(3)
driver.quit()
