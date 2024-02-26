from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException
import time



PASSWORD = "testaccount123456"
USERNAME = "teststst751@gmail.com"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
ACCOUNT_TO_FOLLOW = input("ENTER AN ACCOUNT whose followers you want to follow:  ") #example:  _cooking_chef
driver.get("https://www.instagram.com/")



time.sleep(4)
cookieAcceptButton = driver.find_element(By.XPATH,value='/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[1]')
cookieAcceptButton.click()

username = driver.find_element(By.NAME, value="username")
password = driver.find_element(By.NAME, value="password")

username.send_keys(USERNAME)
password.send_keys(PASSWORD)

loginButton = driver.find_element(By.XPATH,value='//*[@id="loginForm"]/div/div[3]/button/div')
time.sleep(4)
loginButton.click()

time.sleep(4)

dont_save = driver.find_element(By.CLASS_NAME, value="_ac8f")
dont_save.click()

time.sleep(4)

not_now = driver.find_element(By.CLASS_NAME, value="_a9_1")
not_now.click()

time.sleep(4)
sökButton = driver.find_element(By.CLASS_NAME, value="x5n08af")
sökButton.click()

driver.get(f"https://www.instagram.com/{ACCOUNT_TO_FOLLOW}/followers")

time.sleep(3)

all_buttons = driver.find_elements(By.CSS_SELECTOR, value='._aano button')

for button in all_buttons:
    time.sleep(1)
    button.click()



