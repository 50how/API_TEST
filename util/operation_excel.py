import xlrd #pip install xlrd
from xlutils.copy import copy #pip install xlutils

from util.log import log


class OperationExcel:
    """操作excel"""

    def __init__(self, file_name=None, sheet_id=None):
        if file_name:
            self.file_name = file_name
            self.sheet_id = sheet_id
        else:
            self.file_name = '../dataconfig/case.xls'
            self.sheet_id = 0
        self.data = self.get_data()

    def get_data(self):
        """
        获取sheets的内容
        :return:
        """
        data = xlrd.open_workbook(self.file_name,encoding_override='utf-8')
        tables = data.sheets()[self.sheet_id]
        return tables

    def get_lines(self):
        """
        获取单元格行数
        :return:
        """
        tables = self.data
        return tables.nrows

    def get_cell_value(self, row, col):
        """
        获取单元格数据
        :param row: 行
        :param col: 列
        :return:
        """
        tables = self.data
        cell = tables.cell_value(row, col)
        return cell

    def write_value(self, row, col, value):
        """
        回写数据到excel
        :param row:行
        :param col:列
        :param value:值
        :return:
        """
        read_data = xlrd.open_workbook(self.file_name)
        write_data = copy(read_data)
        sheet_data = write_data.get_sheet(0)
        sheet_data.write(row, col, value)
        try:
            write_data.save(self.file_name)
        except:
            log().error('excel读取失败')

    def get_row_data(self, case_id):
        """
        根据对应的case_id获取对应行的内容
        :param case_id: 用例id
        :return:
        """
        row_num = self.get_row_num(case_id)
        row_data = self.get_row_value(row_num)
        return row_data

    def get_row_num(self, case_id):
        """
        根据case_id获取对应行号
        :param case_id:
        :return:
        """
        num = 0
        cols_data = self.get_cols_data()
        for col_data in cols_data:
            if case_id in col_data:
                return num
            num = num + 1

    def get_row_value(self, row):
        """
         根据行号，找到该行的内容
        :param row:行号
        :return:

        """
        tables = self.data
        row_data = tables.row_values(row)
        return row_data

    def get_cols_data(self, col_id=None):
        """
        获取某一列的内容
        :param col_id:列号
        :return:
        """
        if col_id != None:
            cols = self.data.col_values(col_id)
        else:
            cols = self.data.col_values(0)
        return cols


if __name__ == '__main__':
    opera = OperationExcel()
    opera.get_data()
    print(opera.get_data().nrows)
    print(opera.get_lines())
    print(opera.get_cell_value(1, 2))
