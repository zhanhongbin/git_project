"""
提交订单
"""
import time
from selenium.webdriver.common.by import By

from base.base_page import BasePage, BaseHandle


class SubmitOrderPage(BasePage):

    def __init__(self):
        super().__init__()
        # 提交订单按钮
        self.submit_order_btn = (By.CSS_SELECTOR, ".Sub-orders")
        # 订单提交的结果元素
        self.submit_order_result = (By.CSS_SELECTOR, ".erhuh h3")

    # 找提交订单按钮
    def find_submit_order_btn(self):
        return self.find_ele(self.submit_order_btn)

    # 找到订单提交的结果元素
    def find_submit_order_result(self):
        return self.find_ele(self.submit_order_result)


class SubmitOrderHandle(BaseHandle):

    def __init__(self):
        self.so_page = SubmitOrderPage()

    # 点击提交订单
    def click_sob(self):
        time.sleep(3)
        self.so_page.find_submit_order_btn().click()

    # 获取提交订单结果
    def get_sbo_result(self):
        return self.so_page.find_submit_order_result().text


class SubmitOrderProxy:

    def __init__(self):
        self.so_handle = SubmitOrderHandle()

    # 提交订单并返回结果
    def test_submit_order(self):
        # 点击提交订单
        self.so_handle.click_sob()
        # 获取并返回提交订单的结果
        return self.so_handle.get_sbo_result()
