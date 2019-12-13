from base.method import *
import unittest
from page.openS import *
from utils.excel_data import excel_data as e
from log import logger
class test_tenant(unittest.TestCase):
    def setUp(self):
        self.obj=method()
        self.excel_data =e()
        #获取实际结果列数
        self.r_col=self.excel_data.get_result_col()
        #获取响应时间列数
        self.t_col=self.excel_data.get_time_col()
        self.f = "public_url.json"
        self.f1="requestData_tenant.json"
        self.f2="data_tenant.xls"
        self.tenantId=self.obj.get_tenantId(1,self.f,self.f2)
        self.logger=logger.logger(__name__)
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
        #组件标签列表
        r=self.obj.get_t(2,self.f1,self.f2)
        self.write2excel(r,2,self.f2)
    def test_003(self):
        #激活组件标签
        l=[]
        li=[]
        l.append("relationId")
        li.append(self.tenantId)
        r=self.obj.post_c(3,self.f1,self.f2,l,li)
        self.write2excel(r,3,self.f2)
    def test_004(self):
        #企业语言-查询企业所有语言
        r=self.obj.post_t(4,self.f1,self.f2)
        self.write2excel(r,4,self.f2)
        tenantLanguageCode = r.json()["data"]["rows"][0]["tenantLanguageCode"]
        id = r.json()["data"]["rows"][0]["id"]
        # 查询未使用的语言代码
        r = self.obj.get_t(5, self.f1, self.f2)
        self.write2excel(r, 5, self.f2)
        if len(r.json()["data"]["unusedlist"]) > 0:
            tenantLanguageCode = r.json()["data"]["unusedlist"][0]["isoCode"]
            l = []
            li = []
            l.append("tenantLanguageCode")
            li.append(tenantLanguageCode)
            # 企业语言-新增按钮
            r = self.obj.post_c(6, self.f1, self.f2, l, li)
            self.write2excel(r, 6, self.f2)
            # 企业语言-编辑按钮
            id = r.json()["data"]["id"]
            l = []
            li = []
            l.append("tenantLanguageCode")
            li.append(tenantLanguageCode)
            l.append("id")
            li.append(id)
            r = self.obj.post_c(7, self.f1, self.f2, l, li)
            self.write2excel(r, 7, self.f2)
            # 企业语言-删除按钮
            r = self.obj.get_v(8, id, self.f1, self.f2)
            self.write2excel(r, 8, self.f2)
        else:
            self.logger.getlogger().debug("没有可使用的语言代码")
            # 企业语言-编辑按钮
            l = []
            li = []
            l.append("tenantLanguageCode")
            li.append(tenantLanguageCode)
            l.append("id")
            li.append(id)
            r = self.obj.post_c(7, self.f1, self.f2, l, li)
            self.write2excel(r, 7, self.f2)
            # 企业语言-删除按钮
            r = self.obj.get_v(8, id, self.f1, self.f2)
            self.write2excel(r, 8, self.f2)
    def test_005(self):
        #查询币种列表
        r=self.obj.get_t(9,self.f1,self.f2)
        self.write2excel(r,9,self.f2)
        #新增币种
        r=self.obj.post_t(10,self.f1,self.f2)
        self.write2excel(r,10,self.f2)
        #根据ID查询企业币种信息
        id=r.json()["data"]["id"]
        r=self.obj.get_v(11,id,self.f1,self.f2)
        self.write2excel(r,11,self.f2)
        #编辑币种
        l=[]
        li=[]
        l.append("id")
        li.append(id)
        l.append("tenantId")
        li.append(self.tenantId)
        r=self.obj.post_c(12,self.f1,self.f2,l,li)
        self.write2excel(r,12,self.f2)
        # 新增汇率
        tenantCurrCode=r.json()["data"]["tenantCurrCode"]
        l=[]
        li=[]
        l.append("shopCurrCode")
        li.append(tenantCurrCode)
        r = self.obj.post_c(14,self.f1,self.f2,l,li)
        self.write2excel(r, 14, self.f2)
        id1=r.json()["data"]["id"]
        # 查询汇率列表
        r = self.obj.get_c(15,self.f1,self.f2,l,li)
        self.write2excel(r, 15, self.f2)
        # 编辑汇率
        l = []
        li = []
        l.append("id")
        li.append(id1)
        l.append("shopCurrCode")
        li.append(tenantCurrCode)
        r = self.obj.post_c(16, self.f1, self.f2, l, li)
        self.write2excel(r, 16, self.f2)
        # 删除汇率
        l = []
        li = []
        l.append("ids")
        li.append([id1])
        r = self.obj.post_c(17, self.f1, self.f2, l, li)
        self.write2excel(r, 17, self.f2)
        #删除币种
        r=self.obj.get_v(13,id,self.f1,self.f2)
        self.write2excel(r,13,self.f2)
    def test_006(self):
        #获取企业订阅规则列表
        r=self.obj.get_t(18,self.f1,self.f2)
        self.write2excel(r,18,self.f2)
        if len(r.json()["data"])>0:
            # 企业管理-规则设置-编辑按钮
            id = r.json()["data"][0]["id"]
            flag = r.json()["data"][0]["openFlag"]
            if flag == 0:
                openFlag = 1
            else:
                openFlag = 0
            ruleConf = r.json()["data"][0]["ruleConf"]
            ruleId=r.json()["data"][0]["ruleId"]
            l=[]
            li=[]
            l.append("busiTenantRuleBaseDTOS")
            li.append([{"id":id,"openFlag":openFlag,"ruleConf":ruleConf,"ruleId":ruleId}])
            r=self.obj.post_c(19,self.f1,self.f2,l,li)
            self.write2excel(r,19,self.f2)
            #新增邮件模板
            r=self.obj.post_t(20,self.f1,self.f2)
            self.write2excel(r,20,self.f2)
            #租户设置-邮件模板-编辑按钮
            id=r.json()["data"]["id"]
            l=[]
            li=[]
            l.append("id")
            li.append(id)
            r=self.obj.post_c(21,self.f1,self.f2,l,li)
            self.write2excel(r, 21, self.f2)
            #租户设置-邮件模板-启用按钮
            r=self.obj.get_v(22,id,self.f1,self.f2)
            self.write2excel(r,22,self.f2)
            #租户设置-邮件模板-禁用按钮
            r = self.obj.get_v(23, id, self.f1, self.f2)
            self.write2excel(r, 23, self.f2)
            #租户设置 - 邮件模板 - 删除按钮
            r = self.obj.get_v(24, id, self.f1, self.f2)
            self.write2excel(r, 24, self.f2)
if __name__ == '__main__':
    unittest.main()