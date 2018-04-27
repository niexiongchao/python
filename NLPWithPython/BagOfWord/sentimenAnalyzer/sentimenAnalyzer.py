#导入如下的包
from nltk.corpus import movie_reviews
from nltk.classify import NaiveBayesClassifier
from nltk.classify.util import accuracy as nltk_accuracy

#定义函数来构建一个基于输入数据的的字典对象并返回
#从输入数据列表提取特征
def extract_features(words):
    return dict([(word,True) for word in words])

#定义主函数
if __name__ == '__main__':
    #从语料库载入影评
    fileids_pos = movie_reviews.fileids('pos')
    fileids_neg = movie_reviews.fileids('neg')

    #从影评中提取特征
    features_pos = [(extract_features(movie_reviews.words(fileids = [f])),'Positive') for f in fileids_pos]

    features_neg = [(extract_features(movie_reviews.words(fileids = [f])),'Negative') for f in fileids_neg]

    #定义训练和测试集
    threshold = 0.8
    num_pos = int(threshold*len(features_pos))
    num_neg = int(threshold*len(features_neg))

    features_train = features_pos[:num_pos]+features_neg[:num_neg]
    features_test = features_pos[num_pos:]+features_neg[num_neg:]
    
    #打印被使用的数据点数目
    print('\nNumber of Training datapoints:',len(features_train))
    print('\nNumber of Testing datapoints:',len(features_test))

    #训练一个朴素贝叶斯分类器
    classifier = NaiveBayesClassifier.train(features_train)
    print('\nAccuracy of the classifier:',nltk_accuracy(classifier,features_test))

    N =15
    print('\nTop'+str(N) + 'most information words:')
    for i,item in enumerate(classifier.most_informative_features()):
        print(str(i+1)+'.'+item[0])
        if i==N-1:
            break

    #测试输入的影评
    input_reviews = ['the costumes in this movie were great',
                      'I thik the story was terrible and the characters were very weak',
                     'People say that the director of the movie is amazing',
                     'This is such an idiotic movie. I will not recommand it to anyone']
    

    print("\nMovie review predictions:")
    for review in input_reviews:
        print("\nReview:", review)

        # Compute the probabilities
        probabilities = classifier.prob_classify(extract_features(review.split()))

        # Pick the maximum value
        predicted_sentiment = probabilities.max()

        # Print outputs
        print("Predicted sentiment:", predicted_sentiment)
        print("Probability:", round(probabilities.prob(predicted_sentiment), 2))


