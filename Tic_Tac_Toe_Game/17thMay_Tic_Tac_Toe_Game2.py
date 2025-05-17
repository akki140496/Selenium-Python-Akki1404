import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager

# Define square XPaths by board index (0–8)
square_xpaths = [
    "//div[@class='square top left']",      # 0
    "//div[@class='square top']",           # 1
    "//div[@class='square top right']",     # 2
    "//div[@class='square left']",          # 3
    "//div[@class='square']",               # 4 (center)
    "//div[@class='square right']",         # 5
    "//div[@class='square bottom left']",   # 6
    "//div[@class='square bottom']",        # 7
    "//div[@class='square bottom right']"   # 8
]

# All 8 winning combinations (by index)
win_combinations = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
    [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
    [0, 4, 8], [2, 4, 6]              # Diagonals
]

def get_board_state(driver):
    board = []
    for xpath in square_xpaths:
        try:
            driver.find_element(By.XPATH, f"{xpath}//div[@class='x']")
            board.append('x')
        except NoSuchElementException:
            try:
                driver.find_element(By.XPATH, f"{xpath}//div[@class='o']")
                board.append('o')
            except NoSuchElementException:
                board.append('')
    return board

def get_empty_indices(board):
    return [i for i, val in enumerate(board) if val == '']

def is_winning_combo(board, player, combo):
    return all(board[i] == player for i in combo)

def can_win(board, player):
    for i in get_empty_indices(board):
        temp = board.copy()
        temp[i] = player
        if any(is_winning_combo(temp, player, combo) for combo in win_combinations):
            return i
    return None

def play_best_move(driver):
    board = get_board_state(driver)

    # 1. Win if possible
    move = can_win(board, 'x')
    if move is not None:
        driver.find_element(By.XPATH, square_xpaths[move]).click()
        print(f"Played winning move at index {move}")
        return

    # 2. Block opponent
    move = can_win(board, 'o')
    if move is not None:
        driver.find_element(By.XPATH, square_xpaths[move]).click()
        print(f"Blocked opponent at index {move}")
        return

    # 3. Take center
    if board[4] == '':
        driver.find_element(By.XPATH, square_xpaths[4]).click()
        print("Took center")
        return

    # 4. Take opposite corner
    for you, opp in [(0, 8), (2, 6), (6, 2), (8, 0)]:
        if board[opp] == 'o' and board[you] == '':
            driver.find_element(By.XPATH, square_xpaths[you]).click()
            print(f"Took opposite corner {you}")
            return

    # 5. Take empty corner
    for idx in [0, 2, 6, 8]:
        if board[idx] == '':
            driver.find_element(By.XPATH, square_xpaths[idx]).click()
            print(f"Took empty corner {idx}")
            return

    # 6. Take empty side
    for idx in [1, 3, 5, 7]:
        if board[idx] == '':
            driver.find_element(By.XPATH, square_xpaths[idx]).click()
            print(f"Took empty side {idx}")
            return

def check_winner(driver):
    board = get_board_state(driver)

    for combo in win_combinations:
        first = board[combo[0]]
        if first and all(board[i] == first for i in combo):
            return first  # 'x' or 'o'

    if all(cell != '' for cell in board):
        return 'draw'

    return None

def print_result(result):
    if result == 'x':
        print("\n🎉 You (X) WIN the game!")
    elif result == 'o':
        print("\n😞 You (X) LOST the game.")
    elif result == 'draw':
        print("\n🤝 The game is a DRAW.")
    else:
        print("\n❓ Game state unknown.")

# === Main Driver ===
if __name__ == "__main__":
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("http://playtictactoe.org/")
    print("🔄 Game launched. Waiting for opponent to move...")

    time.sleep(4)  # Wait for the opponent (O) to play first

    while True:
        result = check_winner(driver)
        if result:
            print_result(result)
            break

        play_best_move(driver)
        time.sleep(2)
    time.sleep(10)


