from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from threading import Thread
from part_five.jingdong import jingdong


# 书写业务逻辑
def to_jingdong(name, server_address):
    print(name)
    driver = webdriver.Remote(command_executor=server_address,
                              desired_capabilities=DesiredCapabilities.CHROME)
    driver.maximize_window()
    jingdong.dell_start(driver)


my_address = {
    "windows": "http://localhost:4444/wd/hub"
}
threads = []
for name, url in my_address.items():
    t = Thread(target=to_jingdong,args=(name,url))
    threads.append(t)

for t in threads:
    t.start()
