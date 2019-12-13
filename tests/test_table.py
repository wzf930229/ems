from base.method import *
import unittest
from page.openS import *
from utils.excel_data import excel_data as e
from log import logger
class test_table(unittest.TestCase):
    def setUp(self):
        self.obj=method()
        self.excel_data =e()
        #获取实际结果列数
        self.r_col=self.excel_data.get_result_col()
        #获取响应时间列数
        self.t_col=self.excel_data.get_time_col()
        self.f = "public_url.json"
        self.f1="requestData_table.json"
        self.f2="data_table.xls"
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
        #维度类别新增
        r=self.obj.post_t(2,self.f1,self.f2)
        self.write2excel(r,2,self.f2)
        id=r.json()["data"]["id"]
        typeName=r.json()["data"]["typeName"]
        #加载维度类别
        r=self.obj.get_t(3,self.f1,self.f2)
        self.write2excel(r,3,self.f2)
        #维度类别下移
        if len(r.json()["data"])>1:
            id=r.json()["data"][0]["id"]
            l=[]
            li=[]
            l.append("dimensionTypeId")
            li.append(id)
            r=self.obj.post_c(7,self.f1,self.f2,l,li)
            self.write2excel(r,7,self.f2)
            #维度类别上移
            r = self.obj.post_c(8, self.f1, self.f2, l, li)
            self.write2excel(r, 8, self.f2)
        #层级维度新增
        l=[]
        li=[]
        l.append("dimensionTypeId")
        li.append(id)
        r=self.obj.post_c(4,self.f1,self.f2,l,li)
        self.write2excel(r,4,self.f2)
        dimensionValue=r.json()["data"]["dimensionValue"]
        #层级维度编辑
        id1=r.json()["data"]["id"]
        labelDefault=r.json()["data"]["labelDefault"]
        level=r.json()["data"]["level"]
        levelName=r.json()["data"]["levelName"]
        parentId=r.json()["data"]["parentId"]
        l=[]
        li=[]
        l.append("dimensionTypeId")
        li.append(id)
        l.append("id")
        li.append(id1)
        l.append("labelDefault")
        li.append(labelDefault)
        l.append("level")
        li.append(level)
        l.append("levelName")
        li.append(levelName)
        l.append("parentId")
        li.append(parentId)
        r=self.obj.post_c(9,self.f1,self.f2,l,li)
        self.write2excel(r,9,self.f2)
        #加载报表层级
        l=[]
        li=[]
        l.append("id")
        li.append(id)
        r=self.obj.get_c(5,self.f1,self.f2,l,li)
        self.write2excel(r,5,self.f2)
        #维度类别编辑
        l=[]
        li=[]
        l.append("id")
        li.append(id)
        l.append("typeName")
        li.append(typeName)
        r=self.obj.post_c(6,self.f1,self.f2,l,li)
        self.write2excel(r,6,self.f2)
        #查询层级维度绑定的物业
        l=[]
        li=[]
        l.append("hierarchyId")
        li.append(dimensionValue)
        r=self.obj.post_c(10,self.f1,self.f2,l,li)
        self.write2excel(r,10,self.f2)
        #查询未绑定的物业
        l = []
        li = []
        l.append("hierarchyId")
        li.append(dimensionValue)
        r = self.obj.post_c(11, self.f1, self.f2, l, li)
        self.write2excel(r, 11, self.f2)
        #报表层级与物业绑定
        if r.json()["data"]["total"]>0:
            shopIds=r.json()["data"]["rows"][0]["id"]
            l.append("shopIds")
            li.append(shopIds)
            l.append("hierarchyId")
            li.append(dimensionValue)
            r=self.obj.post_c(12,self.f1,self.f2,l,li)
            self.write2excel(r,12,self.f2)
            #报表层级与物业解绑
            l = []
            li = []
            l.append("hierarchyId")
            li.append(dimensionValue)
            r = self.obj.post_c(10, self.f1, self.f2, l, li)
            ids=r.json()["data"]["rows"][0]["shopHierarchyRelId"]
            l=[]
            li=[]
            l.append("ids")
            li.append(ids)
            r=self.obj.post_c(13,self.f1,self.f2,l,li)
            self.write2excel(r,13,self.f2)
        #层级维度删除
        r=self.obj.post_v(14,id1,self.f1,self.f2)
        self.write2excel(r,14,self.f2)
        #维度类别删除
        r = self.obj.post_v(15, id, self.f1, self.f2)
        self.write2excel(r, 15, self.f2)
if __name__ == '__main__':
    unittest.main()