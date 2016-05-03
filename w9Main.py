
# coding: utf-8

# In[1]:

def charCount(word):
    mydict=dict()
    for i in word:
        if i not in mydict:
            mydict[i]=1
        else:
                mydict[i]=mydict[i]+1
    return mydict

def countDigitisLetters(word):
    dicA={'int':0,'str':0}
    for i in word:
        if i.isdigit():
            dicA['int']=dicA['int']+1
        else:
            dicA['str']=dicA['str']+1
    return dicA    

def drawBar(mydict):
    import matplotlib
    import matplotlib.pyplot as plt

    plt.bar(range(len(mydict)),mydict.values(), align='center')
    plt.xticks(range(len(mydict)), list(mydict.keys()))
    plt.show()
    
def electronics(a,b):
    print "우리집"
    print a
    print "친구집"
    print b
    print "우리 집에 없지만 친구 집에 있는 가전제품" 
    print b.difference(a)
    print "친구 집에 없지만 우리 집에 있는 가전제품" 
    print a.difference(b)
    print "모든 집에 같이 있는 가전제품 "
    print a.intersection(b)
    print "어느 한 집에라도 있는 가전제품"
    print a.union(b)
    
def countElectronics(a,b):
    dict={}
    for i in a:
        if i not in dict:
            dict[i]=1
        else:
            dict[i]=dict[i]+1

    for i in b:
        if i not in dict:
            dict[i]=1
        else:
            dict[i]=dict[i]+1

    return dict
    


def lab9():
    print "각 문자 갯수 세고 막대그래프 그리기"
    word=raw_input("input your sentence: ")
    result=charCount(word)
    print result
    drawBar(result)
    print "문자와 숫자 갯수 세고 막대그래프 그리기"
    word2=raw_input("input your sentence with ints: ")
    result2=countDigitisLetters(word2)
    print result2
    drawBar(result2)
    print "우리집과 친구집"
    oh={'TV','phone','camera','fridger','mixer','audio','cd player','light','computer','notebook','recorder'}
    fh={'coffee machine','radio','camera','running machine','ramp','computer','notebook','recorder'}
    electronics(oh,fh)
    print "모든 집에 있는 가전제품 갯수 세기"
    result3=countElectronics(oh,fh)
    print result3

def main():
    lab9()
    
if __name__=="__main__":
    main()

