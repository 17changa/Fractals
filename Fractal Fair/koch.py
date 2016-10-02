import turtle
wn = turtle.Screen()
wn.bgcolor("black")
f1 = turtle.Turtle()
f1.penup()
f1.goto(-680, -175)
f1.pendown()
f1.color("purple")

f2 = turtle.Turtle()
f2.penup()
f2.goto(-680, -200)
f2.pendown()
f2.color("red")

f3 = turtle.Turtle()
f3.penup()
f3.goto(-680, -195)
f3.pendown()
f3.color("orange")

f4 = turtle.Turtle()
f4.penup()
f4.goto(-680, -190)
f4.pendown()
f4.color("yellow")

f5 = turtle.Turtle()
f5.penup()
f5.goto(-680, -185)
f5.pendown()
f5.color("green")

f6 = turtle.Turtle()
f6.penup()
f6.goto(-680, -180)
f6.pendown()
f6.color("blue")
#h = turtle.Turtle()
#h.penup()
#h.goto(-680,-200)
#h.pendown()
#h.color("white")
#h.forward(2000)

dis = 2
x = ["red", "orange", "yellow", "green", "blue", "purple"]
c = 0 
k =0
def koch(f,n,s):
    #global k;
    #global x;
    #global c;
    #k += 1;
    #if k%30==0:
        #c += 1;
        #f.color(x[c%len(x)])    
    if n==1:
        f.forward(s)
    if n>1:
        f.speed(0)
        koch(f,n-1,s)
        f.left(60)
        koch(f,n-1,s)
        f.right(120)
        koch(f,n-1,s)
        f.left(60)
        koch(f,n-1,s)
        
koch(f1, 7,dis)
koch(f2, 7,dis)
koch(f3, 7,dis)
koch(f4, 7,dis)
koch(f5, 7,dis)
koch(f6, 7,dis)
wn.exitonclick()
