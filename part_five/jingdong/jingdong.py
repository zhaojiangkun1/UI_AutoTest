from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import os
import json
from part_five.jingdong.my_cookies import *
from part_five.jingdong.my_mysql import *


# 登录功能
def login(driver):
    driver.get("https://www.jd.com")
    driver.find_element_by_class_name("link-login").click()
    driver.find_element_by_link_text("账户登录").click()
    driver.find_element_by_id("loginname").send_keys("16601258428")
    driver.find_element_by_id("nloginpwd").send_keys("123456qwert")
    driver.find_element_by_id("loginsubmit").click()

    # 要保存cookies到文件中
    save_cookies_to_file(driver)


def to_start(driver, name):
    # 要有一个循环来控制登录状态，判断登录是否成功
    try:
        loop_status = True
        while loop_status:
            # 检验cookies是否有效
            login_status = check_cookies(driver)
            if login_status:
                loop_status = False
            else:
                login(driver)
        # 跳转到商品信息页面
        to_goods_page(driver, name)
    finally:
        time.sleep(3)
        driver.quit()


def dell_start(driver):
    to_start(driver,"dell")