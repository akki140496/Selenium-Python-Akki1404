from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import cv2
import numpy as np
from PIL import Image

# Setup driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://poki.com/en/g/tic-tac-toe-3")
driver.maximize_window()
time.sleep(10)

# Switch to iframe
iframe = driver.find_element(By.CSS_SELECTOR, "iframe#game-element")
driver.switch_to.frame(iframe)

# Click "1 Player" button
one_player_button = driver.find_element(By.XPATH, "//canvas")
ActionChains(driver).move_to_element_with_offset(one_player_button, 210, 500).click().perform()
time.sleep(3)

def take_canvas_screenshot(driver):
    canvas = driver.find_element(By.XPATH, "//canvas")
    location = canvas.location
    size = canvas.size
    driver.save_screenshot("full_screen.png")

    image = Image.open("full_screen.png")
    left = location['x']
    top = location['y']
    right = left + size['width']
    bottom = top + size['height']

    image = image.crop((left, top, right, bottom))
    image.save("canvas_screenshot.png")

def detect_board_state():
    board = [["" for _ in range(3)] for _ in range(3)]
    canvas = cv2.imread("canvas_screenshot.png")
    x_template = cv2.imread("x_piece.png", 0)
    o_template = cv2.imread("o_piece.png", 0)
    canvas_gray = cv2.cvtColor(canvas, cv2.COLOR_BGR2GRAY)

    for i in range(3):
        for j in range(3):
            x, y = j * 150 + 30, i * 150 + 30
            roi = canvas_gray[y:y+90, x:x+90]

            res_x = cv2.matchTemplate(roi, x_template, cv2.TM_CCOEFF_NORMED)
            res_o = cv2.matchTemplate(roi, o_template, cv2.TM_CCOEFF_NORMED)

            if res_x.max() > 0.7:
                board[i][j] = "X"
            elif res_o.max() > 0.7:
                board[i][j] = "O"
    return board

def get_available_moves(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ""]

def make_move_on_canvas(driver, i, j):
    canvas = driver.find_element(By.XPATH, "//canvas")
    x = j * 150 + 75
    y = i * 150 + 75
    ActionChains(driver).move_to_element_with_offset(canvas, x, y).click().perform()
    time.sleep(2)

def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != "":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != "":
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != "":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != "":
        return board[0][2]
    return None

def minimax(board, depth, is_max):
    winner = check_winner(board)
    if winner == "X":
        return 10 - depth
    elif winner == "O":
        return depth - 10
    elif not get_available_moves(board):
        return 0

    if is_max:
        best = -float("inf")
        for i, j in get_available_moves(board):
            board[i][j] = "X"
            best = max(best, minimax(board, depth + 1, False))
            board[i][j] = ""
        return best
    else:
        best = float("inf")
        for i, j in get_available_moves(board):
            board[i][j] = "O"
            best = min(best, minimax(board, depth + 1, True))
            board[i][j] = ""
        return best

def best_move(board):
    best_val = -float("inf")
    move = (-1, -1)
    for i, j in get_available_moves(board):
        board[i][j] = "X"
        move_val = minimax(board, 0, False)
        board[i][j] = ""
        if move_val > best_val:
            move = (i, j)
            best_val = move_val
    return move

# Game Loop
while True:
    take_canvas_screenshot(driver)
    board = detect_board_state()

    winner = check_winner(board)
    if winner:
        print("Game Over! Winner:", winner)
        break

    move = best_move(board)
    if move:
        make_move_on_canvas(driver, *move)
    else:
        print("Draw!")
        break

    time.sleep(3)

driver.quit()
