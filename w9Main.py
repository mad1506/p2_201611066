
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
    print "our home"
    print a
    print "friend's home"
    print b
    print "only friend's home" 
    print b.difference(a)
    print "only our home" 
    print a.difference(b)
    print "together electronics"
    print a.intersection(b)
    print "at least one home"
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
    
def calDistance(p1,p2):
    import math
    global dist
    dist=list()
    for p2 in tuple:
        print "x1={0} y1={1}".format(p1[0],p2[1])
        print "x2={0} y2={1}".format(p2[0],p2[1])
        distance=math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
        print "distance: ", distance
        dist.append(distance)
    print "minimum distacne is: ", min(dist)
    
def mansum(my2dlist):
    mansum=0
    for i in my2dlist:
        mansum=mansum+i[0]
    return mansum

def womansum(my2dlist):
    womansum=0
    for i in my2dlist:
        womansum=womansum+i[1]
    return womansum

def manaver(my2dlist):
    manaver=mansum(my2dlist)/len(my2dlist)
    return manaver

def womanaver(my2dlist):
    womanaver=womansum(my2dlist)/len(my2dlist)
    return womanaver

def goosum(my2dlist):
    goosum=0
    goosumm=list()
    for i in my2dlist:
        goosum=i[0]+i[1]
        goosumm.append(goosum)
    return goosumm

def drawBar2(mylist):
    import matplotlib
    import matplotlib.pyplot as plt

    plt.bar(range(len(mylist)),mylist, align='center')
    plt.xticks(range(len(mylist)), list(mylist))
    plt.show()

def lab9():
    import math
    print "count each string and draw bar graph."
    word=raw_input("input your sentence: ")
    result=charCount(word)
    print result
    drawBar(result)
    print "count strings and digits and draw bar graph."
    word2=raw_input("input your sentence with ints: ")
    result2=countDigitisLetters(word2)
    print result2
    drawBar(result2)
    print "our home and friend's home"
    oh={'TV','phone','camera','fridger','mixer','audio','cd player','light','computer','notebook','recorder'}
    fh={'coffee machine','radio','camera','running machine','ramp','computer','notebook','recorder'}
    electronics(oh,fh)
    print "count all electronics"
    result3=countElectronics(oh,fh)
    print result3
    #경복궁역
    kbg=(37.575811, 126.973588)
    #광화문역
    khm=(37.571593, 126.976443)
    #안국역
    ak=(37.576570, 126.985406)
    #독립문역
    drm=(37.574577, 126.957754)
    #종각역
    jk=(37.570099, 126.983046)
    #시청역
    sch=(37.565649, 126.976820)
    global tuple
    tuple=(khm, ak, drm, jk, sch)
    p1=kbg
    p2=tuple
    calDistance(p1,p2)
    my2dlist=[
    [74425, 76326],
    [61164, 61636],
    [109688, 115744],
    [144796, 146776],
    [174996, 181676],
    [177841, 177434],
    [204630, 205980],
    [223373, 232245],
    [161055, 166130],
    [171576, 176735],
    [279169, 293772],
    [239450, 251066],
    [148690, 156510],
    [182977, 196992],
    [237792, 242641],
    [283869, 296762],
    [209344, 210282],
    [118965, 114441],
    [186503, 186856],
    [195734, 203014],
    [254381, 249472],
    [212401, 229111],
    [271654, 295354],
    [319197, 335045],
    [229829, 231671]
]
    print "mansum: ", mansum(my2dlist)
    print "womansum: ", womansum(my2dlist)
    print "manaver: ", manaver(my2dlist)
    print "womanaver: ", womanaver(my2dlist)
    goosumm=goosum(my2dlist)
    print "goosum: ", goosumm
    drawBar2(goosumm)

def main():
    lab9()
    
if __name__=="__main__":
    main()
