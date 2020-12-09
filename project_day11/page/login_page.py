from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from case_datas import casedatas
class login_page_class(object):
    input_phone_located=(By.XPATH, '//input[@name="phone"]')
    input_pwd_located=(By.XPATH, '//input[@name="password"]')
    button_login_located=(By.XPATH, '//button[text()="登录"]')
    page_error_info=(By.XPATH, '//div[@class="form-error-info"]')
    toast_error_info=(By.XPATH, '//div[@class="layui-layer-content"]')
    def __init__(self,driver):
        self.driver=driver
    def login_click(self,mobile,pwd):
        phone_input=self.driver.find_element(*self.input_phone_located)
        phone_input.clear()
        phone_input.send_keys(mobile)

        pwd_input=self.driver.find_element(*self.input_pwd_located)
        pwd_input.clear()
        pwd_input.send_keys(pwd)
        self.driver.find_element(*self.button_login_located).click()
    def get_page_error_info(self):
        result = self.driver.find_element(*self.page_error_info).text
        return result
    def get_page_toast_info(self):
        WebDriverWait(self.driver, 15, 0.5).until(
            EC.visibility_of_element_located(self.toast_error_info))
        result = self.driver.find_element(*self.toast_error_info).text
        return result
    def reset_login(self):
        self.driver.get("http://120.78.128.25:8765/Index/login.html")


