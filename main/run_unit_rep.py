import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
c='C:\\Users\\Administrator.AVIEGX0QQXBXQAV\\PycharmProjects\\untitled\\venv\\Lib\\site-packages\\'
sys.path.append(c)
master='{"branch":master,"version":a960016,"hash":a9600160c7aec9ae996bfabf61e475f643e8fe5c} '

import unittest
import time
from report.HTMLTestRunnerCN import HTMLTestReportCN
from report.get_version import get_v
import sys
import base.config
from report.dingding import send_ding
discover = unittest.defaultTestLoader.discover( '../main/', 'run_unit.py')

if __name__ == '__main__':
    v=get_v()
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    #filename = '../report/report.html'
    filename = '../report/' + now + 'result.html'  # 重构文件名
    with open(filename, 'wb') as f:
        runner = HTMLTestReportCN(stream=f,title=base.config.REPORT_TITLE, description=v,tester='小云')
        rep=runner.run(discover)
        report_str="通过："+str(rep.success_count)+", 失败："+str(rep.failure_count)+", 错误："+str(rep.error_count)
        print(report_str)
        send_ding(report_str)
    f.close()