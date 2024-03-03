import time

from Utils import init_web_driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

userCount = 7
passWord = "hgsy28'/.se58DEjT76><@"
webEnvPath = r'D:\rich\pythonProject1\webEnvTest'
helpWordPath = r'D:\rich\pythonProject1\userData\helpWord.txt'

my_file = open(helpWordPath, "w")

for n in range(userCount):
    # 创建 WebDriver 对象，指明使用chrome浏览器驱动
    envPath = webEnvPath + fr'\{n}'
    driver = init_web_driver(envPath)
    driver.get('chrome-extension://ogclokjhnpcoojbnkgilfopgoppgbjcb/home.html')

    # 等待加载
    driver.implicitly_wait(5)
    # 点击同意
    aggregate = driver.find_element(By.ID, "onboarding__terms-checkbox")
    aggregate.click()
    # 点击创建
    createButton = driver.find_element(By.CLASS_NAME, "btn-primary")
    createButton.click()
    # 点击我同意
    iAggregate = driver.find_element(By.CLASS_NAME, "btn-primary")
    iAggregate.click()
    # 输入密码
    password = driver.find_elements(By.CLASS_NAME, "form-field__input")
    password[0].send_keys(passWord)
    password[1].send_keys(passWord)
    # 我明白
    iUnderstand = driver.find_element(By.CLASS_NAME, "check-box")
    iUnderstand.click()
    # 创建钱包
    createAccount = driver.find_element(By.CLASS_NAME, "create-password__form--submit-button")
    createAccount.click()
    # 保护钱包
    defectAccount = driver.find_element(By.CLASS_NAME, "mm-button-primary")
    defectAccount.click()
    # 显示助记词
    viesWords = driver.find_element(By.CLASS_NAME, "recovery-phrase__footer--button")
    viesWords.click()
    # 助记词
    wordList = []  # 用于登录
    wordString = ""  # 用于保存到文件
    words = driver.find_elements(By.CLASS_NAME, "recovery-phrase__chip")

    for i in range(0, 12):
        wordList.append(words[i].text)
        wordString = wordString + words[i].text + ' '
    my_file.write(wordString + '\n')

    # 下一步
    next = driver.find_element(By.CLASS_NAME, "recovery-phrase__footer--button")
    next.click()
    # 填写助记词
    inputWords = driver.find_elements(By.CLASS_NAME, "recovery-phrase__chip--with-input")
    inputWords[0].find_element(By.TAG_NAME, "input").send_keys(wordList[2])
    inputWords[1].find_element(By.TAG_NAME, "input").send_keys(wordList[3])
    inputWords[2].find_element(By.TAG_NAME, "input").send_keys(wordList[7])
    time.sleep(1)
    # 完成
    ok = driver.find_element(By.CLASS_NAME, "recovery-phrase__footer__confirm--button")
    ok.click()

    # 知道了
    know = driver.find_element(By.CLASS_NAME, "btn-primary")
    know.click()

    # 下一步
    next = driver.find_element(By.CLASS_NAME, "btn-primary")
    next.click()

    # 完成
    complete = driver.find_element(By.CLASS_NAME, "btn-primary")
    complete.click()
    time.sleep(1)

    # 关闭弹窗
    driver.find_element(By.CSS_SELECTOR, ".popover-container .mm-box.mm-button-icon.mm-button-icon--size-sm.mm-box--display-inline-flex.mm-box--justify-content-center.mm-box--align-items-center.mm-box--color-icon-default.mm-box--background-color-transparent.mm-box--rounded-lg").click()
    time.sleep(1)

    driver.switch_to.window(driver.window_handles[-1])  # 切换到最新窗口
    time.sleep(1)
    driver.close()

my_file.close()