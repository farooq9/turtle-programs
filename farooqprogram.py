import turtle
pen = turtle.Turtle()
t = turtle.Screen()
t.bgcolor('black')
pen.color('red')
turtle.speed(10)



# rectangle
pen.pensize(9)
pen.fd(260) #bottom starting line
pen.lt(90)
pen.fd(170) #right line
pen.lt(90)
pen.fd(470) #upper line
pen.lt(90)
pen.fd(170) #left line
pen.lt(90)
pen.fd(210) #bottom ending line

# for F
pen.pensize(9)
pen.penup()
pen.lt(180)
pen. fd(180) #bottom ending double line 
pen.rt(90)
pen.fd(25)
pen.pendown()
pen.fd(120) #straight line
pen.rt(90)
pen.fd(60) # small top line
pen.penup()
pen.rt(90)
pen.fd(55)
pen.rt(90)
pen.fd(20)
pen.pendown()
pen.fd(42) #small middle line

#for A
pen.penup()
pen.lt(90)
pen.fd(63)
pen.lt(90)
pen.fd(75)
pen.pendown()
pen.lt(90)
pen.fd(120)
pen.rt(90)
pen.fd(50)
pen.rt(90)
pen.fd(60)
pen.rt(90)
pen.fd(50)
pen.rt(180)
pen.fd(50)
pen.rt(90)
pen.fd(60)

#for R
pen.penup()
pen.lt(90)
pen.fd(20)
pen.pendown()
pen.lt(90)
pen.fd(120)
pen.rt(90)
pen.fd(50)
pen.rt(90)
pen.fd(60)
pen.rt(90)
pen.fd(50)
pen.lt(135)
pen.fd(85)
pen.rt(135)
pen.penup()
pen.fd(50)

#for 3 O
for i in range(3):
    pen.rt(180)
    pen.penup()
    pen.fd(70)
    pen.pendown()
    pen.lt(90)
    pen.fd(120)
    pen.rt(90)
    pen.fd(50)
    pen.rt(90)
    pen.fd(120)
    pen.rt(90)
    pen.fd(50)

#for line in Q
pen.rt(135)  
pen.penup()  
pen.fd(35)
pen.pendown()
pen.rt(90)
pen.fd(50)
turtle.done()

