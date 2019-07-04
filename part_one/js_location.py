from selenium import webdriver
import time

try:
    path = "D:\Python3.6/chromedriver"
    driver = webdriver.Chrome(path)
    driver.maximize_window()

    driver.get("https://www.12306.cn/index/")
    from_element = driver.find_element_by_id("fromStationText")
    # 此处必须停留2秒，否则报错
    time.sleep(2)
    from_element.click()
    time.sleep(2)
    from_element.send_keys("北京")
    time.sleep(2)
    # 输入北京，选择北京北的两种方式；第二种是鼠标放在北京北上，右击，检查元素
    # driver.find_element_by_xpath("//*[text()='北京北']").click()
    driver.find_element_by_xpath("//*[@id=\"citem_0\"]/span[1]").click()

    to_element = driver.find_element_by_id("toStationText")
    to_element.click()
    time.sleep(2)
    to_element.send_keys("长春")
    driver.find_element_by_xpath("//*[text()='长春南']").click()

    # 定位出发日期，去掉readonly属性
    js = "$('input[id=train_date]').removeAttr('readonly')"
    driver.execute_script(js)
    date_element = driver.find_element_by_id("train_date")
    date_element.click()
    time.sleep(2)
    date_element.clear()
    date_element.send_keys("2019-06-30")
    driver.find_element_by_class_name("form-label").click()
    driver.find_element_by_id("search_one").click()
finally:
    time.sleep(3)

