"""
商品详情页(尝试编写详情页面的PO)
"""
from selenium.webdriver.common.by import By

from base.base_page import BasePage, BaseHandle
from utils import DriverUtils

"""
对象库层：
1.定义对象库层类，继承对象库层基类，记住导包
2.定义对象库层初始化方法，重写父类初始化方法
3.定义对象库层实例属性，当前py文件所代表的页面所有要操作的元素，都定义一个实例属性来表示
4.实例属性赋值，通过实例属性来管理定位信息，值的类型为元组(含2个元素)，一个元素为By类提供的定位方法，
  第二个元素为选中定位方式后所对应的值
5.定义对象库层实例方法，当前py文件所代表的页面所要用的元素，都定义一个对应的找元素实例方法
6.实现实例方法，通过继承方式调用基类中公用的元素定位方法，找到元素对象，并且返回
"""


class GoodsInfoPage(BasePage):

    def __init__(self):
        super().__init__()
        # 加入购物车按钮
        self.add_cart = (By.ID, "join_cart")
        # iframe
        self.iframe = (By.CSS_SELECTOR, "[id*='layui-layer-iframe']")
        # 结果信息
        self.result = (By.CSS_SELECTOR, ".conect-title span")

    # 找加入购物车按钮
    def find_add_cart(self):
        return self.find_ele(self.add_cart)

    # 找iframe
    def find_iframe(self):
        return self.find_ele(self.iframe)

    # 找结果信息
    def find_result(self):
        return self.find_ele(self.result)


"""
操作层：
1.定义操作层类，继承操作层基类，记住导包
2.定义操作层初始化方法，在初始化方法中创建对象库层对象，并定义一个实例属性来承接
3.定义操作层操作方法，当前py文件所代表的页面所有要操作的元素都定义一个操作方法，如输入、点击等，
  部分特殊的另外处理
4.实现操作层操作方法，通过第2步实例属性来调用对象库层的实例方法找到元素对象后执行常用元素操作方法
"""


class GoodsInfoHandle(BaseHandle):

    def __init__(self):
        self.gi_page = GoodsInfoPage()

    # 购物车按钮的点击
    def click_add_cart(self):
        self.gi_page.find_add_cart().click()

    # 获取加入购物车的结果信息
    def get_result(self):
        # iframe切换
        DriverUtils.get_driver().switch_to.frame(self.gi_page.find_iframe())
        # 获取结果
        return self.gi_page.find_result().text


"""
业务层：
1.定义业务层类
2.定义业务层初始化方法，在初始化方法中创建操作层对象，并定义一个实例属性来承接
3.定义业务层业务方法，当前py文件所代表的页面可能存在多个业务操作，根据实际手工测试用例来定义，
如商品详情页面对于加入购物车的用例提供了加入购物车业务操作
"""


class GoodsInfoProxy:

    def __init__(self):
        self.gi_handle = GoodsInfoHandle()

    # 加入购物车并且返回加入结果
    def test_add_cart(self):
        # 1.加入购物车
        self.gi_handle.click_add_cart()
        # 2.返回加入结果
        return self.gi_handle.get_result()
