from selenium.webdriver import Chrome
import unittest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from unittestreport import ddt,list_data
from case_datas import casedatas
from page.login_page import login_page_class
from page.index_page import index_page_class
from handle_func.handle_log import log

import pytest



class Test_login_class:

    @pytest.mark.parametrize('case',casedatas.login_data_pass)
    def test_login_is_pass(self,case,setup_login):
        login,index=setup_login
        login.login_click(case['phone'],case['password'])
        res=index.is_login()
        try:
            assert res
        except AssertionError as e:
            log.error("用例---{}--执行失败".format(case['title']))
            log.exception(e)
            raise e
        else:
            log.info("用例执行成功")
        index.click_quit()
    @pytest.mark.parametrize('case',casedatas.login_data_is_none)
    def test_login_is_none(self,case,setup_login):
        login,index=setup_login
        login.reset_login()
        login.login_click(case['phone'],case['password'])
        res=login.get_page_error_info()
        try:
            assert case['expected']==res
        except AssertionError as e:
            log.error("用例---{}---执行失败".format(case['title']))
            log.exception(e)
            raise e
        else:
            log.info("用例执行成功")

    @pytest.mark.parametrize('case',casedatas.login_toast_is_error)
    def test_login_toast_error(self,case,setup_login):
        login,index=setup_login
        login.reset_login()
        login.login_click(case['phone'],case['password'])
        res=login.get_page_toast_info()
        try:

            assert case['expected']==res
        except AssertionError as e:
            log.error("用例--{}--执行失败".format(case['title']))
            log.exception(e)
            raise e
        else:
            log.info("用例执行成功")

