
# coding: utf-8

# In[3]:

import w5Main


# In[4]:

w5Main.main()


# In[6]:

sel1=raw_input("enter s,r or p: ")


# In[7]:

print sel1


# * 변수의 타입 -> 데이터형을 아는 것이 중요하다.

# In[8]:

type(sel1)


# In[9]:

sel2=raw_input("enter s,r or p: ")


# In[10]:

if sel1=="s":
    if sel2=="r":
        print "sel2 win"
    elif sel2=="p":
        print "sel1 win"


# In[11]:

if sel1=="s" and sel2=="r":
        print "sel2 win"
elif sel1=="s" and sel2=="p":
        print "sel1 win"


# In[12]:

if sel1=="s" and sel2=="r":
        res="sel2 win"
elif sel1=="s" and sel2=="p":
        res="sel1 win"
print res


# In[15]:

def rspPlay():
    if sel1=="s" and sel2=="r":
        res="sel2 win"
    elif sel1=="s" and sel2=="p":
        res="sel1 win"
    return res

print rspPlay() 


# In[22]:

def rspPlay(sel1,sel2):
    if sel1=="s" and sel2=="r":
        res="sel2 win"
    elif sel1=="s" and sel2=="p":
        res="sel1 win"
    return res

result=rspPlay("s","p")

print result


# ## 제어-7 삼각형 그리기

# * operator overloading
# 연산자 "+"가 수를 만나면 덧셈을 하지만
# 연산자 "+"가 문자를 만나면 합성을 한다.

# In[57]:

print 1+1
print '1'+'1'
print 'hello'+'jsl'
print '1'*2
print "#"*5


# In[46]:

for i in range(1,6):
    print "#"*i


# In[67]:

for i in range(1,7):
    print " "*(7-i)+"#"*i+"#"*(i-1)


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



