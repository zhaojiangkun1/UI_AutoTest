from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from threading import Thread


# 书写业务逻辑
def to_baidu(name, server_address):
    print(name)
    driver = webdriver.Remote(command_executor=server_address,
                              desired_capabilities=DesiredCapabilities.CHROME)
    driver.maximize_window()
    driver.get("https://www.jd.com")


my_address = {
    "windows": "http://localhost:4444/wd/hub"
}
threads = []
for name, url in my_address.items():
    t = Thread(target=to_baidu,args=(name,url))
    threads.append(t)

for t in threads:
    t.start()
