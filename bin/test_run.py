import unittest
import os
import HTMLTestRunner
import time
from  tests import  *
if __name__ == '__main__':
    test_dir=os.path.join(os.path.dirname(os.path.dirname(__file__)),"tests")
    testcase=unittest.defaultTestLoader.discover(test_dir,pattern='test*.py')
    now=time.strftime("%Y-%m-%d_%H_%M_%S",time.localtime(time.time()))
    filepath="d:\\report\\"+now+".html"
    fp=open(filepath,'wb')
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title="接口自动化测试报告",description="ems")
    runner.run(testcase)
    fp.close()
