#作者:Administrator
#时间:2019/10/19
from utils.public import *
import json
from utils import operationExcel
class operationJson:

    def __init__(self):
        self.excel=operationExcel.operationExcel()

    def getReadJson(self,f1):
        with open(data_dir(data="data",filename=f1),encoding="utf-8") as f:
            data=json.load(f)
        return data
    def get_json_data(self,row,f1,f2):
        return json.dumps(self.getReadJson(f1)[self.excel.get_data(row,f2)])
    def get_public_url(self):
        public_url=self.getReadJson("public_url.json")["public_url"]
        return public_url
    #获取不带参的url
    def get_n_url(self, row,f):
        return self.get_public_url() + self.excel.get_url(row,f)
    #获取带参的url
    def get_v_url(self, row,id,f):
        url=str(self.get_public_url() + self.excel.get_url(row,f)).format(id)
        return url
    def get_2v_url(self,row,id1,id2,f):
        url = str(self.get_public_url() + self.excel.get_url(row, f)).format(id1,id2)
        return url



