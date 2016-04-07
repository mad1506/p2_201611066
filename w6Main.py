
# coding: utf-8

# In[4]:

def projecteuler1():
    print "Hello! This is Project Euler 1 answer."
    
    sum = 0
    
    for i in range(1,1000):
        if i%3 == 0 or i%5 == 0:
            sum = sum + i
            
    print "Project Euler 1 answer is %d" %sum
    
def yunnyun():
    print "Hello! This is Yunnyun Program."
    
    year=input("input year: ")

    if year%4 == 0 and not year%100 == 0:
        result = "yun nyun"
    elif year%4==0 and year%400==0:
        result = "yun nyun"
    else:
        result = "not yun nyun or Input error"
    
    print result

def highlowgame():

    import random
    
    print "Hello! This is High-Low Game."

    correct = random.randrange(1,51)

    while True:
    
        answer = input("Input your answer (1-50): ")

        if(answer==correct):
            result = "Correct! Game is over."
        
            print result
        
            break

        else:
            if(50>=answer>correct):
                result = "Your answer is too high. Try again."
            
            elif(1<=answer<correct):
                result = "Your answer is too low. Try again."
            
            else:
                result = "Input Error. Try again."
            
            print result

def lab5():
    projecteuler1()
    yunnyun()
    highlowgame()
    

def main():
    lab5()
    
if __name__=="__main__":
    main()

