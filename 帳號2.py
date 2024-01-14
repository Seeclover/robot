from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

url = 'https://youthdream.phdf.org.tw/project/show/787'
driver = webdriver.Chrome()  
driver.get(url)

vote_button_xpath = '//*[@id="project-info"]/div[2]/div[4]/div/a[2]'
vote_button = WebDriverWait(driver, 100).until(
    EC.element_to_be_clickable((By.XPATH, vote_button_xpath))
)
vote_button.click()

social_button_xpath = '//*[@id="social"]/a[2]'
social_button = WebDriverWait(driver, 100).until(
    EC.element_to_be_clickable((By.XPATH, social_button_xpath))
)
social_button.click()

username_input = WebDriverWait(driver, 500).until(
    EC.presence_of_element_located((By.ID, "identifierId"))
)
username_input.send_keys("   ")

WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "identifierNext"))
).click()

password_input = WebDriverWait(driver, 500).until(
    EC.presence_of_element_located((By.NAME, "Passwd"))
)
password_input.send_keys("   ")

WebDriverWait(driver, 100).until(
    EC.visibility_of_element_located((By.ID, "passwordNext"))
).click()

tab_element_xpath = '//*[@id="tabs"]/a[1]'
tab_element = WebDriverWait(driver, 100).until(
    EC.element_to_be_clickable((By.XPATH, tab_element_xpath))
)
tab_element.click()

driver.get('https://youthdream.phdf.org.tw/project/show/787')

vote_button = WebDriverWait(driver, 100).until(
    EC.element_to_be_clickable((By.XPATH, vote_button_xpath))
)
vote_button.click()

time.sleep(5)

print('Success')
