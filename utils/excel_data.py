#作者:Administrator
#时间:2019/10/19
import sys
import os
from utils.public import *
from utils.operationJson import *
from utils.operationExcel import *
import json
class excel_data:
    def __init__(self):
        self.caseId=0
        self.url=2
        self.data=3
        self.expect=4
        self.result=5
        self.time=6
    def get_caseId_col(self):
        return self.caseId
    def get_url_col(self):
        return self.url
    def get_data_col(self):
        return self.data
    def get_expect_col(self):
        return self.expect
    def get_result_col(self):
        return self.result
    def get_time_col(self):
        return self.time
#从token文件中获取token
def get_token():
    with open(data_dir("data","token"),"r",encoding="utf-8") as f:
        token=f.read()
    return token
#不带token的头信息
def getHeader():
    headers={
        "content-type":"application/json",
        "Cookie":"noLoginLanguage=zh; oms_lang=zh; ems_lang=zh",
        "Referer":"https://sdptest.shijicloud.com/open_source_pro/",
         "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
    }
    return headers
#带token的头信息
def getHeader_token():
    headers = {
        "authorization":get_token(),
        "content-type": "application/json",
        "Cookie": "noLoginLanguage=zh; oms_lang=zh; ems_lang=zh",
        "Referer": "https://sdptest.shijicloud.com/open_source_pro/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
    }
    return headers


