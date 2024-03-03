import time

from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

# 初始化浏览器
def init_web_driver(chrome_data_dir):
    options = ChromeOptions()
    # 屏蔽受控提示
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_experimental_option('useAutomationExtension', False)
    # 避免webdriver检测
    options.add_argument('--disable-blink-features')
    options.add_argument('--disable-blink-features=AutomationControlled')
    # 窗口最大化
    options.add_argument("--start-maximized")
    # --headless 不显示浏览器启动及执行过程
    # options.add_argument('--headless')
    # 加载小狐狸、yes
    # options.add_extension(r'D:\rich\pythonProject1\plugins\metamask-chrome-11.7.3.1.crx')
    # 加载用户数据
    options.add_argument('--user-data-dir=' + chrome_data_dir)
    options.add_argument('--profile-directory=Default')
    # 设置user-agent
    options.add_argument(
        'User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')
    # 设置驱动
    #driver = webdriver.Chrome(options=options, service=Service(executable_path=ChromeDriverManager().install()))
    service = Service(executable_path="~/warehouse/web3/chromedriver/120.0.6099.109/chromedriver")
    driver = webdriver.Chrome(options=options, service=service)
    return driver

def is_dom_exist(cssSelector, driver):
    try:
        driver.find_element(By.CSS_SELECTOR, cssSelector)
        return 1
    except NoSuchElementException:
        return 0

def waiting_dom_loaded(cssSelector, driver):
    try:
        driver.find_element(By.CSS_SELECTOR, cssSelector)
        print("dom已找到：", cssSelector)
        return 1
    except NoSuchElementException:
        print("dom未找到：", cssSelector)
        time.sleep(1)
        waiting_dom_loaded(cssSelector, driver)

def waiting_dom_loaded_space_only(cssSelector, driver):
    if is_dom_exist(".a", driver):
        driver.back()
    try:
        driver.find_element(By.CSS_SELECTOR, cssSelector)
        print("dom已找到：", cssSelector)
        return 1
    except NoSuchElementException:
        print("dom未找到：", cssSelector)
        time.sleep(1)
        waiting_dom_loaded(cssSelector, driver)

class waitingDOM:
    def __init__(self, cssSelector, driver):
        self.cssSelector = cssSelector
        self.driver = driver
        self.count = 0
    def appear(self):
        try:
            self.driver.find_element(By.CSS_SELECTOR, self.cssSelector)
            print("dom已出现：", self.cssSelector)
            return 1
        except:
            print("dom未出现：", self.count, self.cssSelector)
            if self.count == 30:
                self.count = 0
                self.driver.refresh()
            time.sleep(1)
            self.count = self.count + 1
            self.appear()
    def disappear(self):
        try:
            self.driver.find_element(By.CSS_SELECTOR, self.cssSelector)
            if self.count == 30:
                self.count = 0
                self.driver.refresh()
            print("dom仍在：", self.count, self.cssSelector)
            time.sleep(1)
            self.count = self.count + 1
            self.disappear()
        except:
            print("dom消失：", self.cssSelector)
            return 1

def click_one_dom(cssSelector, driver):
    try:
        driver.find_element(By.CSS_SELECTOR, cssSelector).click()
        return 1
    except:
        return 0

def confirm_signature(driver):
    time.sleep(5)
    driver.switch_to.window(driver.window_handles[-1])  # 切换到最新窗口，可能是本窗口，也可能是小狐狸的弹窗
    time.sleep(1)
    if is_dom_exist('.button.btn--rounded.btn-primary.page-container__footer-button', driver):
        driver.find_element(By.CSS_SELECTOR, ".button.btn--rounded.btn-primary.page-container__footer-button").click()
        time.sleep(1)
    time.sleep(1)
    driver.switch_to.window(driver.window_handles[-1])
    time.sleep(1)

def confirm_wallet_connect(driver):
    if is_dom_exist('.ant-btn.ant-btn-default._cneterBtn_k8sci_64', driver):
        driver.find_element(By.CSS_SELECTOR, ".ant-btn.ant-btn-default._cneterBtn_k8sci_64").click()  #  新开页面的都建议延迟5秒后再切换窗口
        time.sleep(5)
        # 小狐狸弹窗确认签名请求
        driver.switch_to.window(driver.window_handles[-1])  # 切换到最新窗口
        waitingDOM(".request-signature__origin", driver).appear()  # 等待签名页面加载完成
        driver.find_element(By.CSS_SELECTOR, ".button.btn--rounded.btn-primary.page-container__footer-button").click()  # 点击签名
        time.sleep(5)
        driver.switch_to.window(driver.window_handles[-1])  # 切换到最新窗口
        time.sleep(1)

