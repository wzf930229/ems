from base.method import *
import unittest
from page.openS import *
from utils.excel_data import excel_data as e
from log import logger
class test_userPermission(unittest.TestCase):
    def setUp(self):
        self.obj=method()
        self.excel_data =e()
        #获取实际结果列数
        self.r_col=self.excel_data.get_result_col()
        #获取响应时间列数
        self.t_col=self.excel_data.get_time_col()
        self.f = "public_url.json"
        self.f1="requestData_userPermission.json"
        self.f2="data_userPermission.xls"
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
        #新增角色
        r=self.obj.post_t(2,self.f1,self.f2)
        self.write2excel(r,2,self.f2)
        id=r.json()["data"]["id"]
        name=r.json()["data"]["name"]
        level=r.json()["data"]["level"]
        #左侧角色列表
        r=self.obj.get_t(3,self.f1,self.f2)
        self.write2excel(r,3,self.f2)
        #右侧用户列表
        l=[]
        li=[]
        l.append("roleId")
        li.append(id)
        r=self.obj.get_c(4,self.f1,self.f2,l,li)
        self.write2excel(r,4,self.f2)
        #角色编辑
        l=[]
        li=[]
        l.append("id")
        li.append(id)
        l.append("name")
        li.append(name)
        l.append("level")
        li.append(level)
        r=self.obj.post_c(5,self.f1,self.f2,l,li)
        self.write2excel(r,5,self.f2)
        #加载文件夹列表
        l=[]
        li=[]
        l.append("roleId")
        li.append(id)
        r=self.obj.get_c(6,self.f1,self.f2,l,li)
        self.write2excel(r,6,self.f2)
        #角色授权- 保存
        l = []
        li = []
        l.append("roleId")
        li.append(id)
        r = self.obj.post_c(7, self.f1, self.f2, l, li)
        self.write2excel(r, 7, self.f2)
        #成员新增
        l=[]
        li=[]
        l.append("loginName")
        li.append("cs")
        l.append("deptIdList")
        li.append([self.tenantId])
        l.append("dataIdList")
        li.append([self.tenantId])
        l.append("roleIdList")
        li.append([id])
        r=self.obj.post_c(11,self.f1,self.f2,l,li)
        self.write2excel(r,11,self.f2)
        #成员禁用
        id1=r.json()["data"]["id"]
        r=self.obj.get_v(12,id1,self.f1,self.f2)
        self.write2excel(r,12,self.f2)
        # 成员启用
        r = self.obj.get_v(13, id1, self.f1, self.f2)
        self.write2excel(r, 13, self.f2)
        # 成员锁定
        r = self.obj.get_v(14, id1, self.f1, self.f2)
        self.write2excel(r, 14, self.f2)
        # 成员解锁
        r = self.obj.get_v(15, id1, self.f1, self.f2)
        self.write2excel(r, 15, self.f2)
        #成员与组织机构解绑
        l=[]
        li=[]
        l.append("delList")
        li.append([id1])
        l.append("deptId")
        li.append(self.tenantId)
        r=self.obj.post_c(16,self.f1,self.f2,l,li)
        self.write2excel(r,16,self.f2)
        #未绑定部门的用户列表
        l=[]
        li=[]
        l.append("orgId")
        li.append(self.tenantId)
        r=self.obj.get_c(18,self.f1,self.f2,l,li)
        self.write2excel(r,18,self.f2)
        # 成员与组织机构绑定
        l = []
        li = []
        l.append("addList")
        li.append([id1])
        l.append("deptId")
        li.append(self.tenantId)
        r = self.obj.post_c(17, self.f1, self.f2, l, li)
        self.write2excel(r, 17, self.f2)
        #成员删除
        r=self.obj.get_v(19,id1,self.f1,self.f2)
        self.write2excel(r,19,self.f2)
        #删除角色
        r=self.obj.get_v(8,id,self.f1,self.f2)
        self.write2excel(r,8,self.f2)
    def test_003(self):
        #成员列表（分页）
        l=[]
        li=[]
        l.append("orgId")
        li.append(self.tenantId)
        r=self.obj.get_c(9,self.f1,self.f2,l,li)
        self.write2excel(r,9,self.f2)
        #角色列表
        r=self.obj.get_t(10,self.f1,self.f2)
        self.write2excel(r,10,self.f2)
if __name__ == '__main__':
    unittest.main()