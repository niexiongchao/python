import datetime
import numpy as np
import matplotlib.pyplot as plt
from hmmlearn.hmm import GaussianHMM
from Slicing_time_series_data import read_data
#　　　hmmlearn实现了三种HMM模型类，按照观测状态是连续状态还是离散状态，可以分为两类。GaussianHMM和GMMHMM是连续观测状态的HMM模型，而MultinomialHMM是离散观测状态的模型，也是我们在HMM原理系列篇里面使用的模型。
#加载数据
data = np.loadtxt('data_1D.txt',delimiter=',')

#提取第三列进行训练
x=np.column_stack([data[:,2]])

#创建GaussianHMM，参数：状态的数量n_components=5,covariance_type='diag',“diag” - 每个状态使用对角协方差矩阵。n_iter要执行的最大迭代次数。
num_components =5
hmm =GaussianHMM(n_components=num_components,covariance_type='diag',n_iter=1000)

#训练HMM
print("\n正在训练隐马尔科夫模型....")
hmm.fit(x)
#输出每个HMM状态的平均值和方差
print("\n均值和方差：")
for i in range(hmm.n_components):
    print('\n隐状态',i+1)
    print('均值 = ',round(hmm.means_[i][0],2))
    print("方差 = ",round(np.diag(hmm.covars_[i])[0],2))

#生成1200条数据训练HMM模型并绘出
num_samples = 1200
generated_data,_=hmm.sample(num_samples)#_约定不关心数字的变量，后期不使用
plt.plot(np.arange(num_samples),generated_data[:,0],c='red')
plt.title('Gnenerate data')
plt.show()