#作者:Administrator
#时间:2019/10/19
import xlrd
from utils.public import *
from utils import excel_data
from utils.operationJson import *
class operationExcel:
    def __init__(self):
        self.exdata=excel_data.excel_data()
    def getExcel(self,f):
        db=xlrd.open_workbook(data_dir("data",f))
        sheet=db.sheet_by_index(0)
        return sheet
    def get_rows(self,f):
        return self.getExcel(f).nrows
    def get_value(self,row,col,f):
        return self.getExcel(f).cell_value(row,col)
    def get_caseId(self,row,f):
        return self.get_value(row,self.exdata.get_caseId_col(),f)
    def get_url(self,row,f):
        return self.get_value(row,self.exdata.get_url_col(),f)
    def get_data(self,row,f):
        return self.get_value(row,self.exdata.get_data_col(),f)
    def get_expect(self,row,f):
        return self.get_value(row,self.exdata.get_expect_col(),f)



