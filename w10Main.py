
# coding: utf-8

# In[12]:

def milkRate(coffee):
    coffeeList=coffee[1:]
    freq=0.
    for i in coffeeList:
        if i[2]=="No":
            freq=freq
        else:
            freq=freq+1
    result=(freq/len(coffeeList))*100
    return result

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
    
def main():
    lab10()
    
if __name__=="__main__":
    main()

