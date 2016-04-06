
# coding: utf-8

# In[22]:

year=input("input year: ")

if year%4 == 0 and not year%100 == 0:
    result = "yun nyun"
elif year%4==0 and year%400==0:
    result = "yun nyun"
else:
    result = "not yun nyun or Input error"
    
print result

