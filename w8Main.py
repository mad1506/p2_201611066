
# coding: utf-8

# In[16]:

def charCount(word):
    global mydict
    mydict=dict()
    for i in word:
        if i not in mydict:
            mydict[i]=1
        else:
                mydict[i]=mydict[i]+1
    return mydict

def drawBar():
    get_ipython().magic(u'matplotlib inline')

    import matplotlib
    import matplotlib.pyplot as plt

    plt.bar(range(len(mydict)),mydict.values(), align='center')
    plt.xticks(range(len(mydict)), list(mydict.keys()))
    plt.show()

def lab8():
    global word
    word="media software"
    result=charCount(word)
    print result
    drawBar()
    
def main():
    lab8()
    
if __name__=="__main__":
    main()

