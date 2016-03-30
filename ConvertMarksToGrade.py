
# coding: utf-8

# In[7]:

marks = raw_input("Input your marks 0~100: ")
def ConvertMarksToGrade(marks):
    if 90<=float(marks)<=100:
        grade="A"
    elif 80<=float(marks)<=89:
        grade="B"
    elif 70<=float(marks)<=79:
        grade="C"
    elif 60<=float(marks)<=69:
        grade="D"
    else:
        grade="F or Input Error"
    return grade
result=ConvertMarksToGrade(marks)
print "Your Grade is %s" %result

