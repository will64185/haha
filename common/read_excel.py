# coding=utf-8

import xlrd
import traceback
from datetime import datetime
from xlrd import xldate_as_tuple


class excelHandle:
    def decode(self, filename, sheetname):
        try:
            pass
        except Exception :
            print(traceback.print_exc())
        return filename, sheetname

    def read_excel(self, filename, sheetname):
        filename, sheetname = self.decode(filename, sheetname)
        rbook = xlrd.open_workbook(filename)
        sheet = rbook.sheet_by_name(sheetname)
        rows = sheet.nrows
        cols = sheet.ncols
        all_content = []
        for i in range(rows):
            if i > 0:
                row_content = []
                for j in range(cols):
                    ctype = sheet.cell(i, j).ctype  # 表格的数据类型
                    cell = sheet.cell_value(i, j)
                    if ctype == 2 and cell % 1 == 0:  # 如果是整形
                        cell = int(cell)
                    elif ctype == 3:
                        # 转成datetime对象
                        date = datetime(*xldate_as_tuple(cell, 0))
                        cell = date.strftime('%Y/%d/%m %H:%M:%S')
                    elif ctype == 4:
                        cell = True if cell == 1 else False
                    row_content.append(cell)
                all_content.append(row_content)
                # print('[' + ','.join("'" + str(element) + "'" for element in row_content) + ']')
        return all_content


if __name__ == '__main__':
    eh = excelHandle()
    filename = 'D:/will/workfile/haha/config//data.xlsx'
    sheetname = '滚动计划'
    a = eh.read_excel(filename, sheetname)
    print(a[1][1])

