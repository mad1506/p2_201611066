def drawSquareAt(size, pos):
    import turtle
    wn=turtle.Screen()
    t1=turtle.Turtle()
    t1.penup()
    t1.setpos(pos)
    t1.pendown()
    tracks=list()
    for i in range(0,4):
        tracks.append(t1.pos())
        t1.forward(size)
        t1.right(90)
    return tracks

def lab7():
    mytrack=drawSquareAt(100,(10,10))
    print mytrack
    
def main():
    lab7()
    
if __name__=="__main__":
    main()
