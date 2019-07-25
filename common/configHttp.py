import requests
import json
class RunMain():
    def send_post(self, url, data):
        result = requests.post(url= url,data= data).json()
        res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
        return res
    
    def send_get(self,url,data):
        result = requests.get(url= url,data=data)
        res = json.dumps(result,ensure_ascii=False,sort_keys=True, indent=2)
        return res
    
    def run_main(self,method,url=None,data=None):
        result = None
        if method =='post':
            result= self.send_post(url,data)
        elif method =='get':
            result= self.send_get(url,data)
        else:
            print("menthod值错误！！")
        
        return result

if __name__ == '__main__':
    result = RunMain().run_main('post', 'http://127.0.0.1:8888/login', 'name=xiaoming&pwd=')
    print(result)

