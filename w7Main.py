def drawSquareAt(size, pos):
    t1.penup()
    t1.setpos(pos)
    t1.pendown()
    for i in range(0,4):
        t1.forward(size)
        t1.right(90)

def drawSquareAt2(size, pos):

    t1.penup()
    t1.setpos(pos)
    t1.pendown()
    track=list()
    for i in range(0,4):
        track.append(t1.pos())
        t1.forward(size)
        t1.right(90)
    return track

def drawSquareFrom(tracks):
    tracks=list()
    tracks.append((-200,-200))
    tracks.append((-200,200))
    tracks.append((200,-200))
    tracks.append((200,200))
    for i in range(0,4):
        drawSquareAt(100,tracks[i])

def lab7():
    global wn
    global t1
    import turtle
    wn=turtle.Screen()
    t1=turtle.Turtle()
    mytrack=drawSquareAt2(100,(10,10))
    print mytrack
    drawSquareFrom(100)
    
def main():
    lab7()
    
if __name__=="__main__":
    main()
