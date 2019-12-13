#作者:Administrator
#时间:2019/10/20
from utils import operationExcel
from utils.operationJson import operationJson as op
from utils.excel_data import *
import json
import requests
from page.openS import *
import json
class method:
    def __init__(self):
        self.excel=operationExcel.operationExcel()
        self.data=op()
        #self.url=self.data.get_public_url()

    #不带token不带参的post请求
    def post(self,row,f1,f2):
        return requests.post(url=self.data.get_n_url(row,f2),
                        data=self.data.get_json_data(row,f1,f2),
                        headers=getHeader())

    #带token不带参的post请求
    def post_t(self,row,f1,f2):
        return requests.post(url=self.data.get_n_url(row,f2),
                        data=self.data.get_json_data(row,f1,f2),
                        headers=getHeader_token())
    #参数可自行输入的post请求
    def post_c(self,row,f1,f2,l=[],li=[]):
        return requests.post(url=self.data.get_n_url(row,f2),
                        data=json.dumps(set_key_val(row,f1,f2,l,li)),
                        headers=getHeader_token())

    # 参数可自行输入的get请求
    def get_c(self, row, f1, f2, l=[], li=[]):
        return requests.get(url=self.data.get_n_url(row,f2),
                        params=(set_key_val(row, f1, f2, l, li)),
                        headers=getHeader_token())

    #不带token不带参的get请求
    def get(self, row,f1,f2):
        return requests.get(url=self.data.get_n_url(row,f2),
                            params=json.loads(self.data.get_json_data(row,f1,f2)),
                            headers=getHeader())
    #带token不带参的get请求
    def get_t(self,row,f1,f2):
        return requests.get(url=self.data.get_n_url(row,f2),
                            params=json.loads(self.data.get_json_data(row,f1,f2)),
                            headers=getHeader_token())
    #url中带两个参数的get请求
    def get_2v(self,row,id1,id2,f1,f2):
        return requests.get(url=self.data.get_2v_url(row,id1,id2,f2),
                            params=json.loads(self.data.get_json_data(row,f1,f2)),
                            headers=getHeader_token())
    #带token且url中带参数的get请求
    def get_v(self,row,id,f1,f2):
        return requests.get(url=self.data.get_v_url(row,id,f2),
                            params=json.loads(self.data.get_json_data(row,f1,f2)),
                            headers=getHeader_token())
    #带token且url中带参数的post请求
    def post_v(self,row,id,f1,f2):
        return requests.post(url=self.data.get_v_url(row,id,f2),
                            data=self.data.get_json_data(row,f1,f2),
                            headers=getHeader_token())
    def get_tenantId(self,row,f1,f2):
        return json.loads(self.data.get_json_data(row,f1,f2))["tenantId"]
class IsAssert:
    def __init__(self):
        self.excel=operationExcel.operationExcel()
    def IsContent(self,row,str2):
        flag=None
        if self.excel.get_expect(row) in str2:
            flag=True
        else:
            flag=False
        return flag


