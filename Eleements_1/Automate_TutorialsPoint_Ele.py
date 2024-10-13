import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd


#############  Chrome Driver Manager ########################################
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get('https://www.tutorialspoint.com/selenium/practice/text-box.php')
driver.maximize_window()
time.sleep(5)

####  Variable Declaration Xpaths ###########


#####   Text Box Xpaths #####################

Full_name_xpath = "//input[@id='fullname']"
Email_xpath = "//input[@id='email']"
Current_address_xpath = "//textarea[@id='address']"
Password_xpath = "//input[@id='password']"
submit_xpath = "//input[@value='Submit']"

#####   Check Box Xpaths ######################
Element_button_xpath = "//button[text()=' Elements']"
Checkbox_button_xpath = "//a[text()=' Check Box']"
first_plus_xpath = "(//li[@id='bs_1']//span[@class='plus'])[1]"
Sub_level_2_label_xpath = "//input[@id='c_bf_2']"
secound_plus_xpath = "//li[@id='bs_2']//span[@class='plus']"
Sub_level_3_label_xpath = "//input[@id='c_bf_3']"

##### Radio Button Xpath ###########

RadioButton_xpath = "//a[text()=' Radio Button']"
Radio_Text_Headline_Xpath = "//p[text()='Do you like the site?']"
Yes_RadioButton_Xpath = "//input[@value='igottwo']"
First_part_Text_YesXpath = "//div[@id='check']"
Secound_part_Text_YesXpath = "//div[@id='check']//b"
Impressive_Radio_Button_XPath = "//input[@value='igotthree']"
First_part_Text_ImpressiveXpath = "//div[@id='check1']"
Secound_part_Text_ImpressiveXpath = "//div[@id='check1']//b"

###    Web Table XPATH ##########
WebTable_Xpath = "//a[text()=' Web Tables']"
WebTable_FirstColoumn_Xpath = "//th[text()='First Name']"
WebTable_SecoundColoumn_Xpath = "//th[text()='Last Name']"
WebTable_ThirdColoumn_Xpath = "//th[text()='Age']"
WebTable_FourthColoumn_Xpath = "//th[text()='Email']"
WebTable_FivthColoumn_Xpath = "//th[text()='Salary']"
WebTable_SixColoumn_Xpath = "//th[text()='Department']"
WebTable_SevenColoumn_Xpath = "//th[text()='Action']"
Add_Button_XPath = "//button[text()='Add']"
First_Name_Xpath = "//input[@id='firstname'][1]"
Last_Name_Xpath = "//input[@id='lastname'][1]"
Email_xpath = "//input[@id='email'][1]"
Age_Xpath = "//input[@id='age'][1]"
Salary_Xpath = "//input[@id='salary'][1]"
Department_Xpath = "//input[@id='deparment'][1]"
Login_WTXpath = "//input[@value='Login']"
First_label_error_xpath = "//label[@id='firstname-error']"
Last_label_error_xpath  = "//label[@id='lastname-error']"
age_error_xpath = "//label[@id='age-error']"
salary_error_xpath = "//label[@id='salary-error']"
Close_button_xpath = "//button[@aria-label='Close']"

#### Buttons Xpath ###########
Button_Headline_Xpath = "//h1[text()='Buttons']"
Click_Me_Button_Xpath = "//button[text()='Click Me']"
Right_Click_Me_Button_Xpath = "//button[text()='Right Click Me']"
Double_Click_Me_Button_Xpath = "//button[text()='Double Click Me']"
Button_Page_Xpath = "//a[text()=' Buttons']"
Click_Me_Text_Xpath = "//div[@id='welcomeDiv']"
Double_Click_Me_Text_Button = "//p[@id='doublec']"

##########   Link Xpaths  #########
link_Tab_Xpath = "//a[text()=' Links']"
link_Headline_Xpath = "//h1[text()='Links']"
Home_Link_Xpath = "//a[text()='Home']"
HomePWPU_Link_XPath = "//a[text()='HomewPWPU']"
Created_Link_XPath = "//a[text()='Created']"
NoContent_Link_XPath = "//a[text()='No Content']"
Moved_Link_XPath = "//a[text()='Moved']"
Bad_Request_Link_XPath = "//a[text()='Bad Request']"
Unauthorised_Link_XPath = "//a[text()='Unauthorized']"
Forbidden_Link_Xpath = "//a[text()='Forbidden']"
Not_Found_Link_Xpath = "//a[text()='Not Found']"
Create_class_text_Xpath = "//div[@class='create']"
Create_class_status_code_Xpath = "//div[@class='create']//b[1]"



