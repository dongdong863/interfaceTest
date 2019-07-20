import os
import configparser #读取配置文件的包
import getpathInfo#导入提示报错，可以尝试把getpathInfo.py文件放到lib目录下

path = getpathInfo.get_path()
config_path = os.path.join(path,'config.ini')
config = configparser.ConfigParser()
config.read(config_path,encoding='utf-8')

class ReadConfig():
    
    def get_http(self,name):
        value= config.get('HTTP',name)
        return value
    def get_email(self,name):
        value = config.get('EMAIL',name)
        return value
    def get_db(self,name):
        value = config.get('DATABASE',name)
        return value

if __name__ == '__main__':
    print('HTTP中的baseurl值为：',ReadConfig().get_http('baseurl'))
    
    print('EMAIL中开关on_off值为：',ReadConfig().get_email('on_off'))

