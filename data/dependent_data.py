from util.log import log
from util.operation_excel import OperationExcel
from base.runmethod import RunMethod
from data.get_data import GetData
from jsonpath_rw import jsonpath, parse #pip install jsonpath-rw
import json
import re


key_values = [] #list存依赖ID匹配到的值，1个或多个
case_value={} #{caseid：{id1：1}}

class DependentData:
    """解决数据依赖问题"""

    def __init__(self, case_id):
        self.case_id = case_id
        self.opera_excel = OperationExcel()
        self.data = GetData()
        case_value[case_id]={} #先创建空的字典之后存{caseid：{id1：1}}

    def get_case_line_data(self):
        """
        通过case_id去获取该case_id的整行数据
        :param case_id: 用例ID
        :return:
        """
        rows_data = self.opera_excel.get_row_data(self.case_id)
        return rows_data

    def run_dependent(self):
        """
        查询依赖caseid的响应数据并返回
        :return:
        """
        row_num = self.opera_excel.get_row_num(self.case_id)
        res = self.data.get_respond_data(row_num)
        rj=json.loads(res)
        return rj

    def get_data_for_key(self, row):
        """
        根据依赖的key去获取执行依赖case的响应然后返回
        :return:依赖字段+依赖值 [id1:3]
        """
        log_key = None
        try:
            response_data = self.run_dependent()
            depend_data = self.data.get_depend_key(row)
            log().info('开始解析依赖字段 %s',depend_data)
            depend_k_v=str_to_dict(depend_data)
            end_key={}

            for key in depend_k_v:
                log_key=key
                if not re.search(r'\d', key):
                    key_findvalue(response_data, key)
                else:
                    r = re.compile(r'\d')
                    str=r.sub('',key)
                    key_findvalue(response_data, str)

                end_key[key]=key_values[depend_k_v[key]]
                key_values.clear()

            case_value[self.case_id].update(end_key) #{caseid：{id1:1,id2:2}}
            log().info('依赖字段解析完成\n%s',case_value)
            return case_value

        except Exception as e:
            log().error('在%s的响应结果中没有找到依赖字段%s',self.case_id,log_key)
            return


def key_findvalue(jsons, key):
            """
            通过依赖参数key，在jsons中进行匹配并输出该key对应的value
            :param jsons: 需要解析的json串
            :param key: 需要查找的key
            :return:
            """
            global key_values
            key_value = ''

            if isinstance(jsons, dict):
                for json_result in jsons.keys():
                    if key ==json_result:
                        key_value = jsons.get(key)
                        if key_value !='':
                            if key_value not in key_values:
                                if isinstance(key_value,dict):
                                    key_findvalue(key_value, key)
                                elif isinstance(key_value,list):
                                    for l in key_value:
                                        key_findvalue(l, key)
                                else:key_values.append(key_value)#临时解决办法

                    elif isinstance(jsons.get(json_result),dict):
                        key_findvalue(jsons.get(json_result), key)
                    elif isinstance(jsons.get(json_result),list):
                        for i in jsons.get(json_result):
                            key_findvalue(i, key)
                    else:pass

            elif isinstance(jsons, list):
                for json_array in jsons:

                    key_findvalue(json_array, key)

            # if key_value != '':
            #     print(key_value)

def str_to_dict(st):
    """
    传入依赖字段解析为字段+匹配位置，默认匹配第0个
    :param st: 需要解析的依赖字段
    :param :
    :return:解析后{字段+位置}
    """

    d={}
    if ',' in st:
        strlist = st.split(',')
        for x in strlist:
            if not re.search(r'\d', x):
                d[x]=0
            else:
                m=''
                for b in re.findall(r'\d',x):
                        #r = re.compile(r'\d')
                        #d[r.sub('',x)]=int(b)
                        m+=b
                d[x] = int(m)
                m=''

    else:
        if not re.search(r'\d', st):
            d[st]=0
        else:
            m=''
            #r = re.compile(r'\d')
            for n in re.findall(r'\d',st):
                #d[r.sub('',st)]=int(n)
                m+=n
            d[st] = int(m)
    log().info('字段解析中 %s',d)
    return d