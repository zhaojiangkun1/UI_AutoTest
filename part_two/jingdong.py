from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import json
import os
import time

# 启动浏览器
path = "D:\Python3.6/chromedriver"
driver = webdriver.Chrome(path)
driver.maximize_window()


# 登录功能
def login():
    driver.get("https://www.jd.com")
    driver.find_element_by_class_name("link-login").click()
    driver.find_element_by_link_text("账户登录").click()
    driver.find_element_by_id("loginname").send_keys("13701476279")
    driver.find_element_by_id("nloginpwd").send_keys("agf1992zhao")
    driver.find_element_by_id("loginsubmit").click()

    # 登录成功之后，保存cookies信息到文件中
    save_cookies_to_files(driver)


def save_cookies_to_files(driver):
    # 获取保存cookies信息的路径
    file_path = get_cookies_dir()
    # 获取cookies
    cookies = driver.get_cookies()
    # 存储cookies信息到文件中
    with open(file_path + "jd.cookies","w") as c:
        json.dump(cookies,c)


def get_cookies_dir():
    project_path = os.path.dirname(os.getcwd())
    file_path = project_path + "/cookies/"
    if not os.path.exists(file_path):
        os.mkdir(file_path)
    return file_path


def check_cookies():
    # 设置一个登录状态，初始值为未登录
    login_status = False
    # 将cookies信息保存到driver中，实际上是将cookies信息添加到新的链接中
    driver = save_cookies_to_driver()

    # 跳转链接的检测
    driver.get("https://order.jd.com/center/list.action")
    current_url = driver.current_url
    if current_url == "https://order.jd.com/center/list.action":
        login_status = True
        return login_status
    else:
        return login_status


# 保存cookies信息到driver中
def save_cookies_to_driver():
    # 先获取已保存的cookies信息
    cookies_file = get_cookies_file()
    # 打开cookies文件
    jd_cookies_file = open(cookies_file, "r")
    # 读取cookies文件
    jd_cookies_str = jd_cookies_file.readline()
    jd_cookies_dict = json.loads(jd_cookies_str)
    # 清除以前的cookies信息
    driver.get("https://www.jd.com")
    driver.delete_all_cookies()

    for cookie in jd_cookies_dict:
        driver.add_cookie(cookie)
    return driver


def get_cookies_file():
    return get_cookies_dir() + "jd.cookies"


def to_goods_page():
    # 首先把页面放到首页上
    driver.get("https://www.jd.com")
    # 定位到电脑上
    computer_element = driver.find_element_by_link_text("电脑")
    # 鼠标悬停
    ActionChains(driver).move_to_element(computer_element).perform()
    time.sleep(2)
    # 选择笔记本
    driver.find_element_by_link_text("笔记本").click()
    # 此时已经打开第二个页面，切换句柄
    handles = driver.window_handles
    # 获取当前url
    index_handle = driver.current_url
    for handle in handles:
        if handle != index_handle:
            driver.switch_to.window(handle)
    # 点击thinkPad
    driver.find_element_by_xpath("//*[@id=\"brand-11518\"]/a/img").click()
    # 点击7000以上
    driver.find_element_by_xpath("//*[@id=\"J_selectorPrice\"]/div/div[2]/div/ul/li[7]/a").click()
    # 点击评论数
    driver.find_element_by_xpath("//*[@id=\"J_filter\"]/div[1]/div[1]/a[3]").click()
    # 点击第一款电脑
    driver.find_element_by_xpath("//*[@id=\"plist\"]/ul/li[1]/div/div[1]/a/img").click()
    # 切换句柄
    notebook_handler = driver.current_window_handle
    # 重新获取所有句柄，此时已经有三个窗口了
    handles = driver.window_handles
    for handle in handles:
        if handle != index_handle and handle != notebook_handler:
            driver.switch_to.window(handle)
    # 屏幕往下滚动
    js = "window.scrollTo(0,1500)"
    driver.execute_script(js)
    # 点击规格与包装
    driver.find_element_by_xpath("//*[@id=\"detail\"]/div[1]/ul/li[2]").click()
    # 解析所有标签
    info_elements = driver.find_elements_by_class_name("Ptable-item")

    # 用一个list存储最终的结果
    return_list = []
    # 标签一个个解析
    for info_element in info_elements:
        info_element_dict = get_info_element_dict(info_element)
        return_list.append(info_element_dict)
    # 保存这些信息到文件中
    save_goods_info(return_list)


def get_info_element_dict(info_element):
    # 拿到第一列的信息
    computer_part = info_element.find_element_by_tag_name("h3")
    # 计算机信息中的key值
    computer_info_keys = info_element.find_elements_by_tag_name("dt")
    # 计算机信息中的value值
    computer_info_values = info_element.find_element_by_xpath("dl//dd[not(contains(@class,'Ptable-tips'))]")

    # 存储计算机信息中的key和value
    key_and_value_dict = {}

    # 存储所有的计算机组成信息
    parts_dict = {}

    for i in range(len(computer_info_keys)):
        key_and_value_dict[computer_info_keys[i].text] = computer_info_values[i].text

    parts_dict[computer_part.text] = key_and_value_dict

    return parts_dict


def save_goods_info(info_list):
    project_path = os.path.dirname(os.getcwd())
    file_path = project_path + "/goods_infos/"
    if not os.path.exists(file_path):
        os.mkdir(file_path)

    with open(file_path+"computer.infos", "a", encoding="utf-8") as f:
        f.write(str(info_list))
        print(str(info_list))


if __name__ == "__main__":
    # 需要一个循环来控制登录状态，判断是否登录成功
    # try:
    #     loop_status = True
    #     while loop_status:
    #         # 检验cookies是否生效
    #         login_status = check_cookies()
    #         if login_status:
    #             loop_status = False
    #         else:
    #             login()
        # 跳转到商品信息页面
    login()
    to_goods_page()
    # finally:
    time.sleep(3)
    driver.quit()
