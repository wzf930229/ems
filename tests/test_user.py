from base.method import *
import unittest
from page.openS import *
from utils.excel_data import excel_data as e
class test_user(unittest.TestCase):
    def setUp(self):
        self.obj=method()
        self.excel_data =e()
        #获取实际结果列数
        self.r_col=self.excel_data.get_result_col()
        #获取响应时间列数
        self.t_col=self.excel_data.get_time_col()
        self.f = "public_url.json"
        self.f1="requestData_user.json"
        self.f2="data_user.xls"
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
        #查询文件夹列表
        r=self.obj.get_t(2,self.f1,self.f2)
        self.write2excel(r,2,self.f2)
    def test_003(self):
        #查询看板列表
        r=self.obj.get_t(3,self.f1,self.f2)
        self.write2excel(r,3,self.f2)

        '''
        total=r.json()["data"]["total"]
        if total>0:
            id=r.json()["data"]["rows"][0]["id"]
            #禁用看板
            l=[]
            li=[]
            l.append("id")
            li.append(id)
            r=self.obj.post_c(4,self.f1,self.f2,l,li)
            r=self.obj.get_v(5,id,self.f1,self.f2)
            print(r.text)
            self.write2excel(r,4,self.f2)
            '''
    def test_004(self):
        #新增我的计划
        r=self.obj.post_t(4,self.f1,self.f2)
        self.write2excel(r,4,self.f2)
        #编辑我的计划
        id=r.json()["data"]["id"]
        l=[]
        li=[]
        l.append("id")
        li.append(id)
        r=self.obj.post_c(5,self.f1,self.f2,l,li)
        self.write2excel(r,5,self.f2)
        #停用我的计划
        r=self.obj.get_v(6,id,self.f1,self.f2)
        self.write2excel(r,6,self.f2)
        # 启用我的计划
        r=self.obj.get_v(7,id,self.f1,self.f2)
        self.write2excel(r,7,self.f2)
        #看板详情
        l=[]
        li=[]
        l.append("id")
        li.append(id)
        r=self.obj.post_c(8,self.f1,self.f2,l,li)
        self.write2excel(r,8,self.f2)
        #任务日志
        l=[]
        li=[]
        l.append("boardPlanId")
        li.append(id)
        r=self.obj.post_c(9,self.f1,self.f2,l,li)
        self.write2excel(r,9,self.f2)
        #删除我的计划
        self.obj.get_v(6, id, self.f1, self.f2)
        r=self.obj.get_v(10,id,self.f1,self.f2)
        self.write2excel(r,10,self.f2)
    def test_005(self):
        #查询规则订阅
        r=self.obj.get_t(11,self.f1,self.f2)
        self.write2excel(r,11,self.f2)
        if len(r.json()["data"])>0:
            id=r.json()["data"][0]["id"]
            #订阅规则
            r=self.obj.get_v(12,id,self.f1,self.f2)
            self.write2excel(r,12,self.f2)
            #设置规则订阅
            r=self.obj.get_v(13,id,self.f1,self.f2)
            self.write2excel(r,13,self.f2)
            #保存
            l=[]
            li=[]
            l.append("subscriptionid")
            li.append(id)
            r=self.obj.post_c(14,self.f1,self.f2,l,li)
            self.write2excel(r,14,self.f2)
            #退订规则
            r=self.obj.get_v(15,id,self.f1,self.f2)
            self.write2excel(r,15,self.f2)
    def test_006(self):
        #查询订阅消息
        r=self.obj.post_t(16,self.f1,self.f2)
        self.write2excel(r,16,self.f2)
if __name__ == '__main__':
    unittest.main()