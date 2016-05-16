def keyup():
    t1.forward(50)
    pt=t1.pos()
    t1.write(pt)
    print "up",pt
    if isInRectangle(pt, coord):
        t1.write("Turtle is in Rectangle!!")
        t1.penup()
        t1.goto(-400,300)
        t1.pendown()
    elif isInCircle(pt,radius,cpos):
        t1.write("Turtle is in Circle!!")
        t1.penup()
        t1.goto(-400,300)
        t1.pendown()
        
    elif isOnLine(pt,line):
        t1.write("Turtle is in Line!!")
        t1.penup()
        t1.goto(-400,300)
        t1.pendown()

def keyleft():
    t1.left(45)

def keyright():
    t1.right(45)

def keydown():
    t1.backward(50)
    pt=t1.pos()
    t1.write(pt)
    print "down",pt
    if isInRectangle(pt, coord):
        t1.write("Turtle is in Rectangle!!")
        t1.penup()
        t1.goto(-400,300)
        t1.pendown()
    elif isInCircle(pt,radius,cpos):
        t1.write("Turtle is in Circle!!")
        t1.penup()
        t1.goto(-400,300)
    elif isOnLine(pt,line):
        t1.write("Turtle is in Line!!")
        t1.penup()
        t1.goto(-400,300)
        t1.pendown()

def addKeys():
    wn.onkey(keyup, "Up")
    wn.onkey(keyleft, "Left")
    wn.onkey(keyright, "Right")
    wn.onkey(keydown, "Down")
    wn.onkey(wn.bye, "q")
    
def setGame():
    t1.speed(20)
    t1.penup()
    t1.pencolor("BLUE")
    t1.goto(350,-300)
    t1.pendown()
    t1.fd(100)
    t1.goto(450,-200)
    t1.bk(100)
    t1.goto(350,-300)
    t1.penup()
    t1.goto(0,-300)
    t1.pendown()
    t1.circle(100)
    t1.penup()
    t1.goto(-450,-300)
    t1.pendown()
    t1.fd(150)
    
def mousegoto(x,y):
    msg="mouse clicked {0} {1}".format(x,y)
    wn.title(msg)
    t1.setpos(x,y)
    pt=t1.pos()
    t1.write(pt)
    print "click",pt
    if isInRectangle(pt, coord):
        t1.write("Turtle is in Rectangle!!")
        t1.penup()
        t1.goto(-400,300)
        t1.pendown()
    elif isInCircle(pt,radius,cpos):
        t1.write("Turtle is in Circle!!")
        t1.penup()
        t1.goto(-400,300)
    elif isOnLine(pt,line):
        t1.write("Turtle is in Line!!")
        t1.penup()
        t1.goto(-400,300)
        t1.pendown()

def addMouse():
    wn.onclick(mousegoto)
    
def gamePlay():
    import turtle
    global wn
    global t1
    global coord
    global radius
    global cpos
    global line
    line=[(-450,-300),(-300,-300)]
    coord=[(350,-300),(450,-200)]
    radius=100
    cpos=(0,-300)
    wn=turtle.Screen()
    wn.bgpic("myMaze.gif")
    t1=turtle.Turtle()
    setGame()
    t1.speed(7)
    t1.penup()
    t1.goto(-400,300)
    t1.pendown()
    t1.pencolor("Red")
    t1.write("Click or Input Keys")
    addKeys()
    addMouse()
    wn.listen()
    turtle.mainloop()
    
def isInRectangle(curpos, coord):
    xs=startCoord(coord)[0]
    xe=endCoord(coord)[0]
    ys=startCoord(coord)[1]
    ye=endCoord(coord)[1]
    
    return (xs<=curpos[0]<=xe or xe<=curpos[0]<=xs) and (ys<=curpos[1]<=ye or ye<=curpos[1]<=ys)

def startCoord(coord):
    if distance(coord[0],(0,0))<=distance(coord[1],(0,0)):
        return coord[0]
    else:
        return coord[1]
    
def endCoord(coord):
    if distance(coord[0],(0,0))>=distance(coord[1],(0,0)):
        return coord[0]
    else:
        return coord[1]

def distance(pos1,pos2):
    import math
    return math.sqrt(math.pow(pos2[0]-pos1[0],2)+math.pow(pos2[1]-pos1[1],2))

def isInCircle(curpos,radius,pos):
    center=(pos[0],pos[1]+radius)
    return distance(curpos,center)<=radius

def isOnLine(point,line):
    x1=line[0][0]-1
    y1=line[0][1]-1
    x2=line[1][0]+1
    y2=line[1][1]+1
    x=point[0]
    y=point[1]
    point=(x,y)
    return isInRectangle(point,[(x1,y1),(x2,y2)])

def lab11():
    gamePlay()
    
def main():
    lab11()

if __name__=="__main__":
    main()
