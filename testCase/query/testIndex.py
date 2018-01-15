import unittest
import paramunittest
from common import common
from common.Log import MyLog
import readConfig as readConfig
from common import configHttp as configHttp
import logging

data = common.get_xls_bypandas("query.xlsx", "index")
Readconfig = readConfig.ReadConfig()
cf = configHttp.ConfigHttp()

@paramunittest.parametrized(*data)
class test_Login(unittest.TestCase):
    def setParameters(self, case_name, path, method, code, msg):
        self.case_name = str(case_name)
        self.path = str(path)
        self.method = str(method)
        self.code = int(code)
        self.msg = str(msg)

    def shortDescription(self):
        self.case_name

    def setUp(self):
        self.log = MyLog.get_log()
        self.logger = self.log.get_logger()

    def test_Login(self):
        self.url = self.path
        cf.set_url(self.url)
        self.response = cf.getwithoutheaders()
        #print(self.response.text)
        self.checkResult()

    def tearDown(self):
 #       self.log.build_case_line(self.info)
        pass
    def checkResult(self):
        self.info = self.response.json()
        logging.info(self.info)
        #common.show_return_msg(self.response)
        self.assertEqual(self.info['code'], self.code)
        self.assertEqual(self.info['msg'], self.msg)

