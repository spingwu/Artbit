import os
import unittest
from common.Log import MyLog as Log
import readConfig as readConfig
from common import HTMLTestReportCN
from common import HTMLTestRunner
from common.configEmail import MyEmail
case_path = os.path.join(os.getcwd(),"testCase","query")
resultPath = os.path.join(os.getcwd(),"result","report.html")

localReadConfig = readConfig.ReadConfig()


class ALLTest:
    def __init__(self):
        global log, logger, resultpath, on_off
        log = Log.get_log()
        logger = log.get_logger()
        on_off = localReadConfig.get_email("on_off")
        self.email = MyEmail.get_email()
    def run(self):
        try:
            logger.info("*****Test Start*********")
            discover = unittest.defaultTestLoader.discover(case_path, pattern="test*.py")
            # return discover
            fp = open(resultPath, 'wb')
            runner = HTMLTestReportCN.HTMLTestRunner(stream=fp, title=u'Test Report', description=u'Test Description')
            runner.run(discover)


        finally:
            logger.info("*********TEST END*********")
            fp.close()
            # send test report by email
            if on_off == 'on':
                self.email.send_email()
            elif on_off == 'off':
                logger.info("Doesn't send report email to developer.")
            else:
                logger.info("Unknow state.")



if __name__ == "__main__":
    #runner =unittest.TextTestRunner()
    obj = ALLTest()
    obj.run()
