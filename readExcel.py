import os
import getpathInfo

from xlrd import open_workbook
path = getpathInfo.get_path()

class readExcel():
    def get_xls(self, xls_name, sheet_name):  # xls_name填写用例的Excel名称 sheet_name该Excel的sheet名称
        cls = []
        xlsPath = os.path.join(path,"testFile",'case',xls_name)
        file = open_workbook(xlsPath)
        sheet = file.sheet_by_name(sheet_name)
        
        nrows = sheet.nrows
        
        for i in (nrows):
            if sheet.rows_values(i)[0] != 'case_name':
                cls.append(sheet.row_values(i))
                return cls

if __name__ == '__main__':
    print(readExcel().get_xls('userCase.xlsx', 'login'))
    print(readExcel().get_xls('userCase.xlsx', 'login')[0][1])
    print(readExcel().get_xls('userCase.xlsx', 'login')[1][2])