import turtle
from math import sin, cos, tan,radians
wn = turtle.Screen()
wn.bgcolor("black")
f = turtle.Turtle()

f.penup()
f.goto(0, -200)
f.pendown()
f.color("white")
iteration = 5
m = ["#F26C4F", "#F68E55","#FFF467","#3BB878","#438CCA","#855FA8"]

#s = ["red", "orange", "yellow", "green", "blue", "purple"]
c = 0 
distance = 100
k =0;

def move(dis, f):
    #global k;
    #global m;
    #global c;
    #k += 1;
    #if k%30==0:
        #c += 1;
        #f.color(m[c%len(m)])
    if dis>2:
        f.speed(10000)
        f.forward(dis)
        f.left(30)
        move(dis*0.7, f)
        f.right(60)
        move(dis*0.7,f)
        f.left(30)
        f.backward(dis)

f.left(90)
#f.forward(distance)
move(distance, f)





    
wn.exitonclick()
