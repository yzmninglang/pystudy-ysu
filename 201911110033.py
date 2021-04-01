import turtle as t 
def drawSnake(rad,angle,len,neckrad):
    # the colors is red , blue , green, every color fill two sections
    colors=['235, 66, 53','235, 66, 53','68,133,245','68,133,245','53,168,80','53,168,80']
    for i,color in zip(range(len),colors):
        t.pencolor(eval(color))
        t.circle(rad,angle)
        t.circle(-rad,angle)
    t.circle(rad,angle/2)
    t.fd(rad)
    t.color(249, 36, 114)  #The neck's color is red 
    t.circle(neckrad+1,180)
    t.fd(rad*2/3)


def eye(size):
    t.pensize(size)
    t.penup()
    t.forward(-10)
    t.pendown()
    t.pencolor(0,0,0)
    t.fillcolor(0,0,0)
    t.begin_fill()
    t.circle(-size)
    t.end_fill()

def main():
    t.colormode(255)   #In this program I use RGB mode instead of english name
    t.speed('fastest')
    t.setup(1300,1300,0,0)
    t.right(180)    
    t.penup()
    t.goto(-370,10)
    pythonsize=40
    t.pensize(pythonsize)
    t.pendown()
    t.seth(-40)
    drawSnake(40,80,6,pythonsize)
    eye(5)
    t.hideturtle() 
    t.done() 

if __name__=='__main__':
    main()