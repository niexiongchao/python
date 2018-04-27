import datetime
import warnings
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.finance import quotes_historical_yahoo_ochl as quotes_yahoo
from hmmlearn.hmm import GaussianHMM

#载入历史股票数据
start =datetime.date(1970,9,4)
end = datetime.date(2016,5,17)

stock_quotes =quotes_yahoo('INTC',start,end)

#提取每天的收盘情况
closing_quotes =np.array([quote[2] for quote in stock_quotes])

volumes =np.array([quote[5] for quote in stock_quotes])[1:]

diff_percentage =100.0*np.diff(closing_quotes)/closing_quotes[:-1]
# 重第二个值开始取日期
dates = np.array([quotes[0] for quote in stock_quotes],dtype=np.int)[1:]

#使用不同的大量值进行训练
training_data = np.column_stack([diff_percentage,volumes])
hmm = GaussianHMM(n_components =7,covariance_type='diag',n_iter=1000)
with warnings.catch_warnings():
    warnings.simplefilter('ignore')
    hmm.fit(training_data)


#使用HMM生成数据
num_samples =300
samples ,_=hmm.sample(num_samples)
#画出生成的数据
plt.figure()
plt.title('difference percentage')
plt.plot(np.arange(num_samples),samples[:,0],c='black')

#画出交易数据
plt.figure()
plt.title('Volume of shares')
plt.plot(np.arange(num_samples),samples[:,1],c='black')

plt.show()