"""
商品添加购物车用例
"""
import time

from page.goods_info_page import GoodsInfoProxy
from page.home_page import HomeProxy
from page.search_goods_page import SearchGoodsProxy
from utils import DriverUtils
import unittest

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
9.在data目录定义json格式的测试数据
10.引入参数化，针对测试方法进行调整，@parameterized.expand方法来调用工具文件中读取数据文件方法来获取测试数据
11.修改测试方法参数，测试数据有多少个定义多少个参数，同时修改输入数据地方，使用参数来进行代替
"""


class TestAddCart(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = DriverUtils.get_driver()
        # 实例化首页对象
        cls.home_proxy = HomeProxy()
        # 实例化搜索结果页业务层对象
        cls.sg_proxy = SearchGoodsProxy()
        # 实例化详情页面业务层对象
        cls.gi_proxy = GoodsInfoProxy()

    @classmethod
    def tearDownClass(cls):
        time.sleep(2)
        DriverUtils.quit_driver()

    def setUp(self):
        time.sleep(2)
        self.driver.get("http://localhost/")

    def test_add_cart(self):
        # 1.在首页输入搜索信息并点击搜索
        self.home_proxy.test_search_goods("小米")
        # 2.在搜索结果页点击加入购物车
        self.sg_proxy.to_goods_info_page()
        # 3.在商品详情页点击加入购物车获取加入购物车的结果
        msg = self.gi_proxy.test_add_cart()
        # 断言
        self.assertIn("添加成功", msg)
