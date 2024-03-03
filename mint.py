import time
from Utils import init_web_driver, login_metatask_and_project
from selenium.webdriver.common.by import By
from Utils import waitingDOM, userDataList


for (n, user) in enumerate(userDataList):
    currentEnvPath = user['webEnvPath']
    passWord = user['passWord']

    driver = init_web_driver(currentEnvPath)
    driver.get('chrome-extension://ogclokjhnpcoojbnkgilfopgoppgbjcb/home.html#unlock')
    waitingDOM(".unlock-page__mascot-container", driver).appear()
    driver.implicitly_wait(2)

    login_metatask_and_project(passWord, driver)

    # 点击citizen
    driver.find_element(By.CSS_SELECTOR, "._nav_list_box_dgei9_55 ._nav_one_dgei9_79:nth-child(4) ._menu_base_name_dgei9_93").click()
    # 点击mint
    driver.find_element(By.CSS_SELECTOR, "._mint_words_sd0u4_135").click()

    driver.switch_to.window(driver.window_handles[-1])  # 跳转到最新的句柄
    # 小狐狸弹窗点击确定
    try:  # 仅第一次mint需要确定
        driver.find_element(By.CSS_SELECTOR, ".button.btn--rounded.btn-primary.page-container__footer-button").click()
    except:
        time.sleep(0)

    driver.close() # 关闭项目
    driver.switch_to.window(driver.window_handles[-1])  # 跳转到最新的句柄
    driver.close() # 关闭小狐狸