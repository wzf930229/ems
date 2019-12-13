from base.method import *
import unittest
from page.openS import *
from utils.excel_data import excel_data as e
from log import logger
import datetime
class test_rule(unittest.TestCase):
    def setUp(self):
        self.obj=method()
        self.excel_data =e()
        #获取实际结果列数
        self.r_col=self.excel_data.get_result_col()
        #获取响应时间列数
        self.t_col=self.excel_data.get_time_col()
        self.f = "public_url.json"
        self.f1="requestData_calendar.json"
        self.f2="data_calendar.xls"
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
        #财务日历-新增
        l=[]
        li=[]
        l.append("tenantId")
        li.append(self.tenantId)
        r=self.obj.post_c(2,self.f1,self.f2,l,li)
        self.write2excel(r,2,self.f2)
        #财务日历-编辑
        id=r.json()["data"]
        l = []
        li = []
        l.append("tenantId")
        li.append(self.tenantId)
        l.append("modCalendarId")
        li.append(id)
        r = self.obj.post_c(3, self.f1, self.f2, l, li)
        self.write2excel(r, 3, self.f2)
        #新增财务年
        startDate=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        endDate=(datetime.datetime.now()+datetime.timedelta(hours=6)).strftime("%Y-%m-%d %H:%M:%S")
        l=[]
        li=[]
        l.append("startDate")
        li.append(startDate)
        l.append("endDate")
        li.append(endDate)
        l.append("tenantId")
        li.append(self.tenantId)
        l.append("calendarDefId")
        li.append(id)
        r=self.obj.post_c(4,self.f1,self.f2,l,li)
        self.write2excel(r,4,self.f2)
        #编辑财务年
        id1=r.json()["data"]
        l=[]
        li=[]
        l.append("tenantId")
        li.append(self.tenantId)
        l.append("calendarDefId")
        li.append(id)
        l.append("id")
        li.append(id1)
        r=self.obj.post_c(5,self.f1,self.f2,l,li)
        self.write2excel(r,5,self.f2)
        #财务年详情
        l=[]
        li=[]
        l.append("tenantId")
        li.append(self.tenantId)
        l.append("calendarId")
        li.append(id)
        l.append("calendarYearId")
        li.append(id1)
        r=self.obj.get_c(6,self.f1,self.f2,l,li)
        self.write2excel(r,6,self.f2)
        # 设置企业财务日历
        r = self.obj.get_2v(7, self.tenantId, id, self.f1, self.f2)
        self.write2excel(r, 7, self.f2)
        #取消企业财务日历
        r=self.obj.get_2v(8,self.tenantId,id,self.f1,self.f2)
        self.write2excel(r,8,self.f2)
        #财务日历-获取财务日历树
        r=self.obj.get_t(9,self.f1,self.f2)
        self.write2excel(r,9,self.f2)
        #查询绑定财务日历的物业列表
        l=[]
        li=[]
        l.append("calendarId")
        li.append(id)
        r=self.obj.post_c(10,self.f1,self.f2,l,li)
        self.write2excel(r,10,self.f2)
        # 查询未绑定财务日历的物业列表
        l = []
        li = []
        l.append("calendarId")
        li.append(id)
        r = self.obj.post_c(11, self.f1, self.f2,l, li)
        self.write2excel(r, 11, self.f2)
        if r.json()["data"]["total"]>0:
            # 绑定物业
            shopPriIdList = r.json()["data"]["rows"][0]["id"]
            l = []
            li = []
            l.append("calendarId")
            li.append(id)
            l.append("shopPriIdList")
            li.append([shopPriIdList])
            r = self.obj.post_c(12, self.f1, self.f2, l, li)
            self.write2excel(r, 12, self.f2)
            # 解绑物业
            l = []
            li = []
            l.append("calendarId")
            li.append(id)
            l.append("shopPriIdList")
            li.append([shopPriIdList])
            r = self.obj.post_c(13, self.f1, self.f2, l, li)
            self.write2excel(r, 13, self.f2)
        #删除财务年
        r=self.obj.get_2v(14,id1,self.tenantId,self.f1,self.f2)
        self.write2excel(r,14,self.f2)
        #财务日历-删除
        l=[]
        li=[]
        l.append("tenantId")
        li.append(self.tenantId)
        l.append("calendarId")
        li.append(id)
        r=self.obj.post_c(15,self.f1,self.f2,l,li)
        self.write2excel(r,15,self.f2)
if __name__ == '__main__':
    unittest.main()