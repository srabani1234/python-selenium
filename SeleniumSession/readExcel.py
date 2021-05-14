import xlrd

workbook = xlrd.open_workbook("data.xlsx")
sheet = workbook.sheet_by_name("login")

totalrow = sheet.nrows
print(totalrow)
totalcol = sheet.ncols
print(totalcol)
for data in range(1,totalrow):
    username = sheet.cell_value(data,0)
    password = sheet.cell_value(data,1)
    print(username+" "+password)