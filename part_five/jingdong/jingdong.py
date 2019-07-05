from selenium.webdriver.common.action_chains import ActionChains
import time
from part_five.jingdong.my_cookies import *
from part_five.jingdong.my_mysql import *


# 登录功能
def login(driver):
    driver.get("https://www.jd.com")
    driver.find_element_by_class_name("link-login").click()
    driver.find_element_by_link_text("账户登录").click()
    driver.find_element_by_id("loginname").send_keys("13701476279")
    driver.find_element_by_id("nloginpwd").send_keys("agf1992zhao")
    driver.find_element_by_id("loginsubmit").click()

    # 要保存cookies到文件中
    save_cookies_to_file(driver)


def to_goods_page(driver, name):
    # 把页面放在首页上
    driver.get("https://www.jd.com")
    # 定位到电脑上
    computer_element = driver.find_element_by_xpath("//*[@id=\"J_cate\"]/ul/li[3]/a[1]")
    # 鼠标悬停在电脑上
    ActionChains(driver).move_to_element(computer_element).perform()
    # 点击笔记本
    time.sleep(2)
    driver.find_element_by_link_text("笔记本").click()
    # 切换句柄
    handles = driver.window_handles
    index_handle = driver.current_url
    for handle in handles:
        if handle != index_handle:
            driver.switch_to.window(handle)

    if name == "thinkspad":
        # 点击thinkpad
        driver.find_element_by_xpath("//*[@id=\"brand-11518\"]/a/img").click()
    if name == "dell":
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id=\"brand-5821\"]/a").click()

    # 点击7000以上
    time.sleep(2)
    driver.find_element_by_xpath("//*[@id=\"J_selectorPrice\"]/div/div[2]/div/ul/li[7]/a").click()
    # 点击评论数
    time.sleep(2)
    driver.find_element_by_xpath("//*[@id=\"J_filter\"]/div[1]/div[1]/a[3]").click()
    # 点击第一款电脑
    time.sleep(2)
    driver.find_element_by_xpath("//*[@id=\"plist\"]/ul/li[1]/div/div[1]/a/img").click()
    # 切换句柄
    notebook_handler = driver.current_window_handle
    # 重新获取句柄，已经有3个窗口了
    handles = driver.window_handles
    for handle in handles:
        if handle != index_handle and handle != notebook_handler:
            driver.switch_to.window(handle)
    time.sleep(2)
    js = "window.scrollTo(0,1500)"
    driver.execute_script(js)
    time.sleep(3)
    # 点击规格与包装
    driver.find_element_by_xpath("//*[@id=\"detail\"]/div[1]/ul/li[2]").click()
    time.sleep(3)
    # 解除所有标签
    info_elements = driver.find_elements_by_class_name("Ptable-item")
    time.sleep(2)
    # 一个list存储最终的结果
    result_list = []
    # 标签一个一个解析
    for info_element in info_elements:
        info_element_dict = get_info_element_dict(info_element)
        result_list.append(info_element_dict)
    # 保存这些信息到文件中
    print(result_list)
    save_goods_info_to_mysql(result_list)


def get_info_element_dict(info_element):
    # 拿到第一列的信息
    computer_part = info_element.find_element_by_tag_name("h3")
    # 计算机信息中的key值
    computer_info_keys = info_element.find_elements_by_tag_name("dt")
    # 计算机信息中的values值
    computer_info_values = info_element.find_elements_by_xpath("dl//dd[not(contains(@class,'Ptable-tips'))]")
    # 存储计算机信息中key和value
    key_and_value_dict = {}

    # 存储所有的计算机组成信息
    parts_dict = {}

    for i in range(len(computer_info_keys)):
        key_and_value_dict[computer_info_keys[i].text] = computer_info_values[i].text
        parts_dict[computer_part.text] = key_and_value_dict
        return parts_dict


def to_start(driver, name):
    try:
        login(driver)
        to_goods_page(driver, name)
    finally:
        time.sleep(3)
        driver.quit()
    # 要有一个循环来控制登录状态，判断登录是否成功
    # try:
    #     loop_status = True
    #     while loop_status:
    #         # 检验cookies是否有效
    #         login_status = check_cookies(driver)
    #         if login_status:
    #             loop_status = False
    #         else:
    #             login(driver)
    #     # 跳转到商品信息页面
    #     to_goods_page(driver, name)
    # finally:
    #     time.sleep(3)
    #     driver.quit()


def dell_start(driver):
    to_start(driver, "dell")

#
# def thinkpad_start(driver):
#     to_start(driver, "thinkpad")
