import unittest
from ddt import ddt,data
# from util.send_email import SendEmail
import main.unit
from util.log import log
from report import sort_report
run = main.unit.RunTest()

lines=run.data.get_case_lines()

name_row={}
for i in range(1, lines):
    if run.data.get_is_run(i):
        name=run.data.get_case_name(i)
        name_row[name]=i
@ddt
class TestStringMethods(unittest.TestCase):

    @data(*name_row)
    def test_(self,name):
        row=name_row[name]
        self.assertIn(run.data.get_expcet_data(row,False), run.go_on_run(row),"与预期结果不一致")

    def tearDown(self):
        pass






if __name__ == '__main__':
    unittest.main()