
# coding: utf-8

# In[1]:

def milkRate(coffee):
    coffeeList=coffee[1:]
    freq=0.
    for i in coffeeList:
        x=i[2].upper()
        if i[2]=="NO":
            freq=freq
        else:
            freq=freq+1
    result=(freq/len(coffeeList))*100
    return result

def sumEngMarks(marks):
    d=list()
    for i in marks:
        x=i[0].upper()
        if x=="ENGLISH":
            d.append(i[1])
    return sum(d)

def sumMatMarks(marks):
    d=list()
    for i in marks:
        x=i[0].upper()
        if x=="MATH":
            d.append(i[1])
    return sum(d)

def averEngMarks(marks):
    d=list()
    for i in marks:
        x=i[0].upper()
        if x=="ENGLISH":
            d.append(i[1])
    return float(sum(d))/len(d)

def averMatMarks(marks):
    d=list()
    for i in marks:
        x=i[0].upper()
        if x=="MATH":
            d.append(i[1])
    return float(sum(d))/len(d)

def maxWord(lyrics):
    doc=lyrics
    d=dict()
    for line in doc:
        words=line.split()
        for c in words:
            if c not in d:
                d[c]=1
            else:
                d[c]=d[c]+1
    return max(d, key=d.get)

def averWellContented(datas):
    sumlist=[]
    list=datas[1:]
    for i in list:
        sumlist.append(i[1])
    sume=sum(sumlist)
    return sume/len(sumlist)

def averContented(datas):
    sumlist=[]
    list=datas[1:]
    for i in list:
        sumlist.append(i[2])
    sume=sum(sumlist)
    return sume/len(sumlist)

def averNotContented(datas):
    sumlist=[]
    list=datas[1:]
    for i in list:
        sumlist.append(i[4])
    sume=sum(sumlist)
    return sume/len(sumlist)

def averNeverContented(datas):
    sumlist=[]
    list=datas[1:]
    for i in list:
        sumlist.append(i[5])
    sume=sum(sumlist)
    return sume/len(sumlist)

def averContenteds(datas):
    return (averWellContented(datas)+averContented(datas))/2

def averNoContenteds(datas):
    return (averNotContented(datas)+averNeverContented(datas))/2

def lab10():
    coffee=[
    ["Coffee", "Water", "Milk", "Icecream"],
    ["Espresso", "No", "No", "No"],
    ["Long Black","Yes","No","No"],
    ["Flat White","No","Yes","No"],
    ["Cappuccino","No","Yes - Frothy","No"],
    ["Affogato","No","No","Yes"],
]
    res=milkRate(coffee)
    print "Milk Rate is: ", res, "%"
    marks=[
    ["English", 100],
    ["Math", 200],
    ["English", 200],
    ["Math", 200],
    ["English", 100],
    ["Math", 300],

]
    resEngSum=sumEngMarks(marks)
    resMatSum=sumMatMarks(marks)
    resEngAver=averEngMarks(marks)
    resMatAver=averMatMarks(marks)
    print "English Marks sum: ", resEngSum
    print "Math Marks sum: ", resMatSum
    print "English Marks average: ",resEngAver
    print "Math Marks average: ", resMatAver
    lyrics=[
    "when I find myself in times of trouble",
    "mother mary comes to me",
    "speaking words of wisdom , let it be",
    "and in my hour of darkness",
    "she is standing right in front of me",
    "speaking words of wisdom , let it be",
    "let it be , let it be",
    "let it be , let it be",
    "whisper words of wisdom , let it be",
    "and when the broken-hearted people",
    "living in the world agree",
    "there will be an answer , let it be",
    "for though they may be parted",
    "there is still a chance that they will see",
    "there will be an answer , let it be",
    "let it be , let it be",
    "let it be , let it be",
    "yeah, there will be an answer , let it be",
    "let it be , let it be",
    "let it be , let it be",
    "whisper words of wisdom , let it be",
    "let it be , let it be",
    "ah, let it be, yeah , let it be",
    "whisper words of wisdom , let it be",
    "and when the night is cloudy",
    "there is still a light that shines on me",
    "shine on until tomorrow , let it be",
    "i wake up to the sound of music ,",
    "mother mary comes to me",
    "speaking words of wisdom , let it be",
    "let it be , let it be",
    "let it be , yeah , let it be",
    "oh, there will be an answer , let it be",
    "let it be , let it be",
    "let it be , yeah , let it be",
    "whisper words of wisdom,  let it be",
]
    max=maxWord(lyrics)
    print "High frequences rates word: ", max
    
    datas=[
    ["division", "well contented", "contented", "normal" "not contented" "never contented"],
    ["contents of education", 13.1, 37.1, 39.6, 8.7, 1.5],
    ["methods of education", 10.6, 34.6, 39.5, 13.4, 1.9],
    ["relations of friends", 27.1, 40.0, 28.5, 2.9, 1.5],
    ["relations of teachers", 16.2, 37.8, 38.4, 6.8, 0.8],
    ["facilities of school", 11.4, 29.8, 39.0, 14.8, 4.9],
    ["surroundings of school", 12.2, 26.5, 42.0, 14.9, 4.4],
    ["major", 13.5, 29.7, 43.4, 11.1, 2.4],
    ["wide school life", 13.7, 37.6, 43.4, 4.1, 1.2]
]
    averA=averContenteds(datas)
    averB=averNoContenteds(datas)
    print "Average of Well Contented & Contented: ", averA
    print "Average of Not Contented & Never Contented: ", averB
    
def main():
    lab10()
    
if __name__=="__main__":
    main()
