# -*- coding: utf-8 -*-
import time
import unittest
from selenium import webdriver
from ddt import ddt, data, unpack


TEST_URL = "http://www.baidu.com"
TEST_DATA = ("python", "selenium", "unittest")


@ddt
class MyTestCase(unittest.TestCase):

    def setUp(self):
        """
        执行测试用例前的初始化操作
        """
        self.browser = webdriver.Chrome()

    @data(*TEST_DATA)
    def testBaidu(self, keyword):
        """
        具体的测试用例
        """
        self.browser.get(TEST_URL)
        self.browser.find_element_by_id("kw").send_keys(keyword)
        self.browser.find_element_by_id("su").click()
        # time.sleep(5)
        # self.browser.sleep(5)
        self.browser.quit()

    @unpack
    def tearDown(self):
        """
        执行测试用例后的操作
        """
        print ("Test Done...")


if __name__ == "__main__":
    unittest.main()
