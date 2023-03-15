import time
import os

import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
load_dotenv()


chrome_driver_path = "C:\development\chromedriver.exe"
chr_options = webdriver.ChromeOptions()
chr_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(chrome_driver_path), options=chr_options)
driver.maximize_window()
driver.get("https://tinder.com/")

time.sleep(8)

login_button = driver.find_element(By.XPATH, "//*[@id='s-1432688076']/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]")
login_button.click()

time.sleep(3)

facebook_login = driver.find_element(By.XPATH, '//*[@id="s-1211347640"]/main/div/div/div[1]/div/div/div[3]/span/div[2]/button/div[2]/div[2]/div')
facebook_login.click()

# switching to facebook login window
fb_window = driver.window_handles[-1]
driver.switch_to.window(fb_window)

time.sleep(8)
# email_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'email')))
email_field = driver.find_element(By.ID, "email")
email_field.send_keys(os.getenv("EMAIL"))

password_field = driver.find_element(By.ID, 'pass')
password_field.send_keys(os.getenv("PASSWORD"))
password_field.send_keys(Keys.RETURN)

driver.switch_to.window(driver.window_handles[0])


