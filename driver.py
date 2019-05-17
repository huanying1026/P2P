import unittest
import time
import os
import copy
from selenium import webdriver
from HTMLTestReportCN import HTMLTestRunner
from libs.PublicFunction import InsertLog_P
from libs.PublicFunction import GetSkipScripts_P
from libs.PublicFunction import GetSkipTestCases_P

#获取不需要执行的模块名称
ConfigFilePath = "./config.xlsx"
gs=GetSkipScripts_P()
m = gs.get_skip_scripts(ConfigFilePath)

#获取不需要执行的用例名称
TestCasePath = u"./cases/EDU_V1.0测试用例.xlsx"
st = GetSkipTestCases_P()
t = st.get_skip_testcases(TestCasePath)


#配置浏览器类型
bs = 'gc'

def create__browser_driver(b=bs):
    try:
        log = InsertLog_P()
        if b == 'gc':
            dv = webdriver.Chrome()
            log.info('打开谷歌浏览器')
        elif b == 'ff':
            dv = webdriver.Firefox()
        elif b == 'ie':
            dv = webdriver.Ie()
        else:
            pass

        return dv
    except BaseException as msg:
        log = InsertLog_P()
        log.error(msg)

## 筛选测试集
def get_test_suite(discover):
    #筛选出并去除不需要执行的脚本
    suite_m = copy.deepcopy(discover)
    for i in range(len(m)):
        for j in range(discover._tests.__len__()):
            d = discover._tests[j]
            if m[i] in str(d):
                suite_m._tests.remove(d)
    #筛选出并去除不需要执行的用例
    suite_c = copy.deepcopy(suite_m)
    for i in range(len(t)):
        for j in range(suite_m._tests.__len__()):
            s_m =  suite_m._tests[j]
            for z in range(s_m._tests.__len__()):
                s_c = s_m._tests[z]
                for k in range(s_c._tests.__len__()):
                    s_t = s_c._tests[k]
                    if t[i] == s_t._testMethodName:
                        suite_c._tests[j]._tests[z]._tests.remove(s_t)
    return suite_c

def run_test():
    try:
        dirpath = os.path.abspath(os.path.join(
            os.path.dirname(__file__), './scripts'))

        discover = unittest.defaultTestLoader.discover(dirpath, pattern='*_tc.py')

        s = get_test_suite(discover)

        currenttime = time.strftime('%y%m%d%H%M%S ')
        filedir = './reports/' + 'report_' + currenttime + '.html'
        fp = open(filedir, 'w',encoding='utf8')
        runner = HTMLTestRunner(stream=fp,
                                title='Edu自动化测试报告',
                                description=u'Edu在线教育平台V1.2自动化测试报告',
                                tester="测试大神")
        runner.run(s)
        fp.close()
        # f = GetNewReport()
        # SendEmail('pythondldysl01@163.com','wxqcl258258','2879237501@qq.com','smtp.163.com',f,25)
    except BaseException as msg:
        log = InsertLog_P()
        log.error(msg)

if __name__ == '__main__':
    run_test()