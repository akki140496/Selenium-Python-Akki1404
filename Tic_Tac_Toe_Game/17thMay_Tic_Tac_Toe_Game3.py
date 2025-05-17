import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager

# Board mapping (index-based)
square_xpaths = [
    "//div[@class='square top left']",
    "//div[@class='square top']",
    "//div[@class='square top right']",
    "//div[@class='square left']",
    "//div[@class='square']",
    "//div[@class='square right']",
    "//div[@class='square bottom left']",
    "//div[@class='square bottom']",
    "//div[@class='square bottom right']"
]

win_combinations = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],
    [0, 3, 6], [1, 4, 7], [2, 5, 8],
    [0, 4, 8], [2, 4, 6]
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

def check_winner(driver):
    board = get_board_state(driver)
    for combo in win_combinations:
        first = board[combo[0]]
        if first and all(board[i] == first for i in combo):
            return first
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

def play_best_move(driver):
    board = get_board_state(driver)

    move = can_win(board, 'x')
    if move is not None:
        print(f"Played winning move at index {move}")
        driver.find_element(By.XPATH, square_xpaths[move]).click()
        return

    move = can_win(board, 'o')
    if move is not None:
        print(f"Blocked opponent at index {move}")
        driver.find_element(By.XPATH, square_xpaths[move]).click()
        return

    if board[4] == '':
        print("Took center")
        driver.find_element(By.XPATH, square_xpaths[4]).click()
        return

    for you, opp in [(0, 8), (2, 6), (6, 2), (8, 0)]:
        if board[opp] == 'o' and board[you] == '':
            print(f"Took opposite corner {you}")
            driver.find_element(By.XPATH, square_xpaths[you]).click()
            return

    for idx in [0, 2, 6, 8]:
        if board[idx] == '':
            print(f"Took empty corner {idx}")
            driver.find_element(By.XPATH, square_xpaths[idx]).click()
            return

    for idx in [1, 3, 5, 7]:
        if board[idx] == '':
            print(f"Took empty side {idx}")
            driver.find_element(By.XPATH, square_xpaths[idx]).click()
            return

if __name__ == "__main__":
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("http://playtictactoe.org/")
    print("🔄 Game launched. Waiting for opponent to move...")

    time.sleep(4)  # Wait for first move by opponent

    while True:
        result = check_winner(driver)
        if result:
            print_result(result)
            break

        try:
            play_best_move(driver)
        except Exception as e:
            print(f"⚠️ Error during move: {e}")
            break

        time.sleep(2)

        result = check_winner(driver)
        if result:
            print_result(result)
            break
