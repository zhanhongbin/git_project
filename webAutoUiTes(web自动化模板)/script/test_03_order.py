"""
测试用例：
1.定义测试类，记得继承unittest.TestCase
2.定义类级别的初始化方法
3.在类级别的初始化方法中定义一个cls.driver实例属性，用来创建的获取浏览器驱动对象
4.在类级别的初始化方法中定义对应业务层的实例属性，要完成一个完整的测试用例步骤，可能需要调用多个PO业务层中的业务方法，才能
形成一个完整测试操作步骤。
5.定义类级别的销毁的方法，调用工具类中关闭浏览器驱动的方法
6.定义测试方法，按手工测试步骤才执行(调用)对应PO业务层中的业务方法，通过初始化方法中定义好实例属性来进行方法调用
7.设计断言
8.定义方法级别fixture，每次执行完测试方法之后回到首页
"""
import time
import unittest

from page.cart_page import CartProxy
from page.home_page import HomeProxy
from page.submit_order_page import SubmitOrderProxy
from utils import DriverUtils


class TestOrder(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # 获取浏览器驱动对象
        cls.driver = DriverUtils.get_driver()
        # 实例化首页业务层对象
        cls.home_proxy = HomeProxy()
        # 实例化购物车业务层对象
        cls.cart_proxy = CartProxy()
        # 实例化提交订单业务层对象
        cls.so_proxy = SubmitOrderProxy()

    @classmethod
    def tearDownClass(cls):
        time.sleep(2)
        DriverUtils.quit_driver()

    def setUp(self):
        self.driver.get("http://localhost/")

    def test_submit_order(self):
        # 在首页点击购物车
        self.home_proxy.to_cart_page()
        # 在购物车页面点击去结算
        self.cart_proxy.to_submit_order_page()
        # 在提交订单页面点击提交订单并且获取提交结果
        msg = self.so_proxy.test_submit_order()
        # 断言
        self.assertIn("订单提交成功", msg)
