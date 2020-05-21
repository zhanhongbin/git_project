import HTMLTestRunner_PY3

import app
import unittest

from script.test_employee import Test_Emyee
from script.test_login import Login_T

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(Test_Emyee))
suite.addTest(unittest.makeSuite(Login_T))

file_log = app.file_dqwj + "/report/report.html"

with  open(file_log,"wb") as f:
    runner = HTMLTestRunner_PY3.HTMLTestRunner(f,verbosity=2,title="登录员工管理接口",description="ihrm接口")
    runner.run(suite)



































