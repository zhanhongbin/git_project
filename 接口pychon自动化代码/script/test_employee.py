import logging
import unittest

from parameterized import parameterized

import app
from api.api_employee import Api_employee
from api.api_login import Api_LE
from until import Ass_Operating, d_file


class Test_Emyee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.login = Api_LE()
        cls.employee = Api_employee()
        cls.ass = Ass_Operating()


    @parameterized.expand(d_file(app.file_dqwj + "/data/emp.json","test01"))
    def test01_employee_login(self,account,status_code,success,code,message):
        # 登录
        response = self.login.login(account)
        app.token = response.json().get("data")
        logging.info(response.json())
        self.ass.asslogin(status_code,success,code,message,response,self)


    @parameterized.expand(d_file(app.file_dqwj + "/data/emp.json","test02"))
    def test02_employee_add(self,username,mobile,status_code, success, code, message):
        # 添加员工
        response = self.employee.employee_add(app.token,username,mobile)
        logging.info(response.json())
        self.ass.asslogin(status_code, success, code, message, response, self)


    @parameterized.expand(d_file(app.file_dqwj + "/data/emp.json","test03"))
    def test03_employee_Inquire(self,status_code, success, code, message):
        # 查询
        response = self.employee.employee_Inquire()
        logging.info(response.json())
        self.ass.asslogin(status_code, success, code, message, response, self)


    @parameterized.expand(d_file(app.file_dqwj + "/data/emp.json","test04"))
    def test04_employee_modify(self,username,status_code, success, code, message):
        # 修改
        response = self.employee.employee_modify(username)
        logging.info(response.json())
        self.ass.asslogin(status_code, success, code, message, response, self)


    @parameterized.expand(d_file(app.file_dqwj + "/data/emp.json","test05"))
    def test05_employee_delete(self,status_code, success, code, message):
        # 删除
        response = self.employee.employee_delete()
        logging.info(response.json())
        self.ass.asslogin(status_code, success, code, message, response, self)




















