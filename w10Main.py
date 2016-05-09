
# coding: utf-8

# In[12]:

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
    
    
    
def main():
    lab10()
    
if __name__=="__main__":
    main()
