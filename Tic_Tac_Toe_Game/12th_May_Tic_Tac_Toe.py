# Usefull libraries Needed to Automate
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Set up the driver


# Imp Xpath for Tic - Tac - Toe
# Square_top_left_Xpath = "//div[@class='square top left']"
# Square_top_Xpath = "div[@class='square top']"
# Square_top_right_Xpath = "div[@class='square top right']"
# Square_left_Xpath = "div[@class='square left']"
# Square_Xpath = "div[@class='square']"
# Square_right_Xpath = "div[@class='square right']"
# Square_bottom_left_Xpath = "div[@class='square bottom left']"
# Square_bottom_Xpath = "div[@class='square bottom']"
# Square_bottom_right_Xpath = "div[@class='square bottom']"


Square_top_left_Xpath = "//div[@class='square top left']"
Square_top_Xpath = "//div[@class='square top']"
Square_top_right_Xpath = "//div[@class='square top right']"
Square_left_Xpath = "//div[@class='square left']"
Square_Xpath = "//div[@class='square']"
Square_right_Xpath = "//div[@class='square right']"
Square_bottom_left_Xpath = "//div[@class='square bottom left']"
Square_bottom_Xpath = "//div[@class='square bottom']"
Square_bottom_right_Xpath = "//div[@class='square bottom right']"


## imp things #################

square_xpaths = [
    Square_top_left_Xpath,
    Square_top_Xpath,
    Square_top_right_Xpath,
    Square_left_Xpath,
    Square_Xpath,
    Square_right_Xpath,
    Square_bottom_left_Xpath,
    Square_bottom_Xpath,
    Square_bottom_right_Xpath
]

def play_random_move(driver):
    remaining_xpaths = []

    for xpath in square_xpaths:
        try:
            # Check for child 'x' or 'o'
            child_x = driver.find_element(By.XPATH, f"{xpath}//div[@class='x']")
            child_o = driver.find_element(By.XPATH, f"{xpath}//div[@class='o']")
            # If any found, continue to next
            continue
        except NoSuchElementException:
            remaining_xpaths.append(xpath)

    if remaining_xpaths:
        chosen_xpath = random.choice(remaining_xpaths)
        driver.find_element(By.XPATH, chosen_xpath).click()
        print(f"Clicked: {chosen_xpath}")
    else:
        print("All squares are filled.")


def check_winner(driver):
    board_state = []

    for xpath in square_xpaths:
        try:
            driver.find_element(By.XPATH, f"{xpath}//div[@class='x']")
            board_state.append('x')
        except NoSuchElementException:
            try:
                driver.find_element(By.XPATH, f"{xpath}//div[@class='o']")
                board_state.append('o')
            except NoSuchElementException:
                board_state.append('')  # empty

    # Define all 8 winning combinations (by index)
    win_combinations = [
        [0, 1, 2],  # top row
        [3, 4, 5],  # middle row
        [6, 7, 8],  # bottom row
        [0, 3, 6],  # left column
        [1, 4, 7],  # center column
        [2, 5, 8],  # right column
        [0, 4, 8],  # top-left to bottom-right diagonal
        [2, 4, 6]   # top-right to bottom-left diagonal
    ]

    for combo in win_combinations:
        first = board_state[combo[0]]
        if first and all(board_state[i] == first for i in combo):
            print(f"{first.upper()} wins!")
            return f"{first} wins"

    # Check for draw
    if all(cell != '' for cell in board_state):
        print("It's a draw!")
        return "draw"

    return None  # No winner yet


if __name__=="__main__":
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("http://playtictactoe.org/")
    print("New screen launched ")

    time.sleep(5)
    #
    # p2_element = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.XPATH, "//div[@class='swap']/p[@class='p2']"))
    # )
    # p2_text = p2_element.text.strip()
    #
    # if p2_text == "2P":
    #     swap_button = driver.find_element(By.XPATH, "//div[@class='swap']")
    #     swap_button.click()
    #     print("Clicked to switch from 2P to 1P")
    # else:
    #     print("Already in 1P mode")
    random_button_X = random.choice(square_xpaths)
    print(random_button_X)
    print("randome x path is choosed ")
    driver.find_element(By.XPATH,random_button_X).click()
    print("randome x path is clicked ")

    time.sleep(2)
    while True:
        result = check_winner(driver)
        if result:
            print(f"Game Over: {result}")
            break
        play_random_move(driver)
        time.sleep(2)
