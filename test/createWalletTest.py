import time

from Utils import init_web_driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# 创建 WebDriver 对象，指明使用chrome浏览器驱动
driver = init_web_driver(r'D:\rich\pythonProject1\webEnv100\1')

driver.get('chrome-extension://ogclokjhnpcoojbnkgilfopgoppgbjcb/home.html')

#等待加载
driver.implicitly_wait(5)
#点击同意
aggregate = driver.find_element(By.ID, "onboarding__terms-checkbox")
aggregate.click()
driver.implicitly_wait(5)
#点击创建
createButton = driver.find_element(By.CLASS_NAME, "btn-primary")
createButton.click()
driver.implicitly_wait(5)
#点击我同意
iAggregate = driver.find_element(By.CLASS_NAME, "btn-primary")
iAggregate.click()
driver.implicitly_wait(5)
#输入密码
password = driver.find_elements(By.CLASS_NAME, "form-field__input")
password[0].send_keys("qwer1234!@#$")
password[1].send_keys("qwer1234!@#$")
driver.implicitly_wait(5)
#我明白
iUnderstand = driver.find_element(By.CLASS_NAME, "check-box")
iUnderstand.click()
driver.implicitly_wait(5)
#创建钱包
createAccount = driver.find_element(By.CLASS_NAME, "create-password__form--submit-button")
createAccount.click()
driver.implicitly_wait(5)
#保护钱包
defectAccount = driver.find_element(By.CLASS_NAME, "mm-button-primary")
defectAccount.click()
driver.implicitly_wait(5)
#显示助记词
viesWords = driver.find_element(By.CLASS_NAME, "recovery-phrase__footer--button")
viesWords.click()
driver.implicitly_wait(5)
#助记词
wordList = []
wordString = ""
words = driver.find_elements(By.CLASS_NAME, "recovery-phrase__chip")

for i in range(0, 12):
    wordList.append(words[i].text)
    wordString = wordString + words[i].text + ' '
my_file = open("wordList.txt", "w")
my_file.write(wordString + '\n')
my_file.write("结尾行")
my_file.close()
#下一步
next = driver.find_element(By.CLASS_NAME, "recovery-phrase__footer--button")
next.click()
driver.implicitly_wait(5)
#填写助记词
inputWords = driver.find_elements(By.CLASS_NAME, "recovery-phrase__chip--with-input")
inputWords[0].find_element(By.TAG_NAME, "input").send_keys(wordList[2])
inputWords[1].find_element(By.TAG_NAME, "input").send_keys(wordList[3])
inputWords[2].find_element(By.TAG_NAME, "input").send_keys(wordList[7])
time.sleep(1)
#完成
ok = driver.find_element(By.CLASS_NAME, "recovery-phrase__footer__confirm--button")
ok.click()
driver.implicitly_wait(5)

#知道了
know = driver.find_element(By.CLASS_NAME, "btn-primary")
know.click()
driver.implicitly_wait(5)

#下一步
next = driver.find_element(By.CLASS_NAME, "btn-primary")
next.click()
driver.implicitly_wait(5)

#完成
complete = driver.find_element(By.CLASS_NAME, "btn-primary")
complete.click()
driver.implicitly_wait(5)

#最新动态
#close = driver.find_element(By.CSS_SELECTOR, "[class = 'mm-box mm-button-icon mm-button-icon--size-sm mm-box--display-inline-flex mm-box--justify-content-center mm-box--align-items-center mm-box--color-icon-default mm-box--background-color-transparent mm-box--rounded-lg']")
close = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[class = 'mm-box mm-button-icon mm-button-icon--size-sm mm-box--display-inline-flex mm-box--justify-content-center mm-box--align-items-center mm-box--color-icon-default mm-box--background-color-transparent mm-box--rounded-lg']")))
close.click()
driver.implicitly_wait(5)

time.sleep(10)
# 调用WebDriver 对象的get方法 可以让浏览器打开指定网址
#driver.get('https://app.starrynift.art/')





# 等待组件加载完成,最长等待100s，没0.5秒检测一次
# wait = WebDriverWait(driver, 100, 0.5)
# element = wait.until(EC.presence_of_element_located((By.ID, "su")))
# print(element.get_attribute("value"))
# kw1 = driver.find_element(By.ID, 'kw')
# kw1.send_keys("测试")
# print(kw1.get_property("value"))
# kw2 = driver.find_element(By.ID, 'content_left')
# kw3 = kw2.find_elements(By.CLASS_NAME, 'title-contanier_RY4Rg')
# kw3.pop().click()
# element.click()


# 程序运行完会自动关闭浏览器，就是很多人说的闪退
# 这里加入等待用户输入，防止闪退
input('等待回车键结束程序')
