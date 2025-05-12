from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import random

# Setup the driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.google.com/search?q=tic+tac+toe")

time.sleep(3)

# Optional: Click the start button or difficulty setting if required
# You can select Easy if not already set
try:
    easy_mode = driver.find_element(By.XPATH, "//div[text()='Easy']")
    easy_mode.click()
    time.sleep(1)
except:
    pass  # It's already in easy mode or no selection needed

# Select whether to play as X or O
your_symbol = input("Choose your symbol (X or O): ").strip().upper()
if your_symbol not in ['X', 'O']:
    print("Invalid input. Defaulting to X.")
    your_symbol = 'X'

# Select player
try:
    if your_symbol == 'X':
        driver.find_element(By.XPATH, "//div[text()='X']").click()
    else:
        driver.find_element(By.XPATH, "//div[text()='O']").click()
    time.sleep(1)
except:
    pass  # Already selected

# Find all cell buttons
def get_cells():
    return driver.find_elements(By.CSS_SELECTOR, "div[jsname='fXzQCc']")

# Wait for Google to make a move
def wait_for_opponent_move(prev_cells):
    timeout = 10
    for _ in range(timeout):
        current_cells = get_cells()
        current_texts = [cell.text for cell in current_cells]
        if current_texts != prev_cells:
            return current_texts
        time.sleep(1)
    return current_texts

# Get initial board state
cells = get_cells()
board_state = [cell.text for cell in cells]

# If playing second (O), wait for X to play first
if your_symbol == 'O':
    print("Waiting for Google (X) to play first...")
    board_state = wait_for_opponent_move(board_state)

# Find empty cell and click it
def make_move(board):
    empty_indexes = [i for i, v in enumerate(board) if v == '']
    if not empty_indexes:
        print("No moves left!")
        return
    move_index = random.choice(empty_indexes)
    get_cells()[move_index].click()
    print(f"Played at position {move_index}")
    return move_index

# Make your move
make_move(board_state)

# Optionally wait and observe further gameplay
time.sleep(10)
driver.quit()
