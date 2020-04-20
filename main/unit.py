# import sys
# import os
# curPath = os.path.abspath(os.path.dirname(__file__))
# rootPath = os.path.split(curPath)[0]
# sys.path.append(rootPath)

from base.runmethod import RunMethod
from data.get_data import GetData
from util.common_util import CommonUtil
from data.dependent_data import DependentData
# from util.send_email import SendEmail
from util.operation_header import OperationHeader
from util.operation_json import OperationJson
from requests_toolbelt import MultipartEncoder
import json
import logging
from util.log import log

class RunTest:

    def __init__(self):
        self.run_method = RunMethod()
        self.data = GetData()
        self.com_util = CommonUtil()
        # self.send_email = SendEmail()

    def go_on_run(self,i):
        pass_count = []
        fail_count = []
        request_data_file = ''
        res = None
        # 获取用例数
        rows_count = self.data.get_case_lines()
        # 第一行索引为0
        # for i in range(1, rows_count):
        is_run = self.data.get_is_run(i)
        if is_run:
            url = self.data.get_request_url(i)
            method = self.data.get_request_method(i)
            #request_data = json.load(self.data.get_request_data(i))
            expect = self.data.get_expcet_data(i)
            token = self.data.is_token(i)
            depend_case = self.data.is_depend(i)
            headers= self.data.get_headers(i)
            r = self.data.get_request_data(i)
            self.data.write_respond_data(i, '')#清空响应信息


            # 上传文件处理
            if r!=None:
                if r.endswith('jpg')| r.endswith('png')| r.endswith('docx')| r.endswith('doc')| r.endswith('ppt')| r.endswith('pptx'):#其他文件暂不考虑
                    log().info('读取上传文件')
                    file_payload = {'file': (r, open('../' + r, 'rb'))}#, "image/jpg"
                    m = MultipartEncoder(file_payload)
                    headers['Content-Type'] = m.content_type
                    request_data = m
                    log().info('生成上传文件Multipart')
                #处理依赖
                elif depend_case != None:
                    self.depend_data = DependentData(depend_case)
                    # 获取依赖key和value [id1:3]
                    depend_response_data = self.depend_data.get_data_for_key(i)  # {caseid：{id1:1,id2:2}}
                    for caseid in depend_response_data:
                        for k in depend_response_data[caseid]:
                            y = '${' + caseid + ',' + k + '}'
                            if r.find(y):
                                t = r.replace(y, str(depend_response_data[caseid][k]))
                                r = t
                    log().info('依赖(最终)请求拼接完成\n%s', r)
                    request_data = json.loads(r, encoding='utf-8')

                else:# 没有依赖直接转换输出
                        log().info('获取没有依赖的请求参数\n%s',r)
                        request_data =json.loads(r,encoding='utf-8')

            else:
                request_data={}

            # 如果token字段值为write则将该接口的返回的token写入到token.json文件，如果为yes则读取token.json文件
            if token == "write":
                log().info('写入token')
                res = self.run_method.run_main(method, url,request_data,headers)
                op_header = OperationHeader(res)
                op_header.write_token()
            elif token == 'yes':
                op_json = OperationJson("../dataconfig/token.json")
                token = op_json.get_data('data')
                log().info("获取token\n%s",token)
                headers.update(token)
                #request_data = dict(request_data, **token)  # 把请求数据与登录token合并，并作为请求数据
                res = self.run_method.run_main(method, url,request_data,headers)

            else:

                res = self.run_method.run_main(method, url,request_data,headers)
            log().info("响应结果\n%s", res)
            self.data.write_respond_data(i, res)

            if expect != None:
                if self.com_util.is_contain(expect, res):
                    self.data.write_result(i, "Pass")
                    pass_count.append(i)

                else:
                    self.data.write_result(i, "failed")
                    fail_count.append(i)

            else:

                log().error('用例ID：case-%s，预期结果不能为空',i)

            return res


    # 发送邮件
    # self.send_email.send_main(pass_count, fail_count)

        # print(f"通过用例数：{len(pass_count)}")
        # print(f"失败用例数：{len(fail_count)}")

