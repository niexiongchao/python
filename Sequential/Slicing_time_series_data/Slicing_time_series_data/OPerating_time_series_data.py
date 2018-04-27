import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from Slicing_time_series_data import read_data

#定义输入文件名
input_file = 'data_2D.txt'

#加载第三列和第四列，分别赋值给两个变量

x1 = read_data(input_file,2)
x2 = read_data(input_file,3)

#创建一个Pandas dataframe对象,包含x1,x2两维
data =pd.DataFrame({'dim1':x1,'dim2':x2})#从字典对象导入数据，Key是列名，Value是数据

#画出指定开始和结束年份的数据图像
start ='1968'
end = '1975'
data[start:end].plot()
plt.title('data overlapped on top of each other')

#
#使用条件过滤数据并显示，这次，我们设置的条件是dim中的所有值小于45，dim2中所有值大于30
#"dim1" 是比限定条件更小
#"dim2"是比限定条件更大
data[(data['dim1']<45)&(data['dim2']>30)].plot()
plt.title('dim1 <45 and dim2 > 30')


#添加两个dataFrame
plt.figure()#绘制图画
diff =data[start:end]['dim1'] + data[start:end]['dim2']
diff.plot()
plt.title('Summation(dim1+dim2)')
plt.show()
