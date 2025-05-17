import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager

# Define XPaths for all 9 cells
square_xpaths = [
    "//div[@class='square top left']",      # index 0
    "//div[@class='square top']",           # index 1
    "//div[@class='square top right']",     # index 2
    "//div[@class='square left']",          # index 3
    "//div[@class='square']",               # index 4 (center)
    "//div[@class='square right']",         # index 5
    "//div[@class='square bottom left']",   # index 6
    "//div[@class='square bottom']",        # index 7
    "//div[@class='square bottom right']"   # index 8
]

# Define all 8 winning combinations by board index
win_combinations = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
    [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
    [0, 4, 8], [2, 4, 6]              # diagonals
]

def get_board_state(driver):
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
                board_state.append('')
    return board_state

def get_empty_indices(board):
    return [i for i, val in enumerate(board) if val == '']

def is_winning_combo(board, player, combo):
    return all(board[i] == player for i in combo)

def can_win(board, player):
    for i in get_empty_indices(board):
        temp_board = board.copy()
        temp_board[i] = player
        if any(is_winning_combo(temp_board, player, combo) for combo in win_combinations):
            return i
    return None

def play_best_move(driver):
    board = get_board_state(driver)
    empty = get_empty_indices(board)

    # 1. Try to win
    move = can_win(board, 'x')
    if move is not None:
        driver.find_element(By.XPATH, square_xpaths[move]).click()
        print(f"Played winning move at index {move}")
        return

    # 2. Block opponent win
    move = can_win(board, 'o')
    if move is not None:
        driver.find_element(By.XPATH, square_xpaths[move]).click()
        print(f"Blocked opponent at index {move}")
        return

    # 3. Take center if free
    if board[4] == '':
        driver.find_element(By.XPATH, square_xpaths[4]).click()
        print("Took center")
        return

    # 4. Take opposite corner
    corners = [(0, 8), (2, 6), (6, 2), (8, 0)]
    for (you, opp) in corners:
        if board[opp] == 'o' and board[you] == '':
            driver.find_element(By.XPATH, square_xpaths[you]).click()
            print(f"Took opposite corner: {you}")
            return

    # 5. Take empty corner
    for idx in [0, 2, 6, 8]:
        if board[idx] == '':
            driver.find_element(By.XPATH, square_xpaths[idx]).click()
            print(f"Took empty corner: {idx}")
            return

    # 6. Take empty side
    for idx in [1, 3, 5, 7]:
        if board[idx] == '':
            driver.find_element(By.XPATH, square_xpaths[idx]).click()
            print(f"Took empty side: {idx}")
            return

def check_winner(driver):
    board_state = get_board_state(driver)

    for combo in win_combinations:
        first = board_state[combo[0]]
        if first and all(board_state[i] == first for i in combo):
            print(f"{first.upper()} wins!")
            return f"{first} wins"

    if all(cell != '' for cell in board_state):
        print("It's a draw!")
        return "draw"

    return None

if __name__ == "__main__":
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("http://playtictactoe.org/")
    print("Launched Tic Tac Toe")

    time.sleep(4)  # wait for opponent move (bot plays second)

    while True:
        result = check_winner(driver)
        if result:
            print(f"Game Over: {result}")
            break

        play_best_move(driver)
        time.sleep(2)