#######  Function Declaraction ####################
def textbox_verification():

    driver.implicitly_wait(20)
    full_name = driver.find_element(By.XPATH, Full_name_xpath)
    full_name.send_keys("Mr. Akshay Sharma")
    driver.implicitly_wait(20)
    Email = driver.find_element(By.XPATH, Email_xpath)
    Email.send_keys("AkshaySharma@yopmail.com")
    driver.implicitly_wait(30)
    Current_address = driver.find_element(By.XPATH, Current_address_xpath)
    Current_address.send_keys("D-11/254  , Sector -7 Rohini New Delhi ")
    driver.implicitly_wait(20)
    Password = driver.find_element(By.XPATH, Password_xpath)
    Password.send_keys("@12345678")
    driver.implicitly_wait(20)
    Submit = driver.find_element(By.XPATH, submit_xpath)
    Submit.click()
    time.sleep(5)
    # driver.quit()

def checkbox_verification():
    driver.implicitly_wait(20)
    Element_button = driver.find_element(By.XPATH, Element_button_xpath)
    Element_button.click()
    driver.implicitly_wait(20)
    Checkbox_button = driver.find_element(By.XPATH, Checkbox_button_xpath)
    Checkbox_button.click()
    driver.implicitly_wait(20)
    first_plus = driver.find_element(By.XPATH, first_plus_xpath)
    first_plus.click()
    driver.implicitly_wait(20)
    Sub_level_2_label = driver.find_element(By.XPATH, Sub_level_2_label_xpath)
    Sub_level_2_label.click()
    # time.sleep(3)
    driver.implicitly_wait(20)
    Secound_plus = driver.find_element(By.XPATH, secound_plus_xpath)
    Secound_plus.click()
    driver.implicitly_wait(20)
    Sub_level_3_label = driver.find_element(By.XPATH, Sub_level_3_label_xpath)
    Sub_level_3_label.click()
    time.sleep(5)

def RadioButton_Verification():
    expected_text ='Do you like the site?'
    expected_yes_text = 'You have checked Yes'
    expected_Impressive_text = 'You have checked Impressive'
    driver.implicitly_wait(20)
    Element_button = driver.find_element(By.XPATH, Element_button_xpath)
    Element_button.click()
    driver.implicitly_wait(20)
    RadioButton = driver.find_element(By.XPATH, RadioButton_xpath)
    RadioButton.click()
    element = driver.find_element(By.XPATH, Radio_Text_Headline_Xpath)
    Radio_Text_Headline = element.text
    assert expected_text in Radio_Text_Headline, f"'{expected_text}' not found in the Page"
    print("Text Found Successfully")
    Yes_RadioButton = driver.find_element(By.XPATH, Yes_RadioButton_Xpath)
    Yes_RadioButton.click()
    First_part_Text_Yes = driver.find_element(By.XPATH, First_part_Text_YesXpath)
    first_Yes_Text = First_part_Text_Yes.text
    Secound_part_Text_Yes = driver.find_element(By.XPATH, Secound_part_Text_YesXpath)
    sec_Yes_Text = Secound_part_Text_Yes.text
    third_Yes_Text = first_Yes_Text + "" + sec_Yes_Text
    assert expected_yes_text in third_Yes_Text , f"'{expected_yes_text}' not found after the Yes Click"
    print("expected yes text"+ " " + third_Yes_Text)
    time.sleep(2)
    Impressive_Radio_Button = driver.find_element(By.XPATH, Impressive_Radio_Button_XPath)
    Impressive_Radio_Button.click()
    First_part_Text_Impressive = driver.find_element(By.XPATH, First_part_Text_ImpressiveXpath)
    first_Impressive_Text = First_part_Text_Impressive.text
    Secound_part_Text_Impressive = driver.find_element(By.XPATH, Secound_part_Text_ImpressiveXpath)
    sec_Impressive_Text = Secound_part_Text_Impressive.text
    third_Impressive_Text = first_Impressive_Text + "" + sec_Impressive_Text
    assert expected_Impressive_text in third_Impressive_Text, f"'{expected_Impressive_text}' not found after the Impressive click "
    print("expecteed Impressive Text"+ " " + expected_Impressive_text)
    time.sleep(5)

