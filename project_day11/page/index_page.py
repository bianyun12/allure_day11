from selenium.webdriver.common.by import By


class index_page_class(object):
    def __init__(self,driver):
        self.driver=driver
    def is_login(self):
        try:
            ele = self.driver.find_element(By.XPATH, '//a[contains(text(),"我的帐户")]')
        except:
            return False
        else:
            return True

    def click_quit(self):
        self.driver.find_element(By.XPATH,"//a[text()='退出']").click()