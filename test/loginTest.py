import time
from Utils import init_web_driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from Utils import waiting_dom_loaded, is_dom_exist

passWord = "12345678"

driver = init_web_driver(r'D:\rich\pythonProject1\webEnv\1')
driver.get('chrome-extension://ogclokjhnpcoojbnkgilfopgoppgbjcb/home.html#unlock')
driver.implicitly_wait(5)

# 输入密码
driver.find_element(By.ID, "password").send_keys(passWord)
driver.implicitly_wait(5)

# 点击登录
driver.find_element(By.CLASS_NAME, "btn-default").click()
driver.implicitly_wait(5)

# 打开项目地址
driver.execute_script("window.open('https://app.starrynift.art/Citizen-pad', '_blank')")
driver.implicitly_wait(5)

time.sleep(1000)