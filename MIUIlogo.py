# Program for MIUI logo

from turtle import *
import turtle
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('#ff620d')  #ff7634
t.pencolor('white')
t.pensize(24)
t.penup()
t.backward(144)   #the bottom line comming back
t.pendown()
# t.speed('fastest')
#For M
t.lt(90)
t.fd(120)  #left line of M
t.rt(143) #first angle
t.fd(60) #small line
t.lt(105) #2nd angle
t.fd(60) #2nd small line
t.rt(142) #3rd angle
t.fd(120)  #right line 

#For I
def I():
    t.penup()
    t.lt(90)
    t.fd(37)
    t.lt(90)
    t.pendown()
    t.fd(120) #longest line of I
I()

#For U
t.rt(90)
t.penup()
t.fd(37)
t.rt(90)
t.pendown()
t.fd(90)  #1st line of U
# t.lt(90)
t.circle(36, 180)  #40, 180
t.fd(90) #2nd line of U

#For I
t.rt(90)
t.penup()
t.fd(37)
t.rt(90)
t.pendown()
t.fd(120) #longest line of I

t.hideturtle()
done()