# 1.导包
import time
import unittest
from HTMLTestRunner import HTMLTestRunner

from utils import DriverUtils


# 关闭关闭浏览器的开关
DriverUtils.change_key(True)

# 2.组织测试用例(测试套件、测试加载器)
suite = unittest.TestLoader().discover("../script", pattern="test*.py")
# 3.定义测试报告的路径
report_file = "../report/test-{}.html".format(time.strftime("%Y%m%d%H%M%S"))

# 4.打开测试报告
with open(report_file, 'wb') as f:
    # 5.创建HTMLTestRunner的对象
    run_report = HTMLTestRunner(stream=f, title="tpshop", description="chrome")
    # 6.运行测试用例
    run_report.run(suite)

# 打开关闭浏览器的开关
DriverUtils.change_key(False)
# 调用关闭浏览器驱动的方法
DriverUtils.quit_driver()