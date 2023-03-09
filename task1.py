import turtle

turtle.bgcolor("lightblue")
turtle.speed(0)
#body circles
turtle.penup()
turtle.setposition(50,-100)
turtle.pendown()
turtle.pencolor("black")
turtle.fillcolor("white")
turtle.begin_fill()
turtle.circle(50)
turtle.penup()
turtle.setposition(50,-5)
turtle.pendown()
turtle.circle(35)
turtle.penup()
turtle.setposition(50,60)
turtle.pendown()
turtle.circle(25)
turtle.penup()
turtle.end_fill()

#end of body circles
#start of eyes

turtle.setposition(40,93)
turtle.pendown()
turtle.color("black")
turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()
turtle.penup()
turtle.setposition(55,93)
turtle.pendown()
turtle.color("black")
turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()

#end of eyes
#start of nose

turtle.penup()
turtle.setposition(58,83)
turtle.left(90)
turtle.pendown()
turtle.color("orange")
turtle.begin_fill()
turtle.circle(7,360,3)
turtle.end_fill()

#end of nose
#start of mouth

turtle.penup()
turtle.setposition(47,73)
turtle.seth(0)
turtle.pendown()
turtle.color("black")
turtle.forward(8)

#end of mouth
#start of buttons

turtle.left(90)
turtle.penup()
turtle.setposition(47.5,50)
turtle.right(180)
for i in range(3):
    turtle.pendown()
    turtle.color("green")
    turtle.begin_fill()
    turtle.circle(5)
    turtle.end_fill()
    turtle.penup()
    turtle.forward(15)
    
#end of buttons
#start of arms

turtle.setposition(15,35)
turtle.right(115)
turtle.pendown()
turtle.width(5)
turtle.color("brown")
turtle.forward(50)
turtle.penup()
turtle.backward(50)
turtle.left(20)
turtle.backward(70)
turtle.right(140)
turtle.pendown()
turtle.forward(50)
turtle.penup()

#end of arms
#start of fingers

turtle.setposition(-35,55)
for i in range(3):
    turtle.left(55)
    turtle.pendown()
    turtle.forward(10)
    turtle.backward(10)
turtle.penup()
turtle.setposition(125,55)
turtle.pendown()
for i in range(3):
    turtle.right(65)
    turtle.forward(10)
    turtle.backward(10)
turtle.penup()

#end of fingers
#start of hat

turtle.setposition(50,108)
turtle.seth(0)
turtle.backward(25)
for i in range(2):
    turtle.pencolor("white")
    turtle.fillcolor("green")
    turtle.width(1)
    turtle.begin_fill()
    turtle.pendown()
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.end_fill()
turtle.penup()
turtle.setposition(50,146)
turtle.pendown()
turtle.left(180)
turtle.pencolor("white")
turtle.fillcolor("green")
turtle.begin_fill()
turtle.circle(18,360,3)
turtle.end_fill()
turtle.penup()
turtle.fillcolor("white")
turtle.begin_fill()
turtle.circle(7)
turtle.end_fill()
turtle.penup()

#end of hat
#start of ground

turtle.setposition(-600,-90)
turtle.seth(0)
turtle.pendown()
turtle.color("white")
turtle.begin_fill()
for i in range(2):
    turtle.forward(1200)
    turtle.right(90)
    turtle.forward(410)
    turtle.right(90)
turtle.end_fill()

#end of ground
#start of sun

turtle.penup()
turtle.setposition(-200, 200)
turtle.pendown()
turtle.fillcolor("yellow")
turtle.pencolor("orange")
turtle.width(3)
turtle.begin_fill()
turtle.circle(50)
turtle.end_fill()

#end of sun

turtle.done()