#导入如下包
from sklearn.datasets import fetch_20newsgroups
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer

#定义类别map,用于训练。我们定义5个类别，字典中的key引用scikit-learn数据集的名字
category_map = {'talk.politics.misc': 'Politics', 'rec.autos': 'Autos', 
        'rec.sport.hockey': 'Hockey', 'sci.electronics': 'Electronics', 
        'sci.med': 'Medicine'}


#获取训练集
training_data = fetch_20newsgroups(subset='train', 
        categories=category_map.keys(), shuffle=True, random_state=5)


#使用CountVectorizerd对象提取单词出现次数
#构建计数向量 和提取词的出现次数
count_verctorizer = CountVectorizer()
train_tc = count_verctorizer.fit_transform(training_data.data)
print("\nDimensions of training data：",train_tc.shape)

#创建词频-逆向文件频度转换器，并进行训练
tfidf = TfidfTransformer()
train_tfidf = tfidf.fit_transform(train_tc)

#定义测试输入例句
input_data = [
    'You need to be careful with cars when you are driving on slippery roads', 
    'A lot of devices can be operated wirelessly',
    'Players need to be careful when they are close to goal posts',
    'Political debates help us understand the perspectives of both sides'
]


#使用训练数据训练多项贝叶斯分类器
classifier = MultinomialNB().fit(train_tfidf,training_data.target)

#使用计数向量转换输入数据
input_tc = count_verctorizer.transform(input_data)

#使用tf-idf 转换器转换向量数据，以便向量能使用在推理模型中
input_tfidf = tfidf.transform(input_tc)

#使用tf-idf预测输出
predictions = classifier.predict(input_tfidf)
 
#打印输出
for sent,category in zip(input_data,predictions):
    print('\nInput:',sent,'\nPredicted dategory:',category_map[training_data.target_names[category]])

