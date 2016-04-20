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
        
def replayTracks(myTracks):
    t1.clear()
    t1.color("blue")
    t1.speed(5)
    for t in myTracks:
        t1.goto(t)

def lab7():
    global wn
    global t1
    import turtle
    wn=turtle.Screen()
    t1=turtle.Turtle()
    mytrack=drawSquareAt2(100,(10,10))
    print mytrack
    drawSquareFrom(100)
    
    import turtle
    wn=turtle.Screen()
    #wn.bgpic("myMaze.gif")
    t1=turtle.Turtle()
    t1.speed(6)
    t1.penup()

    myTracks=list()

    t1.goto(-400,300)
    myTracks.append(t1.pos())
    t1.pendown()
    t1.pencolor("Red")
    t1.right(90)
    t1.fd(400)
    myTracks.append(t1.pos())
    t1.backward(150)
    myTracks.append(t1.pos())
    t1.left(90)
    t1.fd(300)
    myTracks.append(t1.pos())
    t1.left(90)
    t1.fd(300)
    myTracks.append(t1.pos())
    t1.back(150)
    myTracks.append(t1.pos())
    t1.right(90)
    t1.fd(300)
    myTracks.append(t1.pos())
    t1.left(90)
    t1.right(90)
    t1.right(90)
    t1.fd(200)
    myTracks.append(t1.pos())
    t1.fd(300)
    myTracks.append(t1.pos())
    t1.back(100)
    myTracks.append(t1.pos())
    t1.left(90)
    t1.fd(200)
    myTracks.append(t1.pos())
    
    replayTracks(myTracks)
    
def main():
    lab7()
    
if __name__=="__main__":
    main()
