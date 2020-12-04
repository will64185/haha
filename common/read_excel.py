import csv

class ReadExcel():
    def __init__(self, excelPath):
        self.data = xlrd.open_workbook(excelPath)
        self.table = self.csv.reader(open(excelPath, 'r'))


    def dict_data(self):
        if self.rowNum <= 1:
            print("总行数小于1")
        else:
            r = []
            j=1
            for i in range(self.rowNum-1):
                s = {}
                # 从第二行取对应values值
                values = self.table.row_values(j)
                for x in range(self.colNum):
                    s[self.keys[x]] = values[x]
                r.append(s)
                j+=1
        return r

if __name__ == "__main__":
    filepath = "C://Users//will//Desktop//haha//config//data.xlsx"
    data = ReadExcel(filepath)
    print(data.dict_data())