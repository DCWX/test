# -*- utf-8 -*-
#@Time    :2019/9/1023:06
#@Author  :无邪
#@File    :test_case_data.py
#@Software:PyCharm
import unittest
from ddt import ddt,data
from common.read_excel import ReadExcel
from common.split_path import SplitPsth
from common.http_request import HttpRequest
from common.w_log import Mylog

@ddt#装饰测试类
class TestCaseData(unittest.TestCase):
    """单元测试"""
    case=ReadExcel(SplitPsth().split_case(), "Sheet1")
    cases=case.choice()
    # print(cases)
    def setUp(self):
        print("开始执行测试")
    #装饰测试用例
    @data(*cases)
    def test_cases(self,testdata):
        res=HttpRequest().request_start(testdata["Method"],eval(testdata["Params"]),testdata["url"])
        print(res)
        try:
            self.assertEqual(eval(testdata["ExpectedResult"]),res)
            print("用例执行通过")
        except AssertionError as e:
            print("用例不通过，实际结果{}与预期结果{}不一致".format(res,eval(testdata["ExpectedResult"])))
            Mylog().log_debug(e)
            raise e
        finally:
           self.case.write_excel(testdata["Case_id"]+1,8,str(res))
    def tearDown(self):
        print("测试执行结束")



if __name__ == '__main__':
        TestCaseData().test_cases()

