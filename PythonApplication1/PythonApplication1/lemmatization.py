import numpy as np 
from nltk.corpus import brown

#将输入的文本分块，每一块含有N个单词
def chunker(input_data,N):
    input_words = input_data.split(' ')
    output=[]
    cur_chunk = []
    count = 0
    for word in input_words:
        cur_chunk.append(word)
        count+=1
        if count==N:
            output.append(' '.join(cur_chunk))
            count,cur_chunk =0,[]
    output.append(' '.join(cur_chunk))

    return output

if __name__=='__main__':
    #从brown语料库中读入前12000单词
    input_data = ' '.join(brown.words()[:12000])
    #定义每块的大小
    chunk_size =700

    chunks =chunker(input_data,chunk_size)
    print('\nNumber of text chunks =',len(chunks),'\n')
    for i,chunk in enumerate(chunks):
        print('Chunk',i+1,'==>',chunk[:50])
