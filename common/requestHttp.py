import request
import json
class RunMain():
    def send_post(self, url, data):
        
        result = request.post(url= url,data= data).json()


if __name__ == '__main__':
    print（）

