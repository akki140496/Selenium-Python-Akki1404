from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

# Define lists for validation
expected_column_values = ['First Name', 'Last Name', 'Age', 'Email', 'Salary', 'Department', 'Action']
expected_row_values = ['Cierra', 'Vega', '39', 'cierra@example.com', '10000', 'Insurance', '']

# Initialize the web driver (Chrome in this case)
#############  Chrome Driver Manager ########################################
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get('https://www.tutorialspoint.com/selenium/practice/webtables.php#')

# Navigate to the web page containing the table
# driver.get("https://example.com/table-page")

# Give the page some time to load
time.sleep(3)

# Locate the table element by XPath or other selector methods
table = driver.find_element(By.XPATH, '//table')

# Extract headers (first row) for column validation
headers = table.find_elements(By.XPATH, './/thead/tr/th')
header_texts = [header.text for header in headers]

# Validate column headers
if header_texts == expected_column_values:
    print("Column values match!")
else:
    print("Column values do not match!")

# Extract the first row of the table body (assuming it's in a <tbody>)
first_row = table.find_elements(By.XPATH, './/tbody/tr[1]/td')
first_row_texts = [cell.text for cell in first_row]

# Validate the first row values
if first_row_texts == expected_row_values:
    print("First row values match!")
else:
    print("First row values do not match!")

# Optionally, you can print the mismatched values for debugging
if header_texts != expected_column_values:
    print("Expected columns:", expected_column_values)
    print("Actual columns:", header_texts)

if first_row_texts != expected_row_values:
    print("Expected first row:", expected_row_values)
    print("Actual first row:", first_row_texts)

# Close the browser after validation
driver.quit()
