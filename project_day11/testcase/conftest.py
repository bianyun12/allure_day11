import pytest
from selenium import webdriver
from selenium.webdriver import Chrome
from page.index_page import index_page_class
from page.login_page import login_page_class
from handle_func.handle_config import conf

def create_option():
    if conf.getboolean('run','headless'):
        options=webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        driver=webdriver.Chrome(options=options)
    else:
        driver=Chrome()
    return driver

@pytest.fixture(scope='class')
def setup_login():
    driver=create_option()
    driver.get("http://120.78.128.25:8765/Index/login.html")
    driver.implicitly_wait(10)
    login =login_page_class(driver)
    index =index_page_class(driver)
    yield login,index
    driver.quit()