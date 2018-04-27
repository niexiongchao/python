import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from Handling_time_series_data_with_Pandas import read_data

#加载输入数据
index =2
data = read_data('data_2D.txt',index)

#定义开始和结束年份，然后以年份绘图
start ='2003'
end = '2011'
plt.figure()
data[start:end].plot()
plt.title('Input data from '+start +'to' +end)

#定义开始和结束年份，然后以年份绘图
start ='1998-2'
end = '2006-7'
plt.figure()
data[start:end].plot()
plt.title('Input data from '+start +'to' +end)

plt.show()