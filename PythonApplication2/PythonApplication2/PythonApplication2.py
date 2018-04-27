# -*- coding: utf-8 -*-
import xlrd

#xlsPath = r"D:\非煤40.xls"
#data = xlrd.open_workbook(xlsPath)

#table = data.sheets()[0]
#cols = table.col_values(8)
#nrows = table.row_values(5)
sum=0;
result = []
#str = table.cell(1,9).value
str="126.41526416,042.04265692;126.42039816,042.04173604;126.42282672,042.04340968;126.42400464,042.04253704;126.42273348,042.04166332;126.42130572,042.04041448;126.41595608,042.04155856;126.41587724,042.04153336;126.41585204,042.04157656;126.41591108,042.04159600;126.41493116,042.04242544"
points = str.split(';')

for j in points:
    xy = j.split(',')
    a = xy[0].strip('\n')#取消换行
    b = float(a)
    sum+=b
    result.append(b)
    print(b)


average = sum/len(result)
print("平均")
print (average)
