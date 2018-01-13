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
    def run(self):
        # logger.info("*****Test Start*********")
        discover = unittest.defaultTestLoader.discover(case_path, pattern="test*.py", top_level_dir=None)
        return discover

        fp = open(resultPath, 'wb')
        runner = HTMLTestReportCN.HTMLTestRunner(stream=fp, title='Test Report', description='Test Description')
        runner.run()
        #fp.close()


if __name__ == "__main__":
    #runner =unittest.TextTestRunner()
    obj = ALLTest()
    obj.run()







'''


import readConfig
import configparser
import codecs
import os
proDir = '/Users/nancy/Documents/pyproject/lottery_Interface/'

configFile = os.path.join(proDir, "config.ini")


class ReadConfig:
    def __init__(self):
        fd = open(configFile)
        data = fd.read()
        #  remove BOM
        if data[:3] == codecs.BOM_UTF8:
            data = data[3:]
            file = codecs.open(configFile, "w")
            file.write(data)
            file.close()
        fd.close()

        self.cf = configparser.ConfigParser()
        self.cf.read(configFile)

    def get_email(self, name):
        value = self.cf.get("EMAIL", name)
        print(value)

    def get_HTTP(self, name):
        value = self.cf.get("HTTP", name)
        print(value)


Rc = ReadConfig()
Rc.get_email("mail_host")
Rc.get_HTTP("scheme")

'''

##——————————————————————————————————————————————————————————————————#####################
'''
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import traceback

mail_host = "smtp.sina.com"
mail_user = "w_sping@sina.com"
mail_pass = "015501239"


sender='w_sping@sina.com'
receivers=['wushuping@zhaoonline.com']
message=MIMEText('Python 邮件发送', 'plain', 'utf-8')
message['From'] = 'w_sping@sina.com'
message['To'] = 'wushuping@zhaoonline.com'

subject = 'Python'
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")

except smtplib.SMTPException:
    traceback.print_exc()



'''

##——————————————————————————————————————————————————————————————————#####################




'''


import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import urllib
#os.environ['NO_PROXY'] = 'https://accounts.douban.com'
url = 'https://accounts.douban.com'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'}

cookies_str = '__yadk_uid=g0JD2otoAYrazhfjhZU3s4ShmFT09b3i; _pk_id.100001.8cb4=bb129a130bd09611.1511326608.1.1511326959.1511326608.; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1511326608%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DboXKyZoOnALMw1GjeM9rRdbYQcWnv126KAhmESFv2tu%26wd%3D%26eqid%3Db81e34cb00036802000000045a15038c%22%5D; _pk_ses.100001.8cb4=*; __ads_session=36MtZP4ZAgkfcwYGAgA=; __utma=30149280.1876126327.1511326611.1511326611.1511326611.1; __utmb=30149280.15.10.1511326611; __utmc=30149280; __utmt=1; __utmv=30149280.10014; __utmz=30149280.1511326611.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; ap=1; bid=JDTF9q-id60; ct=y; dbcl2="100142835:pJ0YOiSaAGk"; ll="108296"; ps=y; push_doumail_num=0; push_noty_num=0; ue="w_sping@sina.com"'
cookies = {}
for line in cookies_str.split(';'):
    key,value = line.split('=',1)
    cookies[key] =value

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
response = requests.get(url=url, cookies = cookies, headers = headers,verify=False)

print(response.status_code)

'''
