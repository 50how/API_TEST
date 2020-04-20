from util.log import log
from util.operation_excel import OperationExcel
from data import data_config


class GetData:
    """获取excel数据"""

    def __init__(self):
        self.opera_excel = OperationExcel()

    def get_case_lines(self):
        """获取excel行数，即case的个数"""
        return self.opera_excel.get_lines()

    def get_case_name(self, row):
        """获取是否执行"""
        col = int(data_config.get_name())
        case_name = self.opera_excel.get_cell_value(row, col)
        return case_name


    def get_is_run(self, row):
        """获取是否执行"""
        flag = None
        col = int(data_config.get_run())
        run_model = self.opera_excel.get_cell_value(row, col)
        if run_model == 'yes':
            flag = True
        else:
            flag = False
        return flag

    def get_headers(self, row):
        """
        获取携带的headers
        :param row: 行号
        :return:
        """
        col = int(data_config.get_headers())
        header = self.opera_excel.get_cell_value(row, col)
        h={}
        if header:
            h=header_str_dict(header)
            log().info('获取请求头\n%s',h)
            return h
        else:
            log().info('没有请求头')
            return h


    def is_token(self, row):
        """
        是否携带header
        :param row: 行号
        :return:
        """
        col = int(data_config.get_token())
        token = self.opera_excel.get_cell_value(row, col)
        if token != '':
            log().info('获取是否携带token %s',token)
            return token
        else:
            log().info('获取是否携带token为空')
            return None

    def get_request_method(self, row):
        """
        获取请求方式
        :param row: 行号
        :return:
        """
        # col 列
        col = int(data_config.get_run_way())
        request_method = self.opera_excel.get_cell_value(row, col)
        log().info('获取请求方式 %s',request_method)
        return request_method

    def get_request_url(self, row):
        """
        获取url
        :param row: 行号
        :return:
        """
        col = int(data_config.get_url())
        url = self.opera_excel.get_cell_value(row, col)
        log().info('获取请求地址\n%s',url)
        return url

    def get_request_data(self, row):
        """
        获取请求数据
        :param row:行号
        :return:
        """
        col = int(data_config.get_data())
        request_data = self.opera_excel.get_cell_value(row, col)
        if request_data == '':
            log().info('没有请求参数')
            return None
        # r=json.loads(request_data) #将str转为dict
        log().info('获取请求参数')
        return request_data

    def get_expcet_data(self, row,_log=True):
        """
        获取预期结果
        :param row:
        :return:
        """
        col = int(data_config.get_expect())
        expect = self.opera_excel.get_cell_value(row, col)
        if expect == "":
            log().error('预期结果为空')
            return None
        else:
            if _log:
                log().info('获取预期结果 %s',expect)
            return expect

    def get_respond_data(self, row):
        """
        获取预期结果
        :param row:
        :return:
        """
        col = int(data_config.get_resond())
        respond = self.opera_excel.get_cell_value(row, col)
        if respond == "":
            return None
        else:
            return respond

    def write_result(self, row, value):
        """
        写入结果数据
        :param row:
        :param col:
        :return:
        """
        col = int(data_config.get_result())
        self.opera_excel.write_value(row, col, value)

    def write_respond_data(self, row, value):
        """
        写入响应数据
        :param row:
        :param col:
        :return:
        """
        col = int(data_config.get_resond())
        self.opera_excel.write_value(row, col, value)

    def get_depend_key(self, row):
        """
        获取依赖数据的key
        :param row:行号
        :return:
        """
        col = int(data_config.get_data_depend())
        depend_key = self.opera_excel.get_cell_value(row, col)

        if depend_key == "":
            return None
        else:
            return depend_key

    def is_depend(self, row):
        """
        判断是否有case依赖
        :param row:行号
        :return:
        """
        col = int(data_config.get_case_depend())  # 获取是否存在数据依赖列
        depend_case_id = self.opera_excel.get_cell_value(row, col)
        if depend_case_id == "":
            log().info('没有数据依赖')
            return None
        else:
            log().info('获取依赖%s',depend_case_id)
            return depend_case_id

def header_str_dict(header_str):
    """
    headers的str转换为dict
    :param header_str:
    :return: dict
    """

    dt = {}
    if ':' in header_str:
        log().info('请求头格式转换')
        if '\n' in header_str:
            cell = header_str.split('\n')
            for headers in cell:
                headers_k_v = headers.split(':')
                dt[headers_k_v[0]] = headers_k_v[1]
        else:
            headers_k_v = header_str.split(':')
            dt[headers_k_v[0]] = headers_k_v[1]
    else:
        return dt
    return dt

