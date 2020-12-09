import pytest

import os
pytest.main(['--alluredir=testresult/test_report',
            '--reruns','3',
            '--reruns-delay','2'])
os.system("allure serve testresult/test_report")