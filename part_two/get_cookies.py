from selenium import webdriver
import os
import json

path = "D:\Python3.6/chromedriver"
driver = webdriver.Chrome(path)
driver.maximize_window()


def get_url_with_cookies():
    # 读取cookies
    project_path = os.path.dirname(os.getcwd())
    file_path = project_path + "/cookies/"

    jd_cookies_file = open(file_path+"jd.cookies", "r")
    jd_cookies_str = jd_cookies_file.readline()
    jd_cookies_dict = json.loads(jd_cookies_str)

    driver.get("https://www.jd.com")
    driver.delete_all_cookies()
    for cookie in jd_cookies_dict:
        print(cookie)
        # driver.add_cookie(cookie)
    driver.get("https://order.jd.com/center/list.action")


def save_cookies():
    project_path = os.path.dirname(os.getcwd())
    file_path = project_path + "/cookies/"
    if not os.path.exists(file_path):
        os.mkdir(file_path)
    cookies = driver.get_cookies()
    dev_cookie = driver.get_cookie("DeviceSeq")
    # expiry_cookie = driver.get_cookie("expiry")
    # httpOnly_cookie = driver.get_cookie("httpOnly")
    with open(file_path+"jd.cookies","w") as c:
        json.dump(cookies,c)
    print(cookies)
    print(dev_cookie)
    # print(expiry_cookie)
    # print(httpOnly_cookie)


def login():
    driver.get("https://www.jd.com")
    driver.find_element_by_class_name("link-login").click()
    driver.find_element_by_link_text("账户登录").click()
    account_element = driver.find_element_by_id("loginname")
    account_element.send_keys("13701476279")
    pwd_element = driver.find_element_by_id("nloginpwd")
    pwd_element.send_keys("agf1992zhao")
    driver.find_element_by_id("loginsubmit").click()
    save_cookies()


if __name__ == "__main__":
    # login()
    get_url_with_cookies()

