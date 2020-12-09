import os
# 获取当前文件的根目录
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CASE_DIR=os.path.join(BASE_DIR,'test_case')
REPORT_DIR=os.path.join(BASE_DIR,'testresult/test_report')
LOG_DIR=os.path.join(BASE_DIR,'testresult/test_log')
IMG_DIR=os.path.join(BASE_DIR,'testresult/test_img')
DATA_DIR=os.path.join(BASE_DIR,'case_datas')
CONF_DIR=os.path.join(BASE_DIR,'conf')



