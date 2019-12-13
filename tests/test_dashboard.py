from base.method import *
import unittest
from page.openS import *
from utils.excel_data import excel_data as e
from log import logger
class test_dashboard(unittest.TestCase):
    def setUp(self):
        self.obj=method()
        self.excel_data =e()
        #获取实际结果列数
        self.r_col=self.excel_data.get_result_col()
        #获取响应时间列数
        self.t_col=self.excel_data.get_time_col()
        self.f = "public_url.json"
        self.f1="requestData_dashboard.json"
        self.f2="data_dashboard.xls"
        self.tenantId = self.obj.get_tenantId(1, self.f, self.f2)
        self.logger = logger.logger(__name__)
    def write2excel(self,r,row,f):
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["status"], 200)
        writeResult(row, self.r_col, "pass",f)
        writeResult(row, self.t_col, r.elapsed.total_seconds(),f)
    def tearDown(self):
        pass
    def test_001(self):
        #登陆系统
        r=self.obj.post(1,self.f,self.f2)
        writeToken(r.json()["data"]["token"])
        #r=self.obj.post_token(2)
        self.write2excel(r,1,self.f2)
    def test_002(self):
        #查询文件列表
        r=self.obj.get_t(2,self.f1,self.f2)
        self.write2excel(r,2,self.f2)
        #查询看板列表
        if len(r.json()["data"][0]["children"])>0:
            id = r.json()["data"][0]["children"][0]["id"]
            l = []
            li = []
            l.append("folderId")
            li.append(id)
            r = self.obj.get_c(3, self.f1, self.f2, l, li)
            self.write2excel(r, 3, self.f2)
            if len(r.json()["data"]["rows"])>0:
                id=r.json()["data"]["rows"][0]["id"]
                enable_flag=r.json()["data"]["rows"][0]["enable_flag"]
                if enable_flag==0:
                    l=[]
                    li=[]
                    l.append("id")
                    li.append(id)
                    l.append("enableFlag")
                    li.append("1")
                    r=self.obj.post_c(5,self.f1,self.f2,l,li)
                    self.write2excel(r,5,self.f2)
                else:
                    l = []
                    li = []
                    l.append("id")
                    li.append(id)
                    l.append("enableFlag")
                    li.append("1")
                    r = self.obj.post_c(4, self.f1, self.f2, l, li)
                    self.write2excel(r, 4, self.f2)
if __name__ == '__main__':
    unittest.main()