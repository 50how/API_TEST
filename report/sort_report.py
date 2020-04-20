import os

def new_report():
    """
    生成最新的测试报告文件
    :param testreport:
    :return:返回文件
    """
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    testreport = os.path.join(BASE_DIR, "report")
    lists = os.listdir(testreport)
    lists.sort(key=lambda fn: os.path.getmtime(testreport + "\\" + fn))
    file_new = os.path.join(testreport,lists[-1])
    return file_new

if __name__ == '__main__':
    print(new_report())