# -*- coding: utf-8 -*-
import json
import unittest

import requests
import urllib3


class MyTestCase(unittest.TestCase):

    def setUp(self):
        """
        执行测试用例前的初始化操作
        """
        urllib3.disable_warnings()
        self.headers = {'Accept': 'application/json;charset=UTF-8'}

    def testCnpcAuth(self):
        data = {
          "idName": "刘春雷",
          "idNumber": "411527199208117052",
          "phone": "18637638958",
          "uuid": "8855858"
        }

        url = 'https://10.7.7.71:8823/api/cnpcAuth'
        res = requests.post(url, json=data, headers=self.headers, verify=False)
        ret = res.json()
        # print(res.content)

        self.assertEqual(200, res.status_code)
        self.assertEqual('系统繁忙', ret.get('errorMessage'))
        # self.assertEqual()

    def tearDown(self):
        """
        执行测试用例后的操作
        """
        print ("Test Done...")


if __name__ == "__main__":
    unittest.main()
