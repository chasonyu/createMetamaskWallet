import time
from Utils import init_web_driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from Utils import waiting_dom_loaded

# 创建 WebDriver 对象，指明使用chrome浏览器驱动
driver = init_web_driver(r'D:\rich\pythonProject1\webEnv\1')

driver.get('chrome-extension://ogclokjhnpcoojbnkgilfopgoppgbjcb/home.html#unlock')
driver.implicitly_wait(5)

#输入密码
password = driver.find_element(By.ID, "password")
password.send_keys("qwer1234!@#$")
driver.implicitly_wait(5)

#点击登录
login = driver.find_element(By.CLASS_NAME, "btn-default")
login.click()
driver.implicitly_wait(5)

#打开项目地址
driver.execute_script("window.open('https://app.starrynift.art/Citizen-pad', '_blank')")
driver.implicitly_wait(5)

windows = driver.window_handles   # 获取该会话所有的句柄
driver.switch_to.window(windows[-1])  # 跳转到最新的句柄

# 通过判断这个logo是否加载出来，代表整个界面是否加载出来，且不需要判断logo真假，找不到logo程序会一直停在这查找
logo = waiting_dom_loaded("._logo_dgei9_180", driver)

#判断是否链接钱包
connect_flag = 0
try:
    driver.find_element(By.CLASS_NAME, "_noConnect_name_9xb8y_129")
    connect_flag = 1
except:
    connect_flag = 0
if connect_flag == 0: #如果没有这个节点，表示已经链接钱包了，不用管，直接跳出if，执行下面的选择网络
    time.sleep(1)
else:  #如果没链接，则先链接钱包
    driver.find_element(By.CLASS_NAME, "_noConnect_name_9xb8y_129").click()
    time.sleep(1)
    #在弹窗中点击metaTask选项
    driver.find_element(By.CLASS_NAME,"_modelWallet_10en4_40").click()
    driver.switch_to.window(windows[-1])  # 跳转到最新的句柄

    driver.find_element(By.CLASS_NAME, "button btn--rounded btn-primary page-container__footer-button").click()
    driver.find_element(By.CLASS_NAME, "button btn--rounded btn-primary page-container__footer-button").click()
    driver.find_element(By.CLASS_NAME, "button btn--rounded btn-primary page-container__footer-button").click()

#选择下拉
driver.find_element(By.CLASS_NAME, "ant-dropdown-trigger").click()
time.sleep(1)
#选择bsc
driver.find_element(By.CLASS_NAME, "ant-dropdown-menu-item").click()
time.sleep(1)

try:  #第一次链接网络的代码，若第二次会直接报错跳过
    windows = driver.window_handles
    driver.switch_to.window(windows[-1])  # 跳转到最新的句柄

    # 点击批准
    driver.find_element(By.CSS_SELECTOR, ".confirmation-footer__actions .button.btn--rounded.btn-primary").click()

    windows = driver.window_handles
    driver.switch_to.window(windows[-1])  # 跳转到最新的句柄

    # 点击切换网络
    driver.find_element(By.CSS_SELECTOR, ".confirmation-footer__actions .button.btn--rounded.btn-primary").click()
except:
    time.sleep(1)
#点击citizen
driver.find_element(By.CSS_SELECTOR, "._nav_list_box_dgei9_55 ._nav_one_dgei9_79:nth-child(4) ._menu_base_name_dgei9_93").click()
driver.implicitly_wait(5)
#点击mint
driver.find_element(By.CSS_SELECTOR, "._mint_words_sd0u4_135").click()

windows = driver.window_handles
driver.switch_to.window(windows[-1])  # 跳转到最新的句柄

#点击确定
try:  #仅第一次mint需要确定
    driver.find_element(By.CSS_SELECTOR, ".button.btn--rounded.btn-primary.page-container__footer-button").click()
    driver.implicitly_wait(5)
    driver.find_element(By.CSS_SELECTOR, ".button.btn--rounded.btn-primary.page-container__footer-button").click()
    driver.implicitly_wait(5)
except:
    time.sleep(1)

time.sleep(100)