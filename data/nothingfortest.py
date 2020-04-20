import json
from jsonpath_rw import jsonpath, parse
import re
import chardet
from data.get_data import GetData
from urllib.parse import urlencode, quote, unquote
import requests
from util.operation_json import OperationJson
from requests_toolbelt import MultipartEncoder
# import io
# import sys
# import logging
# logger = logging.getLogger('mylog')
# logger.setLevel(logging.DEBUG)
# log_cap = io.StringIO()
# handler = logging.StreamHandler(log_cap)
#
# handler.setLevel(logging.DEBUG)
# formatter = logging.Formatter(
#     '[%(levelname)s][%(asctime)s] [%(filename)s]->[%(funcName)s] line:%(lineno)d ---> %(message)s')
# handler.setFormatter(formatter)
# logger.addHandler(handler)
# s='2'
# logger.debug('23421%s',s)
# logger.info('34243')
# print(log_cap.getvalue())
# import sys
# import os
# curPath = os.path.abspath(os.path.dirname(__file__))
# rootPath = os.path.split(curPath)[0]
# c='C:\\Users\\Administrator.AVIEGX0QQXBXQAV\\PycharmProjects\\untitled\\venv\\Lib\\site-packages\\'
# sys.path.append(c)
# sys.path.append(rootPath)
# print(sys.path)
# i='1'
# print('用例ID：case-%s，预期结果不能为空'%i)
# import logging
#
# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# logger = logging.getLogger(__name__)
#
# logger.info('This is a log info')
# logger.debug('Debugging')
# logger.warning('Warning exists')
# logger.info('Finish')
# try:
#     result = 10 / 0
# except Exception:
#     logger.error('Faild to get result', exc_info=True)
#
# logger.info('Finished')

# data = GetData()
# s=data.get_request_data(4)
#
# h=data.get_headers(10)
# t=str(h)
# import unittest
# from ddt import ddt,data
# d={'1':'23','2':'23'}
# @ddt
# class test(unittest.TestCase):
#     @data(*d)
#     def testd(self,v):
#         print(v)
# if __name__ == '__main__':
#     unittest.main()

# def header_ditc(t):
#     dt = {}
#     if ':'in t:
#         if '\n'in t:
#             cell=t.split('\n')
#             for headers in cell:
#                 headers_k_v=headers.split(':')
#                 dt[headers_k_v[0]]=headers_k_v[1]
#         else:
#             headers_k_v=t.split(':')
#             dt[headers_k_v[0]] = headers_k_v[1]
#     else:
#         return dt
#     return dt
#
# print(header_ditc(t))

#print(chardet.detect(str.encode(s)))

# print(unquote(s))
# fileName = '../dataconfig/case.xls'
#
# currentFile = open(fileName,mode='rb')
# content = currentFile.read()
#
# print(chardet.detect(content))
#
# print (json.dumps(s, ensure_ascii=True))
# print(json.loads(s,encoding='utf-8'))
#



#header = {'Content-Type':'multipart/form-data','name':'file','filename':'01.jpg'}
# file_payload = {'file': ("login.jpg", open('c:\\w.jpg', 'rb'), "image/jpg")}
# op_json = OperationJson("../dataconfig/token.json")
# m=MultipartEncoder(file_payload)
# header = op_json.get_data('data')
# header['Content-Type'] = m.content_type
# print(header)
#
# d=requests.post('https://platform-test.dtedu.com/dt-ecampus/file/file/upload'
#                 ,headers=header,data=m,verify=False)
#
# print(d.json())


