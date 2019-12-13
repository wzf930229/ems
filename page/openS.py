#作者:Administrator
#时间:2019/10/20
import json
from xlutils import copy
from utils.operationJson import *
from utils.public import *
from utils import excel_data
import xlwt
import xlrd

operationJson=operationJson()
def set_key_val(row,f1,f2,l=[],li=[]):
    jsonData = json.loads(operationJson.get_json_data(row,f1,f2))
    for i in range(0, len(l)):
        jsonData[l[i]]=li[i]
    return jsonData
#将token写入到文件中
def writeToken(content):
    with open(data_dir("data","token"),"w") as f:
        f.write(content)
#将结果写入到excel中
def writeResult(row,col,content,f):
    #col=excel_data.excel_data().get_result_col()
    work=xlrd.open_workbook(data_dir("data",f))
    cwork=copy.copy(work)
    csheet=cwork.get_sheet(0)
    csheet.write(row,col,content)
    cwork.save(data_dir("data",f))