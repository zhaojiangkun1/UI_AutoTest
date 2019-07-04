from selenium import webdriver
import os
import json

path = "D:\Python3.6/chromedriver"
driver = webdriver.Chrome(path)
driver.maximize_window()


def save_cookies():
    project_path = os.path.dirname(os.getcwd())
    file_path = project_path + "/shuzu_cookies/"
    if not os.path.exists(file_path):
        os.mkdir(file_path)
    cookies = driver.get_cookies()
    laravel_session_shuzupos = driver.get_cookie("laravel_session_shuzupos")
    with open(file_path+"jd.cookies","w") as c:
        json.dump(cookies,c)
    print(cookies)
    print(laravel_session_shuzupos)


def login():
    driver.get("http://112.74.173.171:8082/login")
    driver.find_element_by_xpath("//*[@id=\"merchantForm\"]/form/div[1]/input").send_keys("shuzu.sysadmin")
    driver.find_element_by_xpath("//*[@id=\"merchantForm\"]/form/div[2]/input").send_keys("shuzu123")
    driver.find_element_by_id("verifycodeInput").send_keys("autotest")
    driver.find_element_by_class_name("login_btn").click()
    save_cookies()


def get_url_with_cookies():
    project_path = os.path.dirname(os.getcwd())
    file_path = project_path + "/shuzu_cookies/"
    jd_cookies_file = file_path + "jd.cookies"
    jd_cookies_str = open(jd_cookies_file, "r").readline()
    jd_cookies_dict = json.loads(jd_cookies_str)

    driver.get("http://112.74.173.171:8082/login")
    driver.delete_all_cookies()
    # driver.add_cookie(jd_cookies_dict)
    for cookie in jd_cookies_dict:
        print(cookie)
        driver.add_cookie(cookie)
    driver.get("http://112.74.173.171:8082/version/manage")


if __name__ == "__main__":
    login()
    # get_url_with_cookies()