#
# st='case'
# ds={st:{}}
# e={'id1':'123'}
# s={'id2':'123'}
# ds[st].update(e)
# ds[st].update(s)
# print(ds)
#
# for i in ds:
#     print(i)
#     for k in ds[i]:
#         print(k)
#         print(ds[i][k])
import json
from jsonpath_rw import jsonpath, parse
import re
# from data.get_data import GetData
# a_dict ={"service":{"core":"01","id":{"usid":"110","us":[{"s":"l"}]}},"client":"browser","username":"15986413434","password":"12345655"}
# # key='core'
# # a_str = json.loads(a_dict)
# # s ='[\'service\'][\'id\'][\'us\'][0][\'s\']'
# data = GetData()
# s=data.get_request_data(3)
# k='${'+'name'+'}'
# if s.find(k):
#     f=s.replace(k,'123')
#     s=f
#     print(s)
# s='e'
# print(s.encode('utf-8'))
#print(a_dict['service']['id']['us'][x]['s'])
#print(type(a_dict.keys()).__name__)

# st1 ='id2,id1,id3'
#
# def e(st):
#     d = {}
#     if ',' in st:
#         strlist = st.split(',')
#         for x in strlist:
#             if not re.search(r'\d', x):
#                 d[x]=0
#             for b in re.findall(r'\d',x):
#                     r = re.compile(r'\d')
#                     #d[r.sub('',x)]=int(b)
#                     d[x]=int(b)
#
#
#     else:
#         if not re.search(r'\d', st):
#             d[st]=0
#         else:
#             r = re.compile(r'\d')
#             for n in re.findall(r'\d',st):
#             #     d[r.sub('',st)]=int(n)
#                     d[st]=int(n)
#     return d
#
# print(e(st1))
# for i in e(st1):
#     print(i)
# st2=e(st1)
# st3={}
# for i in st2:
#     st3[i+str(st2[i])]=0
# print(st3)
# class t:
#     d=[]
#
#     def b(self):
#         self.d.append(1)
#         print(self.d)
# t().b()



#print(type(a_str['client']).__name__ )
# for k,v in a_str.items():
#     print(a_str[])

# for i in a_str:
#     if type(a_str[i]).__name__ =='str':
#         #print(a_str.__getitem__(i))
#         pass
#
#     elif type(a_str[i]).__name__ =='dict':
#         for k in a_str[i]:
#             if k =='core':
#                 print(a_str[i][k])
#             for s in a_str[i][k]:
#                  print(s)


# def get_res(dep, res):
#     for i in res:
#         if i == dep:
#             print( res.__getitem__(i))
#
#         elif type(res[i]).__name__ == 'dict':
#                 for k in res[i]:
#                         if k == dep:
#                             print(res[i][k])
#                         for s in res[i][k]:
#                             print(s)
#
# # print(a_str.__getitem__('service'))
#
# get_res(key,a_str)

# def analyze_json(jsons):
#     """
#     解析传进来的jsons,将jsons解析成key-value并输出
#     :param jsons: 需要解析的json字符串
#     :return:
#     """
#     key_value = ''
#     # isinstance函数是Python的内部函数，他的作用是判断jsons这个参数是否为dict类型
#     # 如果是的话返回True，否则返回False
#     if isinstance(jsons, dict):
#         for key in jsons.keys():
#             key_value = jsons.get(key)
#             if isinstance(key_value, dict):
#                 analyze_json(key_value)
#             elif isinstance(key_value, list):
#                 for json_array in key_value:
#                     analyze_json(json_array)
#             else:
#                 print(str(key) + " = " + str(key_value))
#     elif isinstance(jsons, list):
#         for json_array in jsons:
#             analyze_json(json_array)


# def output_value(jsons, key):
#     """
#     通过参数key，在jsons中进行匹配并输出该key对应的value
#     :param jsons: 需要解析的json串
#     :param key: 需要查找的key
#     :return:
#     """
#     key_value = ''
#     if isinstance(jsons, dict):
#         for json_result in jsons.values():
#             if key in jsons.keys():
#                 key_value = jsons.get(key)
#             else:
#                 output_value(json_result, key)
#     elif isinstance(jsons, list):
#         for json_array in jsons:
#             output_value(json_array, key)
#     if key_value != '':
#         print(str(key) + " = " + str(key_value))

