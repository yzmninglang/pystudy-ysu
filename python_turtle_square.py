import turtle as t 
t.speed("fastest")
t.pensize(2)
t.colormode(255)
coloes=["blue","green","red","gray"]
i=1
for r in range(255):
    for g in range(255):
        for b in range(255):
            t.color(r,g,b)
            t.forward(4*i/100)
            i=1+i
            t.left(91)
t.done()



#     # t.pencolor(coloes[i%4])
#     t.pencolor(i,i,i)
#     t.forward(4*i)
#     t.left(91)
# t.done()
