
# coding: utf-8

# In[1]:

class Dog(object):
    def __init__(self, name):
        self.name=name
    def getName(self):
        print "my dog name is ", self.name
    def talk(self):
        print "mung mung"
        
class ShihTzuDog(Dog):
    def talk(self):
        print "si si"
        
class Maltese(Dog):
    def talk(self):
        print "mal mal"
        
def dogsimal():
    d=Dog('poppy')
    d.talk()
    Mal=Maltese('poppy')
    Mal.talk()
    Si=ShihTzuDog('poppy')
    Si.talk()

def lab14():
    dogsimal()

def main():
    lab14()
    
if __name__=="__main__":
    main()

