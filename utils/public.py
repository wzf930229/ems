#作者:Administrator
#时间:2019/10/19
import os
def data_dir(data=None,filename=None):
    return os.path.join(os.path.dirname(os.path.dirname(__file__)),data,filename)