def WebTable_Verification():
    driver.implicitly_wait(20)
    expected_Reg_Form_Text = "This field is required."
    expected_First_coloumn = "First Name"
    expected_Secound_coloumn = "Last Name"
    expected_third_coloumn = "Age"
    expected_fourth_coloumn = "Email"
    expected_fivth_coloumn = "Salary"
    expected_sixth_coloumn = "Department"
    expected_seventh_coloumn = "Action"
    Element_button = driver.find_element(By.XPATH, Element_button_xpath)
    Element_button.click()
    driver.implicitly_wait(20)
    WebTable = driver.find_element(By.XPATH, WebTable_Xpath)
    WebTable.click()
    WebTable_FirstColoumn = driver.find_element(By.XPATH,WebTable_FirstColoumn_Xpath).text
    WebTable_SecoundColoumn = driver.find_element(By.XPATH,WebTable_SecoundColoumn_Xpath).text
    WebTable_ThirdColoumn = driver.find_element(By.XPATH,WebTable_ThirdColoumn_Xpath).text
    WebTable_FourthColoumn = driver.find_element(By.XPATH,WebTable_FourthColoumn_Xpath).text
    WebTable_FivthColoumn = driver.find_element(By.XPATH,WebTable_FivthColoumn_Xpath).text
    WebTable_SixColoumn = driver.find_element(By.XPATH,WebTable_SixColoumn_Xpath).text
    WebTable_SevenColoumn = driver.find_element(By.XPATH,WebTable_SevenColoumn_Xpath).text
    print("The Web Table has been started ")
    assert expected_First_coloumn in WebTable_FirstColoumn, f"'{expected_First_coloumn}' coloumn header not found in the WebTable"
    assert expected_Secound_coloumn in WebTable_SecoundColoumn,f"'{expected_Secound_coloumn}'coloumn header not found in the WebTable"
    assert expected_third_coloumn in WebTable_ThirdColoumn, f"'{expected_third_coloumn}' coloumn header not found in the WebTable"
    assert expected_fourth_coloumn in WebTable_FourthColoumn, f"'{expected_fourth_coloumn}' coloumn header not found in the WebTable"
    assert expected_fivth_coloumn in WebTable_FivthColoumn, f"'{expected_fivth_coloumn}'coloumn header not found in the WebTable"
    assert expected_sixth_coloumn in WebTable_SixColoumn, f"'{expected_sixth_coloumn}'coloumn header not found in the WebTable"
    assert expected_seventh_coloumn in WebTable_SevenColoumn, f"'{expected_seventh_coloumn}'coloumn header not found in the WebTable"
    print("The Web Table Coloumn verification End ")
    driver.implicitly_wait(20)
    Add_Button = driver.find_element(By.XPATH,Add_Button_XPath)
    Add_Button.click()
    driver.implicitly_wait(20)
    First_Name = driver.find_element(By.XPATH,First_Name_Xpath)
    First_Name.send_keys("Akshay")
    Last_Name = driver.find_element(By.XPATH,Last_Name_Xpath)
    Last_Name.send_keys("Sharma")
    Email = driver.find_element(By.XPATH,Email_xpath)
    Email.send_keys("Akkibelieve1404@gmail.com")
    Age = driver.find_element(By.XPATH,Age_Xpath)
    Age.send_keys('twenty eight ')
    Salary = driver.find_element(By.XPATH,Salary_Xpath)
    Salary.send_keys("Five lakhs fifty five thousand seventy five rupees")
    Department = driver.find_element(By.XPATH,Department_Xpath)
    Department.send_keys("QA Automation + Emnterprenaur")
    Login_Button = driver.find_element(By.XPATH,Login_WTXpath)
    Login_Button.click()
    time.sleep(3)
    driver.implicitly_wait(20)
    Add_Button = driver.find_element(By.XPATH,Add_Button_XPath)
    Add_Button.click()
    driver.implicitly_wait(20)
    Login_Button = driver.find_element(By.XPATH,Login_WTXpath)
    Login_Button.click()
    time.sleep(2)
    First_label_error = driver.find_element(By.XPATH,First_label_error_xpath).text
    Last_label_error = driver.find_element(By.XPATH, Last_label_error_xpath).text
    age_error = driver.find_element(By.XPATH,age_error_xpath).text
    salary_error = driver.find_element(By.XPATH,salary_error_xpath).text
    if First_label_error == expected_Reg_Form_Text:
        print("First Label error Found")
        time.sleep(1)
    if Last_label_error == expected_Reg_Form_Text:
        print("Secound Label Error Text")
        time.sleep(1)
    if age_error == expected_Reg_Form_Text:
        print("Age Label Error text ")
        time.sleep(1)
    if salary_error == expected_Reg_Form_Text:
        print("Salary Error text")
        time.sleep(1)

    Close_button = driver.find_element(By.XPATH, Close_button_xpath)
    Close_button.click()
    time.sleep(5)

