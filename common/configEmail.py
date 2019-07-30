import os
import readConfig
import getpathInfo
import win32com.clinet
import datetime

readconfig = readConfig().ReadConfig()
subject = readConfig.get_email('subject')
app = str(read_conf.get_email('app'))
address = read_conf.get_email('address')
cc = read_conf.get_email('cc')
mail_path = os.path.join(getpathInfo.get_Path(),'result','report.html')

class send_email():
    def outlook(self):
        olook= win32.Dispatch("%s.Application" % app)
        mail = olook.CreateItem(win32.constants.olMailItem)
        mail.To=address
        mail.cc=cc
        mail.Subject = str(datetime.datetime.now())[0:19]+'%s' %subject
        mail.Attachments.Add(mail_path,1,1,"myFile")
        content = """
                    执行测试中……
                    测试已完成！！
                    生成报告中……
                    报告已生成……
                    报告已邮件发送！！
                    """
        mail.Body = content
        mail.Send()
        
if __name__ == '__main__':
    print(subject)
    send_email().outlook()
    print("send email ok!!!!!")