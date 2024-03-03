import time
from Utils import init_web_driver, login_metatask_and_project
from selenium.webdriver.common.by import By
from Utils import waiting_dom_loaded, waitingDOM, userDataList

# 为每个账号新建space，并将账号profile地址输出到文件
profileUrlSavePath = r'D:\rich\pythonProject1\userData\profileUrl.txt'

spaceName = 'love starrynift 2'
spaceDescription = 'lucky for starrynift, waiting for good thing to happen forever 2'

my_file = open(profileUrlSavePath, "w")
for (n, user) in enumerate(userDataList):
    print('用户', n)
    currentEnvPath = user['webEnvPath']
    passWord = user['passWord']

    driver = init_web_driver(currentEnvPath)
    driver.get('chrome-extension://ogclokjhnpcoojbnkgilfopgoppgbjcb/home.html#unlock')
    waitingDOM(".unlock-page__mascot-container", driver).appear()
    driver.implicitly_wait(2)

    login_metatask_and_project(passWord, driver)

    # 点击头像进入my profile
    driver.find_element(By.CSS_SELECTOR, "._icon_box_9xb8y_14").click()
    driver.find_element(By.CSS_SELECTOR, "._op_menu_1cjdb_90 ._op_menu_one_1cjdb_94:nth-child(1)").click()
    driver.switch_to.window(driver.window_handles[-1])  # 切换当前窗口
    time.sleep(5)

    # 获取profile地址，输出到文件
    driver.find_element(By.CSS_SELECTOR, "._avator_box_1aejb_917").click()  # 使悬浮框失去焦点小时
    driver.find_element(By.CSS_SELECTOR, "._media_share_box_1aejb_977").click()
    profileUrl = driver.find_element(By.CSS_SELECTOR, "._link_1aejb_1038").text
    my_file.write(profileUrl + '\n')
    print("profile url", profileUrl)

    # 新建space
    driver.find_element(By.CSS_SELECTOR, "._addImg_1e4mr_95").click()  # 点击create space
    time.sleep(5)
    if waiting_dom_loaded("._space_img_c_qmo2t_58", driver) == 1:
        driver.find_element(By.CSS_SELECTOR, "._space_img_c_qmo2t_58").click()  # 点击图标创建
    time.sleep(5)
    if waiting_dom_loaded("._publish_fzb47_284 div:nth-child(2)", driver) == 1:
        driver.find_element(By.CSS_SELECTOR, "._publish_fzb47_284 div:nth-child(2)").click()  # 点击publish
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, "._inputField_1ciws_56").send_keys(spaceName)
    driver.find_element(By.CSS_SELECTOR, "._textareaField_1ciws_81").send_keys(spaceDescription)
    driver.find_element(By.CSS_SELECTOR, "._bottoms_1ciws_248 div:nth-child(2)").click()  # 点击确认launch

    time.sleep(5)
    if waiting_dom_loaded(".ant-btn.ant-btn-default._cneterBtn_k8sci_64", driver):
        driver.find_element(By.CSS_SELECTOR, ".ant-btn.ant-btn-default._cneterBtn_k8sci_64").click()  # 创建成功确认

    driver.close()
    driver.switch_to.window(driver.window_handles[-1])  # 切换当前窗口
    driver.close()

my_file.close()


