
# coding: utf-8

# In[ ]:

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

def lab5():
    bmiprogram(height,weight)

def main():
    lab5()
    
if __name__=="__main__":
    main()

