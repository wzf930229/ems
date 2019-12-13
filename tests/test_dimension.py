from base.method import *
import unittest
from page.openS import *
from utils.excel_data import excel_data as e
from log import logger
class test_dimension(unittest.TestCase):
    def setUp(self):
        self.obj=method()
        self.excel_data =e()
        #获取实际结果列数
        self.r_col=self.excel_data.get_result_col()
        #获取响应时间列数
        self.t_col=self.excel_data.get_time_col()
        self.f = "public_url.json"
        self.f1="requestData_dimension.json"
        self.f2="data_dimension.xls"
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
        #维度列表-查询收入中心标签
        r=self.obj.get_t(2,self.f1,self.f2)
        self.write2excel(r,2,self.f2)
        #维度列表-查询物业标签
        r = self.obj.get_t(3, self.f1, self.f2)
        self.write2excel(r, 3, self.f2)
        #维度列表-新增物业标签
        r=self.obj.post_t(4,self.f1,self.f2)
        self.write2excel(r,4,self.f2)
        #维度列表-新增收入中心标签
        r = self.obj.post_t(5, self.f1, self.f2)
        self.write2excel(r, 5, self.f2)
        #维度列表-编辑
        id=r.json()["data"]["id"]
        l=[]
        li=[]
        l.append("id")
        li.append(id)
        r=self.obj.post_c(6,self.f1,self.f2,l,li)
        self.write2excel(r,6,self.f2)
        #维度项-新增
        l = []
        li = []
        l.append("dimensionTypeId")
        li.append(id)
        r = self.obj.post_c(7, self.f1, self.f2, l, li)
        self.write2excel(r, 7, self.f2)
        id1=r.json()["data"]["id"]
        #维度项-查询
        l = []
        li = []
        l.append("dimensionTypeId")
        li.append(id)
        r = self.obj.get_c(8, self.f1, self.f2, l, li)
        self.write2excel(r, 8, self.f2)
        #维度项 - 编辑
        l = []
        li = []
        l.append("id")
        li.append(id1)
        r=self.obj.post_c(9,self.f1,self.f2,l,li)
        self.write2excel(r,9,self.f2)
        #查询物业机构树
        r=self.obj.get_t(10,self.f1,self.f2)
        self.write2excel(r,10,self.f2)
        #查询维度列表
        entityId=r.json()["data"]["listTree"][0]["children"][0]["parentId"]
        l=[]
        li=[]
        l.append("entityId")
        li.append(entityId)
        r=self.obj.get_c(11,self.f1,self.f2,l,li)
        self.write2excel(r,11,self.f2)
        #维度项-删除
        r=self.obj.post_v(12,id1,self.f1,self.f2)
        self.write2excel(r,12,self.f2)
        #维度列表-删除
        r = self.obj.post_v(13, id, self.f1, self.f2)
        self.write2excel(r, 13, self.f2)
if __name__ == '__main__':
    unittest.main()