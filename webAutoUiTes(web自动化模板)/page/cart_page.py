"""
购物车页面
"""
from selenium.webdriver.common.by import By

from base.base_page import BasePage, BaseHandle


class CartPage(BasePage):

    def __init__(self):
        super().__init__()
        # 去结算按钮
        self.to_settle_btn = (By.CSS_SELECTOR, ".gwc-qjs")

    # 找到结算按钮
    def find_settle_btn(self):
        return self.find_ele(self.to_settle_btn)


class CartHandle(BaseHandle):

    def __init__(self):
        self.cart_page = CartPage()

    # 点击去结算
    def click_settle_btn(self):
        self.cart_page.find_settle_btn().click()


class CartProxy:

    def __init__(self):
        self.cart_handle = CartHandle()

    # 去提交订单页面
    def to_submit_order_page(self):
        self.cart_handle.click_settle_btn()
