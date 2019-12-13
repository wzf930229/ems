from base.method import *
import unittest
from page.openS import *
from utils.excel_data import excel_data as e
from log import logger
import datetime
class test_sys(unittest.TestCase):
    def setUp(self):
        self.obj=method()
        self.excel_data =e()
        #获取实际结果列数
        self.r_col=self.excel_data.get_result_col()
        #获取响应时间列数
        self.t_col=self.excel_data.get_time_col()
        self.f = "public_url.json"
        self.f1="requestData_sys.json"
        self.f2="data_sys.xls"
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
        #登录日志查询
        r=self.obj.post_t(2,self.f1,self.f2)
        self.write2excel(r,2,self.f2)
        #选择模块下拉列表
        r=self.obj.get_t(3,self.f1,self.f2)
        self.write2excel(r,3,self.f2)
        #操作类型下拉列表
        r=self.obj.get_t(4,self.f1,self.f2)
        self.write2excel(r,4,self.f2)
        #获取物业列表
        r=self.obj.get_t(5,self.f1,self.f2)
        self.write2excel(r,5,self.f2)
    def test_003(self):
        #查询企业下所有删除数据列表
        r=self.obj.post_t(6,self.f1,self.f2)
        self.write2excel(r,6,self.f2)
        #新增企业数据删除配置
        r=self.obj.get_t(7,self.f1,self.f2)
        outletIds=r.json()["data"]["listTree"][0]["children"][0]["orgId"]
        shopIds=r.json()["data"]["listTree"][0]["orgId"]
        self.write2excel(r,7,self.f2)
        startTime=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        endTime=(datetime.datetime.now()+datetime.timedelta(hours=6)).strftime("%Y-%m-%d %H:%M:%S")
        l=[]
        li=[]
        l.append("outletIds")
        li.append([outletIds])
        l.append("shopIds")
        li.append([shopIds])
        l.append("startTime")
        li.append(startTime)
        l.append("endTime")
        li.append(endTime)
        r=self.obj.post_c(8,self.f1,self.f2,l,li)
        self.write2excel(r,8,self.f2)
        idd=r.json()["data"]["id"]
        #编辑
        l = []
        li = []
        l.append("outletIds")
        li.append([outletIds])
        l.append("shopIds")
        li.append([shopIds])
        l.append("startTime")
        li.append(startTime)
        l.append("endTime")
        li.append(endTime)
        l.append("id")
        li.append(idd)
        r=self.obj.post_c(9,self.f1,self.f2,l,li)
        self.write2excel(r,9,self.f2)
        #详情
        r=self.obj.get_v(10,idd,self.f1,self.f2)
        self.write2excel(r,10,self.f2)
        # 删除
        r = self.obj.get_v(11, idd, self.f1, self.f2)
        self.write2excel(r, 11, self.f2)
if __name__ == '__main__':
    unittest.main()