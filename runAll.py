import os
import getpathInfo
import readConfig
from common.configEmail import send_Email
from apscheduler.schedulers.blocking importBlockingSchduler
import unittest
import common.HTMLTestRunner as HTMLTestRunner
import pythoncom
import common.log.logger



send_email = send_email()
path = getpathInfo.get_Path()
report_path = os.path.join(path,'result')
on_off = readConfig.ReadConfig().get_email('on_off')

class AllTest:
    def __init__(self):#初始化参数和数据
        global resultPath  #对函数内部变脸起作用
        resultPath = os.path.join(report_path,"report.html")
        self.caseListFile = os.path.join(path,"caselist.txt")
        self.caseFile = os.path.join(path,"testCase")
        self.caseList=[]
        log.info('resultPath',resultPath)
        log.info('caseListFile',self.caseListFile)
        log.info('caseList',self.caseList)

    def set_case_list(self):

        fb = open(self.caseListFile)
        for  value in fb.readlines():
            data = str(value)
            if data !='' and not data.startswith("#"):
                slef.caseList.append(data.replace("\n",""))
        fb.close

    def set_case_suite(self):

        self.set_case_list()
        test_suite = unittest.TestSuite()
        sutie_module = []
        for case in self.caseLis:
            case_name = case.split("/")[-1]
            print("case_name+".py)

            discover = unittest.defaultTestLoader.discover(self.caseFile,pattern=case_name+
            suite_module.append(discover))
            print('situe_module:'+str(situe_module))

        if len(sutie_module)>0:
            for suite in suite_module:
                for test_name in sutie:
                    test_sutie.addTest(test_name)
        else:
            print('else:')
            return None
        return  test_sutie

    def run(self):
        try:
            suit = self.set_case_sutie()
            print('try')
            print(str(suit))
            if suit is not None:
                print('if-suit')
                fp = open(resultPat,'wb')

                runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='Test Report',descption='Test Descption' )
                runner.run(suit)
            else:
                print("Have no case to test")
        except Exception as ex:
            print(str(ex))

        finally:
            print("******TEST END********")

            fp.close()

            if on_off =='on':
                send_email.outlook()
            else:
                print("邮件发送开关配置关闭，请打开开关后可正常自动发送测试报告")

       if __name__=='__main__':
           AllTest().run()