def login_metatask_and_project(passWord, driver):
    # 输入密码
    driver.find_element(By.ID, "password").send_keys(passWord)
    # 点击登录
    driver.find_element(By.CLASS_NAME, "btn-default").click()
    # 关闭可能的弹窗
    driver.implicitly_wait(0)  # 等待时间置为0
    if is_dom_exist(".button.btn--rounded.btn-primary.page-container__footer-button", driver):
        driver.find_element(By.CSS_SELECTOR, ".button.btn--rounded.btn-primary.page-container__footer-button").click()
    if is_dom_exist(".popover-container .mm-box.mm-button-icon.mm-button-icon--size-sm.mm-box--display-inline-flex.mm-box--justify-content-center.mm-box--align-items-center.mm-box--color-icon-default.mm-box--background-color-transparent.mm-box--rounded-lg", driver) == 1:
        driver.find_element(By.CSS_SELECTOR, ".popover-container .mm-box.mm-button-icon.mm-button-icon--size-sm.mm-box--display-inline-flex.mm-box--justify-content-center.mm-box--align-items-center.mm-box--color-icon-default.mm-box--background-color-transparent.mm-box--rounded-lg").click()
    driver.implicitly_wait(2)  # 等待时间恢复未2
    # 打开项目地址
    driver.execute_script("window.open('https://app.starrynift.art/Citizen-pad', '_blank')")
    time.sleep(5)
    driver.switch_to.window(driver.window_handles[-1])  # 跳转到最新的句柄
    waitingDOM("._logo_dgei9_180", driver).appear()  # 确保网页加载完成
    time.sleep(1)
    # 判断项目网页是否弹出链接钱包请求-偶尔弹出提醒
    confirm_wallet_connect(driver)

    time.sleep(5)  # 只要窗口标签变化了最好加个sleep
    driver.switch_to.window(driver.window_handles[-1])  # 切换当前窗口
    # 判断是否链接钱包
    if is_dom_exist("._noConnect_name_9xb8y_129", driver):  # 如果没链接，则先链接钱包
        driver.find_element(By.CSS_SELECTOR, "._noConnect_name_9xb8y_129").click()
        # 在弹窗中点击metaTask选项
        driver.find_element(By.CLASS_NAME, "_modelWallet_10en4_40").click()
        time.sleep(5)
        driver.switch_to.window(driver.window_handles[-1])  # 切换到小狐狸确认窗口
        waitingDOM(".request-signature__origin", driver).appear()
        try:
            driver.find_element(By.CSS_SELECTOR, ".button.btn--rounded.btn-primary.page-container__footer-button").click()
            driver.find_element(By.CSS_SELECTOR, ".button.btn--rounded.btn-primary.page-container__footer-button").click()
            driver.find_element(By.CSS_SELECTOR, ".button.btn--rounded.btn-primary.page-container__footer-button").click()
        except:
            time.sleep(0)
    driver.switch_to.window(driver.window_handles[-1])
    # 选择下拉链接BSC网络
    driver.find_element(By.CLASS_NAME, "ant-dropdown-trigger").click()
    # 选择bsc
    driver.find_element(By.CLASS_NAME, "ant-dropdown-menu-item").click()

    try:  # 第一次链接网络的代码，若第二次会直接报错跳过
        # 点击批准
        driver.find_element(By.CSS_SELECTOR, ".confirmation-footer__actions .button.btn--rounded.btn-primary").click()
        driver.switch_to.window(driver.window_handles[-1])  # 跳转到最新的句柄
        # 点击切换网络
        driver.find_element(By.CSS_SELECTOR, ".confirmation-footer__actions .button.btn--rounded.btn-primary").click()
    except:
        time.sleep(0)

userDataList = [
    {
        'webEnvPath': r'D:\rich\pythonProject1\webEnv100\0',
        'helpWord': 'earth blood polar quit feature fun review cover skull snake able recycle',
        'passWord': '12345678',
        'profileUrl': 'https://app.starrynift.art/@YUQJqLbn2j?referralCode=ru9w_Eft_G',
    },
    {
        'webEnvPath': r'D:\rich\pythonProject1\webEnv100\1',
        'helpWord': 'manual add knife praise fortune little endless course brisk sight wrist style',
        'passWord': '12345678',
        'profileUrl': 'https://app.starrynift.art/@Nu28faRjtg?referralCode=IYxdq5HLZj',
    },
    {
        'webEnvPath': r'D:\rich\pythonProject1\webEnv100\2',
        'helpWord': 'auto demand season track vast isolate hurdle napkin dinosaur term ski addict',
        'passWord': 'qwer1234!@#$',
        'profileUrl': 'https://app.starrynift.art/@RwcANOvVWr?referralCode=fixTjasfwL',
    },
    {
        'webEnvPath': r'D:\rich\pythonProject1\webEnv100\3',
        'helpWord': 'laundry trial pear insane neither scare foot animal page brown keen ramp',
        'passWord': 'qwer1234!@#$',
        'profileUrl': 'https://app.starrynift.art/@5mGs0vc3ZX?referralCode=a8it3qpy_d',
    },
]

