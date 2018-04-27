#导入如下的包
import random 
from nltk.classify import accuracy as nltk_accuracy
from  nltk.corpus import names 
from nltk import NaiveBayesClassifier

#定义提取输入单词最后N个字母的函数
def extract_features(word,N=2):
    last_n_letters = word[-N:]
    return {'feature':last_n_letters.lower()}
#定义主函数 ，提取重scikit-learn包中提取训练数据。这个数据包含被标记男性和女性的名字
if __name__ == '__main__':
    #创建训练集
    male_list = [(name,'male') for name in names.words('male.txt')]
    female_list = [(name,'female') for name in names.words('female.txt')]
    data = (male_list+female_list)

    #seed() 方法改变随机数生成器的种子,参数为种子，并打乱
    #所谓假Random，是指所返回的随机数字其实是一个稳定算法所得出的稳定结果序列，
    #而不是真正意义上的随机序列。 Seed就是这个算法开始计算的第一个值。所以就会出现只要seed是一样的，那么后续所有“随机”结果和顺序也都是完全一致的。
    random.seed(5)#指定种子，按照特定算法生成固定的随机数
    random.shuffle(data)#打乱序列顺序

    #创建测试数据
    input_names=['Alexander','Danielle','David','Cheryl']

    #定义将被训练和测试数据的百分比
    num_train = int(0.8*len(data))

    #循环输入不同的长度，比较精确度
    for i in range(1,6):
        print('\nNumber of end letters:',i)
        features = [(extract_features(n,i),gender) for (n,gender) in data]
        #将数据分成训练和测试
        train_data,test_data = features[:num_train],features[num_train:]
        #使用训练数据构建朴素贝叶斯分类器
        calssifier =NaiveBayesClassifier.train(train_data)
        #计算分类器的准确度
        accuracy = round(100*nltk_accuracy(calssifier,test_data),2)
        print('Accuracy = '+str(accuracy)+'%')

        #使用训练的模型预测输入数据的输出
        for name in input_names:
            print(name,'==>',calssifier.classify(extract_features(name,i)))
    




