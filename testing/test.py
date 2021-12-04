from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

url = 'https://www.whatismybrowser.com/detect/what-is-my-user-agent'
s = Service('./chromedriver')
driver = webdriver.Chrome(service=s)

driver.get('https://vk.com/')

email_input = driver.find_element(By.ID, 'index_email')
email_input.clear()
email_input.send_keys('')
pass_input = driver.find_element(By.ID, '')
pass_input.clear()
pass_input.send_keys('', Keys.ENTER)

#login_button = driver.find_element(By.ID, 'index_login_button').click()
