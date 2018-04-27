import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from Slicing_time_series_data import read_data

#定义输入文档名字
input_file = "data_2D.txt"

#载入第三和第四列的数据，分成两个变量
x1 = read_data(input_file,2)
x2 = read_data(input_file,3)

#创建 pandas dataframe，命名两个维
data = pd.DataFrame({'dim1':x1,'dim2':x2})

#提取两个维的最大和最小值
print("\nMaximum values for each dimension:")
print(data.max())
print("\nMinimun values for each dimension :")
print(data.min())

#提取整个数据集的平均值 和前12行行平均值
print('\n overall mean:')
print(data.mean())
print('\nRow-wise mean:')
print(data.mean(1)[:12])

#使用大小为24的窗口画出滚动平均值
data.rolling(center =False,window =24).mean().plot()
plt.title('Rolling mean')

#输出相关性
print('\n Correlation coefficient:\n',data.corr())

#使用size=60的窗口画出滚动相关性
plt.figure()
plt.title('rolling correlation:')
data['dim1'].rolling(window=60).corr(other =data['dim2']).plot()

plt.show()