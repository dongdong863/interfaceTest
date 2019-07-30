import unittest
import paramunittest
import json
from common.configHttp import RunMain
import geturlParams
import urllib.pase
import readExcel

url= geturlParams.geturlParams.get_Url()
login_xls = readExcel.readExcel().get_xls('userCase.xls','login')

@paramunittest.parametrized(*login_xls)
class testUserLogin(unittest,Testcase):
    def setParameters(self,case_name,path,query,method):
        self.case_name=str(case_name)
        self.path=str(path)
        self.query=str(query)
        self.method=str(method)

    def description(self):
        self.case_name

    def setUp(self):
        print(self.case_name+"����׼����ʼ")

    def test01case(self):
        self.checkResult()

    def tesrDown(self):
        print("���Խ��������log���\n\n")

    def checkResult(self):
        url1= "http://www.xxx.com/login?"
        new_url= url1+self.query
        data1 = dict(urllib.parse.parse_qsl(urllib.parse.urlsplit(new_url).query))# ��һ��������URL�е�name=&pwd=ת��Ϊ{'name':'xxx','pwd':'bbb'}
        info = RunMain().run_main(self.method,url,data1)
        ss= json.loads(info)

        if self.case_name == 'login':
            self.assertEqual(ss['code'],200)

        if self.case_name == 'login_error':
            self.assertEqual(ss['code'],-1)

        if self.case_name == 'login_null':
            self.assertEqual(ss['code'],10001)