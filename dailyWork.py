import time
from Utils import init_web_driver, confirm_signature, login_metatask_and_project
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Utils import is_dom_exist, waiting_dom_loaded_space_only, confirm_wallet_connect, waitingDOM, userDataList

#问候语
GM_string = "GM"

for (n, user) in enumerate(userDataList):
    print(f'开启一个用户任务-{n}')

    currentEnvPath = user['webEnvPath']
    passWord = user['passWord']

    driver = init_web_driver(currentEnvPath)
    driver.implicitly_wait(2)
    driver.get('chrome-extension://ogclokjhnpcoojbnkgilfopgoppgbjcb/home.html#unlock')
    waitingDOM(".unlock-page__mascot-container", driver).appear()

    login_metatask_and_project(passWord, driver)  # 登录小狐狸 + 打开项目链接小狐狸

    time.sleep(5)
    driver.switch_to.window(driver.window_handles[-1])
    time.sleep(5)
    # 点击earn切换到任务界面
    driver.find_element(By.CSS_SELECTOR, "._nav_list_box_dgei9_55 ._nav_one_dgei9_79:nth-child(6) ._menu_base_name_dgei9_93").click()
    # 判断项目页面是否弹出请求链接钱包窗口
    confirm_wallet_connect(driver)
    waitingDOM("g[clip-path]", driver).disappear()
    waitingDOM("._avator_box_leayb_18", driver).appear()

    # 任务1：daily Streak，每次需要花钱，
    # 如果按钮没有被禁用，就去点击connect并小狐狸确认付费，禁用了就跳过
    # if (is_dom_exist('.ant-btn.ant-btn-default._history_btn_hjp5v_70._disabled_hjp5v_95', driver) == 0):
    #     driver.find_element(By.CSS_SELECTOR, ".ant-btn.ant-btn-default._history_btn_hjp5v_70").click()
    #     # 确认付gas费,有可能小狐狸页面直接弹窗确认，也可能新弹出窗口确认
    #     try:  # 小狐狸页面确认尝试
    #         driver.switch_to.window(driver.window_handles[0])
    #         if is_dom_exist(".button.btn--rounded.btn-primary.page-container__footer-button", driver):
    #             driver.find_element(By.CSS_SELECTOR, ".button.btn--rounded.btn-primary.page-container__footer-button").click()
    #     except:
    #         time.sleep(0)
    #     try:  # 新窗口确认尝试
    #         driver.switch_to.window(driver.window_handles[-1])
    #         time.sleep(1)
    #         if is_dom_exist(".button.btn--rounded.btn-primary.page-container__footer-button", driver):
    #             driver.find_element(By.CSS_SELECTOR, ".button.btn--rounded.btn-primary.page-container__footer-button").click()
    #     except:
    #         time.sleep(0)

    time.sleep(5)
    driver.switch_to.window(driver.window_handles[-1])  # 切换当前窗口
    time.sleep(1)

    # 任务2：访问至少5个陌生人的space 通过window.open新打开标签
    driver.execute_script("window.open('https://app.starrynift.art/personal-space', '_blank')")
    time.sleep(5)
    driver.switch_to.window(driver.window_handles[-1])  # 切换当前窗口
    time.sleep(1)
    for i in range(5):
        waitingDOM("._starry_line_1qn8z_24", driver).appear()
        # 点击第i个space
        driver.find_element(By.CSS_SELECTOR, f"._right_list_1qn8z_194 ._st_listOne_user_1rauv_1._st_listOne_user_big_1rauv_128:nth-child({i + 1}) ._banner_ab_1rauv_46").click()
        waitingDOM("g[clip-path]", driver).disappear()
        # 判断是否弹出链接钱包请求-偶尔弹出提醒
        if is_dom_exist('.button.btn--rounded.btn-primary.page-container__footer-button', driver) == 1:
            time.sleep(5)
            driver.switch_to.window(driver.window_handles[-1])  # 切换当前窗口
            time.sleep(1)
            waitingDOM(".button.btn--rounded.btn-primary.page-container__footer-button", driver).appear()
            driver.find_element(By.CSS_SELECTOR, ".button.btn--rounded.btn-primary.page-container__footer-button").click()

        time.sleep(5)
        driver.switch_to.window(driver.window_handles[-1])  # 切换当前窗口
        time.sleep(1)
        # space留言
        input_box = driver.find_element(By.CSS_SELECTOR, ".ant-input._sendMsgInput_1uiql_160")
        input_box.send_keys(GM_string)
        input_box.send_keys(Keys.ENTER)
        time.sleep(1)
        driver.back()
    driver.close()
    driver.switch_to.window(driver.window_handles[-1])
    time.sleep(1)

    #  任务3：公共space发送GM问候,1个即可，这里设置为2个
    # 点击community切换到公共空间菜单，公共空间不新开标签
    driver.find_element(By.CSS_SELECTOR, "._nav_list_box_dgei9_55 ._nav_one_dgei9_79:nth-child(3) ._menu_base_name_dgei9_93").click()
    for s in range(2):
        waitingDOM("._cmy_title_g4uug_69", driver).appear()
        js = f"document.querySelector('._list_g4uug_31 ._sceneListItem_5157t_1:nth-child({s+1}) ._img_center_5157t_25').click()"
        time.sleep(1)
        driver.execute_script(js)  # 点击个人profile里面的一个space不新开标签
        time.sleep(1)
        waitingDOM("g[clip-path]", driver).disappear()
        waitingDOM("._chat_avatar_1uiql_420", driver).appear()

        # 判断是否打开小狐狸签名确认窗口
        confirm_signature(driver)

        input_box = driver.find_element(By.CSS_SELECTOR, ".ant-input._sendMsgInput_1uiql_160")
        input_box.send_keys(GM_string)
        input_box.send_keys(Keys.ENTER)
        time.sleep(1)
        driver.back()

    # 任务4：关注自己其他账号 + 任务3：邀请别人访问自己的space，这里改成访问自己其他账号的space
    for usr in userDataList:
        if usr['webEnvPath'] == currentEnvPath:  # 如果是本用户访问自己，则直接下一次循环
            continue

        profile_url = usr['profileUrl']
        driver.execute_script(f'window.open("{profile_url}")')
        time.sleep(5)
        driver.switch_to.window(driver.window_handles[-1])  # 切换到最新窗口
        time.sleep(1)

        waitingDOM("g[clip-path]", driver).disappear()
        waitingDOM("._avator_box_1aejb_917", driver).appear()

        # 判断是否打开小狐狸签名确认窗口
        confirm_signature(driver)

        # 如果没关注，则关注之
        if driver.find_element(By.CSS_SELECTOR, "._mine_box_r_1aejb_952 ._word_1aejb_670").text == "Follow":
            driver.find_element(By.CSS_SELECTOR, "._mine_box_r_1aejb_952 ._word_1aejb_670").click()

        # 看有没有发表的space，有则浏览之
        spaces_for_user = driver.find_elements(By.CSS_SELECTOR, "._banner_ab_qkcwk_391")
        print("被访问用户的space数量", len(spaces_for_user))
        for spaceIndex in range(min(len(spaces_for_user), 1)):
            waitingDOM("g[clip-path]", driver).disappear()
            time.sleep(1)
            driver.find_element(By.CSS_SELECTOR, f"._cz_one_my_1e4mr_115:nth-child({spaceIndex+1}) ._banner_ab_qkcwk_391").click()  # 进入某个space,有个bug，有时报链接失败，自动跳转到一个没见过的页面
            waiting_dom_loaded_space_only("._chat_avatar_1uiql_420", driver)
            # 判断是否打开小狐狸签名确认窗口
            confirm_signature(driver)
            # 点赞
            driver.find_element(By.CSS_SELECTOR, "._shareTip_mg1wp_1._shareTipLike_mg1wp_52").click()
            # space留言
            input_box = driver.find_element(By.CSS_SELECTOR, ".ant-input._sendMsgInput_1uiql_160")
            input_box.send_keys(GM_string)
            input_box.send_keys(Keys.ENTER)
            driver.back()
        driver.close()
        time.sleep(5)
        driver.switch_to.window(driver.window_handles[-1])  # 切换到最新窗口
        time.sleep(1)

    driver.close()
    driver.switch_to.window(driver.window_handles[-1])  # 切换到最新窗口
    time.sleep(5)
    driver.close()

print('程序正常结束')
time.sleep(100)
