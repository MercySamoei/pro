import turtle
t= turtle.Pen

def mystar(size, filled):
 if filled == True:
    t.begin_fill()
 for x in range(1, 19):
    t.forward(size)
    if x % 2 == 0:
        t.left(175)
    else:
        t.left(225)
    if filled == True:
        t.end_fill()


mystar(120, True)

##Repeat this code!!!!!!!!!!!!!!!!!