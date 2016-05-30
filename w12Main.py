def writePythonTextFile():
    myfile=open('python.txt', 'w')
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
    
def changeToCap(file):
    import os
    mydir=os.getcwd()
    filename=file
    myfilename=os.path.join(mydir, filename)
    try:
        myfile=open(myfilename, 'r')
        contents=myfile.readlines()
        myfile.close()
        myfile=open(myfilename, 'w')
        for i in range(0,len(contents)):
            line=contents[i].upper()
            myfile.write(line)
        myfile.close()
        myfile=open(myfilename, 'r')
        contents=myfile.read()
        myfile.close()
        print contents
        
        
    except IOError as e:
        print e
    
def findWord(file, word):
    import os
    mydir=os.getcwd()
    filename=file
    myfilename=os.path.join(mydir, filename)
    try:
        myfile=open(myfilename, 'r')
        contents=myfile.readlines()
        myfile.close()
        for i in contents:
            if i.find(word) >= 0:
                print "Find " + word + " :" + i
    except IOError as e:
        print e
        
def outputWrite(file):
    fout = open(file, 'w')
    fout.write("first line\n")
    fout.write("\tsecond line\n")
    fout.write("third")
    fout.close()
    
def realChangeToCap(file, filec):
    fin = open(file, 'r')
    fout = open(filec,'w')
    editFlag='[drgnj edited {}]'.format(time.strftime("%Y-%m-%d %H:%M:%S"))
    for sentence in fin:
        if sentence.find('line')>= 0:
            sentence=sentence.replace('line','LINE')
            sentence=editFlag+sentence
        fout.write(sentence)
    fin.close()
    fout.close()

def writeTwoDimensions(file,data):
    fout=open(file,'w')
    for i,item in enumerate(data):
        str="{0}\t".format(item)
        fout.write(str)
        if(i%2==1):
            fout.write('\n')
    fout.close()
    
def lab12():
    global os
    global time
    import os
    import time
    
    writePythonTextFile()
    
    # 한 줄씩 읽기
    print "\tUse readline():\n"
    mydir=os.getcwd()
    filename='Python.txt'
    myfilename=os.path.join(mydir, filename)
    myfile=open(myfilename, 'r')
    for line in range(0,7):
        line=myfile.readline()
        print line
    myfile.close()
    
    # 전체 읽기
    print "\tUse read():\n"
    myfile=open(myfilename, 'r')
    contents=myfile.read()
    myfile.close()
    print contents
    
    # 전체 읽기인데 자료구조 list이용
    print "\tUse readlines():\n"
    myfile=open(myfilename, 'r')
    contents=myfile.readlines()
    myfile.close()
    print contents
    
    print "\n"
    
    # 검색 함수
    file='Python.txt'
    word="Python"
    findWord(file, word)
    
    # 대문자로 바꿔쓰기
    print "Change to Capital:\n"
    file='Python.txt'
    changeToCap(file)

    # 대문자로 바꿔쓰기 2
    print "Change to Capital 2:\n Check Your 'outputUpper.txt' File"
    file='output.txt'
    outputWrite(file)
    filec='outputUpper.txt'
    realChangeToCap(file, filec)
    
    # 2차원 데이터를 파일로 쓰기
    file='outputNumber.txt'
    data=[1,2,3,4,5,6,7,8,9,10]
    writeTwoDimensions(file, data)
    print "Write Two Dimensions File:\n Check Your 'outputNumber.txt' File"

def main():
    lab12()
    
if __name__=="__main__":
    main()
