import xlrd
from Library.config import Config
from selenium import webdriver
class ReadExcel:
    def read_testdata(self,sheetname):
        wb = xlrd.open_workbook(Config.BOOK_MYSHOW_LOCATORSPATH)
        ws = wb.sheet_by_name(sheetname)
        columns = ws.ncols
        rows = ws.get_rows()
        header = next(rows)
        data = []
        for row in rows:
            if columns == 1:
                data.append(row[0].value)
            else:
                values =()
                for j in range(columns):
                    values += (row[j].value,)
            data.append(values)
        return data

    def read_locators(self,sheetname):
        wb = xlrd.open_workbook(Config.BOOK_MYSHOW_LOCATORSPATH)
        ws = wb.sheet_by_name(sheetname)
        rows = ws.get_rows()
        header = next(rows)
        dict = {}
        for row in rows:
            dict[row[0].value] = (row[1].value,row[2].value)
        return dict