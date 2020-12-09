"""
2020/12/9
4:24 下午
name:bianer
project:test
"""

from selenium.webdriver import Chrome
import time
driver=Chrome('/usr/local/bin/chromedriver')
driver.get("https://www.baidu.com/")
time.sleep(10)
driver.quit()
