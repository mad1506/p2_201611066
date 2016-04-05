
# coding: utf-8

# In[2]:

height=float(input("input your height(m) : "))
weight=float(input("input your weight(kg) : "))
bmi=float(weight/(height*height))

if(bmi<18.5):
    res="low weight"
elif(18.5<=bmi<25.0):
    res="normal weight"
elif(25.0<=bmi<30.0):
    res="obesity"
elif(bmi>=30.0):
    res="dangerous obesity"
else:
    res="Input Error"
    
print res


# In[3]:

def bmiprogram(height,weight):
    
    bmi=float(weight/(height*height))
    
    if(bmi<18.5):
        res="low weight"
    elif(18.5<=bmi<25.0):
        res="normal weight"
    elif(25.0<=bmi<30.0):
        res="obesity"
    elif(bmi>=30.0):
        res="dangerous obesity"
    else:
        res="Input Error"
    
    return res

result=bmiprogram(1.72,72)

print result