def Button_Verification():
    Click_Me_expected_text = "You have done a dynamic click"
    Double_Click_Me_expected_text = "You have Double clicked"
    Button_expected_text = "Buttons"
    driver.implicitly_wait(20)
    Element_button = driver.find_element(By.XPATH, Element_button_xpath)
    Element_button.click()
    driver.implicitly_wait(20)
    Button_Page = driver.find_element(By.XPATH, Button_Page_Xpath)
    Button_Page.click()
    driver.implicitly_wait(20)
    Button_Headline = driver.find_element(By.XPATH,Button_Headline_Xpath).text
    if Button_Headline == Button_expected_text:
        print("Yes we landed on the correct Button Page ")
    else:
        print("Wrong Page  Landed")

    Click_Me_Button = driver.find_element(By.XPATH, Click_Me_Button_Xpath)
    Click_Me_Button.click()
    Click_Me_Button_Text = driver.find_element(By.XPATH, Click_Me_Text_Xpath).text
    if Click_Me_Button_Text == Click_Me_expected_text:
        print("The Click Me Button valid text has been called ")
    time.sleep(2)
    actions = ActionChains(driver)
    Right_Click_Me_Button = driver.find_element(By.XPATH, Right_Click_Me_Button_Xpath)
    # actions.context_click(Right_Click_Me_Button).perform()
    Right_Click_Me_Button.click()
    time.sleep(2)

    Double_Click_Me_Button = driver.find_element(By.XPATH, Double_Click_Me_Button_Xpath)
    actions.double_click(Double_Click_Me_Button).perform()
    Double_Click_Me_Text_ButtonA = driver.find_element(By.XPATH,Double_Click_Me_Text_Button).text
    print(Double_Click_Me_Text_ButtonA)
    time.sleep(1)
    if Double_Click_Me_Text_ButtonA == Double_Click_Me_expected_text:
        print("The Double Click Me valid text has been called ")
        print(Double_Click_Me_Text_ButtonA)
    time.sleep(5)

def Link_Verification():
    exoected_link_tab = "Links"

    driver.implicitly_wait(20)
    Element_button = driver.find_element(By.XPATH, Element_button_xpath)
    Element_button.click()
    driver.implicitly_wait(20)
    Link_Tab = driver.find_element(By.XPATH,link_Tab_Xpath)
    Link_Tab.click()
    driver.implicitly_wait(20)
    link_Headline = driver.find_element(By.XPATH,link_Headline_Xpath).text
    if exoected_link_tab == link_Headline:
        print("Landed on the Valid Page of Link Tab ")
    Home_Link = driver.find_element(By.XPATH,Home_Link_Xpath)
    Home_Link.click()
    time.sleep(1)
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(2)
    valid_new_tab_expected_title = "Quality Tutorials, Video Courses, and eBooks - TutorialsPoint"
    actual_title = driver.title
    if valid_new_tab_expected_title == actual_title:
        print("Landed on the Valid  Tab after Clicking the Home Link")
        time.sleep(1)
        driver.close()
    time.sleep(3)
    driver.switch_to.window(driver.window_handles[0])
    HomePWPU_Link = driver.find_element(By.XPATH, HomePWPU_Link_XPath)
    HomePWPU_Link.click()
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(1)
    url = driver.current_url
    if url == 'about:blank':
        print("The new tab is blank ")
    else:
        body_text = driver.find_element(By.TAG_NAME,'body').text.strip()
        if not body_text:
            print("The new tab is blank (empty content).")
            driver.close()
        else:
            print(f"The new tab has content. URL: {url}")
            driver.close()
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[0])

############ Main Function Creation and calling ########################
if __name__=="__main__":
    # textbox_verification()
    # time.sleep(5)
    # checkbox_verification()
    # time.sleep(5)
    # RadioButton_Verification()
    # time.sleep(5)
    # WebTable_Verification()
    # time.sleep(5)
    # Button_Verification()
    # time.sleep(5)
    Link_Verification()
    time.sleep(5)
    driver.quit()

