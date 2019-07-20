import os
#os.path.split() 返回文件的路径和文件名
def get_path():

    #path = os.path.split(os.path.realpath(__file__))[0]
    path = os.path.split(__file__)[0]
    return path

if __name__=='__main__':
    print('测试路径是否OK，路径为:',get_path())
