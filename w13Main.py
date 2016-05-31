
# coding: utf-8

# In[2]:

def writePythonTextFile(file):
    myfile=open(file, 'w')
    line1='Python is a widely used high-level, general-purpose, interpreted,\n'
    myfile.write(line1)
    line2='dynamic programming language.[23][24]\n'
    myfile.write(line2)
    line3='Its design philosophy emphasizes code readability, and\n'
    myfile.write(line3)
    line4='its syntax allows programmers to express concepts in fewer lines of code\n'
    myfile.write(line4)
    line5='than would be possible in languages such as C++ or Java.[25][26]\n'
    myfile.write(line5)
    line6='The language provides constructs intended to enable clear programs on\n'
    myfile.write(line6)
    line7='both a small and large scale.[27]\n'
    myfile.write(line7)
    myfile.close()
    
def readFile(file):
    mydir=os.getcwd()
    filename=file
    myfilename=os.path.join(mydir,filename)
    myfile=open(myfilename)
    line=myfile.read()
    myfile.close()
    print line

def writeNumberTextFile(file, data):
    fout=open(file,'w')
    for i,item in enumerate(data):
        str="{0}\t".format(item)
        fout.write(str)
        if(i%2==1):
            fout.write('\n')
    fout.close()
    
def overWriteAtoB(fileA,fileB):
    fin1=open(fileB, 'a')
    fin2=open(fileA, 'r')
    for line in fin2:
        fin1.write(line)
    fin1.close()
    fin2.close()

def lab13():
    global os
    import os
    writePythonTextFile('python.txt')
    print "Original python.txt:\n"
    readFile('python.txt')
    data=[1,2,3,4,5,6,7,8,9,10]
    writeNumberTextFile('outputNumber.txt', data)
    print "outputNumber.txt:\n"
    readFile('outputNumber.txt')
    overWriteAtoB('outputNumber.txt', 'python.txt')
    print "Overwrited python.txt:\n"
    readFile('python.txt')
    
    
def main():
    lab13()
    
if __name__=="__main__":
    main()

