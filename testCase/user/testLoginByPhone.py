import unittest
import paramunittest
from common import common
from common.Log import MyLog
import readConfig as readConfig
from common import configHttp as configHttp
import logging

data = common.get_xls_bypandas("user.xlsx", "login")
Readconfig = readConfig.ReadConfig()
cf = configHttp.ConfigHttp()

@paramunittest.parametrized(*data)
class test_Login(unittest.TestCase):
    def setParameters(self, case_name, path, method, phone, password, countryCode, code, msg):
        self.case_name = str(case_name)
        self.path = str(path)
        self.method = str(method)
        self.phone = str(phone)
        self.password = str(password)
        self.countryCode = str(countryCode)
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

        # header = {'Content-Type': 'application/json'}
        # cf.set_headers(header)
        data1 = {'phone': self.phone, 'password': self.password, 'countryCode': self.countryCode}
        #cf.set_data(json.dumps(requestdata))
        cf.set_data(data1)
        self.response = cf.postWithData()
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


if __name__ == "__main__":
    pass

'''
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import urllib
#os.environ['NO_PROXY'] = 'https://accounts.douban.com'

url = 'http://ft1.home.zhaoonline.com'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}

cookies_str ='gr_user_id=d832bb4a-9eed-4753-b397-7c845a2adec2; NTKF_T2D_CLIENTID=guestF8DDC6E8-1C53-DED6-D999-E23A5D5AFE51; nTalk_CACHE_DATA={uid:kf_9560_ISME9754_guestF8DDC6E8-1C53-DE,tid:1511340088572046}; login=zhaoonline; _ga=GA1.2.125441781.1511328997; _gid=GA1.2.532911737.1511328997; Hm_lvt_4faf922322b14bb2c7f2772de1260d0c=1511328996,1511340088; Hm_lpvt_4faf922322b14bb2c7f2772de1260d0c=1511340091; gr_session_id_8add9b5e848122aa=a9f00599-33ce-4689-aaee-75da7b65e084; JSESSIONID=27560BBCC23DF55F3E3B542EF0432ABC; ZHAOONLINE_WEB_LOGIN_ID=8136135; WEB_LOGIN_ID=8136135; ZHAOONLINE_LOGIN_COOKIE=85f7492cc27546069f9668ad19c19d7e; __sign=e38498dd409fa6164eb26ed5a372a989; _z_tk=ZeZGvu7Gq7TppjLg3dm; _z_uid=8136135; _z_nickname=%E5%90%B4%E5%B0%8F%E4%B9%A63; ZHAOONLINE_COOKIE_KEY=1A8DF47F1C52D73651214792D5A76812; OZ_1U_2263=vid=va150ce491b645.0&ctime=1511340598&ltime=1511340090; OZ_1Y_2263=erefer=-&eurl=http%3A//ft1.sh.zhaoonline.com/&etime=1511340088&ctime=1511340598&ltime=1511340090&compid=2263'
cookies = {}
for line in cookies_str.split(';'):
    key,value = line.split('=',1)
    cookies[key] =value

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
response = requests.get(url=url, cookies = cookies, headers = headers,verify=False)

print(response.status_code)
'''
