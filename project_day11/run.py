import pytest

import os

pytest.main(['--alluredir=testresult/test_report'])
# os.system("allure serve testresult/test_report")
