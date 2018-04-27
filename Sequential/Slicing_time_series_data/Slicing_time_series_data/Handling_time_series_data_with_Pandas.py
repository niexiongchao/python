import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#定义函数读入数据，参数index 代表包含相关数据的列数
def read_data(input_file,index):
    input_data = np.loadtxt(input_file,delimiter=',')

    #定义一个lambda函数将string转换为Pandas日期格式
    to_date = lambda x,y:str(int(x))+'-'+str(int(y))

    #提取起始时间
    start = to_date(input_data[0,0],input_data[0,1])

    #提取结束时间
    if input_data[-1,1]==12:
        year = input_data[-1,0]+1
        month = 1
    else:
        year = input_data[-1,0]
        month = input_data[-1,1]+1
    end = to_date(year,month)

    #创建一个时间列表
    date_indices = pd.date_range(start,end,freq='M')
    #添加时间戳到输入数据来创建时间序列数据
    output = pd.Series(input_data[:,index],index = date_indices)
    return output


#定义主函数
if __name__ == '__main__':
    #输入文档名
    input_file = 'data_2D.txt'
    
    #指定需要转换的列数
    indice = [2,3]

    #迭代输入列数 并画出数据
    for  index in indice:
        #将行转换为时间序列
       timeseries = read_data(input_file,index)

       #绘制数据
       plt.figure()
       timeseries.plot()
       plt.title('Dimension'+str(index - 1))

    plt.show();
        