def keyup():
    pt=t1.pos()
    print "up",pt
    t1.write(pt)
    t1.forward(45)
    print isInRectangle(pt, coord)

def keyleft():
    t1.left(45)

def keyright():
    t1.right(45)

def keydown():
    pt=t1.pos()
    print "down",pt
    t1.write(pt)
    t1.back(45)
    print isInRectangle(pt, coord)

def addKeys():
    wn.onkey(keyup, "Up")
    wn.onkey(keyleft, "Left")
    wn.onkey(keyright, "Right")
    wn.onkey(keydown, "Down")
    wn.onkey(wn.bye, "q") # Register function exit to event key_press "q"

def gamePlay():
    import turtle
    global wn
    global t1
    global coord
    coord=[(350,-300),(450,-200)]
    wn=turtle.Screen()
    wn.bgpic("myMaze.gif")
    t1=turtle.Turtle()
    t1.speed(1)
    t1.penup()
    t1.goto(-400,300)
    t1.pendown()
    t1.pencolor("Red")
    addKeys()
    wn.listen()
    turtle.mainloop()
    
def isInRectangle(curpos, coord):
    xs=coord[0][0]
    xe=coord[1][0]
    ys=coord[0][1]
    ye=coord[1][1]
    return abs(xs)<=abs(curpos[0])<=abs(xe) or abs(xe)<=abs(curpos[0])<=abs(xs) and abs(ys)<=abs(curpos[1])<=abs(ye) or abs(ye)<=abs(curpos[1])<=abs(ys)

def lab11():
    gamePlay()
    
def main():
    lab11()

if __name__=="__main__":
    main()
