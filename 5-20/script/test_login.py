import logging
from parameterized import parameterized
from api.api_login import Api_LE
import unittest
import app
from until import Ass_Operating, j_file


class Login_T(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.login_api = Api_LE()
        cls.asslog = Ass_Operating()

    def setUp(self):
        ...

    def tearDown(self):
        ...

    @parameterized.expand(j_file(app.file_dqwj + "/data/newfile.json"))
    def test01_login(self, name, status, success, code, message, logging_01):
        response = self.login_api.login(name)
        logging.info(logging_01)
        logging.info(response.json())
        logging.info(name)
        self.asslog.asslogin(status, success, code, message, response, self)



