from base.method import *
import unittest
from page.openS import *
from utils.excel_data import excel_data as e
from log import logger
class test_org(unittest.TestCase):
    def setUp(self):
        self.obj=method()
        self.excel_data =e()
        #获取实际结果列数
        self.r_col=self.excel_data.get_result_col()
        #获取响应时间列数
        self.t_col=self.excel_data.get_time_col()
        self.f = "public_url.json"
        self.f1="requestData_org.json"
        self.f2="data_org.xls"
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
        #物业管理-物业分页列表查询
        r=self.obj.post_t(2,self.f1,self.f2)
        self.write2excel(r,2,self.f2)
        status = r.json()["data"]["rows"][0]["status"]
        id = r.json()["data"]["rows"][0]["id"]
        if r.json()["data"]["total"]>0:
            #物业管理-物业下收入中心查询
            shopId=r.json()["data"]["rows"][0]["shopId"]
            l=[]
            li=[]
            l.append("shopId")
            li.append(shopId)
            l.append("tenantId")
            li.append(self.tenantId)
            r=self.obj.post_c(3,self.f1,self.f2,l,li)
            self.write2excel(r,3,self.f2)
        #物业管理-修改物业状态-启禁用按钮
        if status==1:
            r=self.obj.get_v(4,id,self.f1,self.f2)
            self.write2excel(r,4,self.f2)
            r = self.obj.get_v(5, id, self.f1, self.f2)
            self.write2excel(r, 5, self.f2)
        else:
            r = self.obj.get_v(5, id, self.f1, self.f2)
            self.write2excel(r, 5, self.f2)
            r = self.obj.get_v(4, id, self.f1, self.f2)
            self.write2excel(r, 4, self.f2)
        #查看物业详情
        r=self.obj.get_v(6,id,self.f1,self.f2)
        self.write2excel(r,6,self.f2)
        #查询物业绑定的层级维度
        l=[]
        li=[]
        l.append("id")
        li.append(id)
        l.append("tenantId")
        li.append(self.tenantId)
        r=self.obj.get_c(7,self.f1,self.f2,l,li)
        self.write2excel(r,7,self.f2)
    def test_003(self):
        #组织机构-新增按钮
        l=[]
        li=[]
        l.append("parentId")
        li.append(self.tenantId)
        l.append("tenantId")
        li.append(self.tenantId)
        r=self.obj.post_c(8,self.f1,self.f2,l,li)
        self.write2excel(r,8,self.f2)
        # 组织机构页面 - 左边层级页面
        r = self.obj.get_t(9, self.f1, self.f2)
        self.write2excel(r, 9, self.f2)
        length = len(r.json()["data"]["listTree"])
        id1 = r.json()["data"]["listTree"][length-1]["id"]
        id2 = r.json()["data"]["listTree"][length-2]["id"]
        #组织机构-编辑按钮
        l = []
        li = []
        l.append("parentId")
        li.append(self.tenantId)
        l.append("tenantId")
        li.append(self.tenantId)
        l.append("id")
        li.append(id1)
        r = self.obj.post_c(10, self.f1, self.f2, l, li)
        self.write2excel(r, 10, self.f2)
        # 组织机构排序上下移
        if length>1:
            r=self.obj.get_2v(11,id1,id2,self.f1,self.f2)
            self.write2excel(r,11,self.f2)
            self.obj.get_2v(11, id2, id1, self.f1, self.f2)
        #物业查询
        l=[]
        li=[]
        l.append("id")
        li.append(id1)
        r=self.obj.post_c(12,self.f1,self.f2,l,li)
        self.write2excel(r,12,self.f2)
        # 未绑定物业查询
        l = []
        li = []
        l.append("id")
        li.append(id1)
        r = self.obj.post_c(13, self.f1, self.f2, l, li)
        self.write2excel(r, 13, self.f2)
        addList=r.json()["data"]["rows"][0]["id"]
        if r.json()["data"]["total"]>0:
            #组织机构物业绑定
            l=[]
            li=[]
            l.append("tenantId")
            li.append(self.tenantId)
            l.append("addList")
            li.append([addList])
            l.append("deptId")
            li.append(id1)
            r=self.obj.post_c(14,self.f1,self.f2,l,li)
            self.write2excel(r,14,self.f2)
            #组织机构物业解绑
            l = []
            li = []
            l.append("tenantId")
            li.append(self.tenantId)
            l.append("delList")
            li.append([addList])
            l.append("deptId")
            li.append(id1)
            r = self.obj.post_c(15, self.f1, self.f2, l, li)
            self.write2excel(r, 15, self.f2)
        #组织机构删除
        r=self.obj.get_v(16,id1,self.f1,self.f2)
        self.write2excel(r,16,self.f2)
if __name__ == '__main__':
    unittest.main()