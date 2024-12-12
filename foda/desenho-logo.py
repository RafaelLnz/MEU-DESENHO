import turtle

turtle.pensize(1)
turtle.color("black")
turtle.speed(100)

#Lua
turtle.begin_fill()
turtle.circle(90)
turtle.end_fill()

turtle.goto(0,90)
turtle.color("white")
turtle.goto(-10,10)

turtle.fillcolor("white")
turtle.begin_fill()
turtle.circle(80)
turtle.end_fill()

turtle.color("black")
turtle.up()
turtle.goto(0,30)
turtle.down()

#LNZ
turtle.fillcolor("black")
turtle.begin_fill()

turtle.goto(60,30)
turtle.goto(-25,30)
turtle.goto(-22,45)
turtle.goto(30,90)
turtle.goto(-55,90)
turtle.goto(-45,150)
turtle.goto(-30,150)
turtle.goto(-40,102)
turtle.goto(0,102)
turtle.goto(10,150)
turtle.goto(25,150)
turtle.goto(40,120)
turtle.goto(45,150)
turtle.goto(60,150)
turtle.goto(50,102)
turtle.goto(35,102)
turtle.goto(22,130)
turtle.goto(15,102)
turtle.goto(50,102)
turtle.goto(47,85)
turtle.goto(0,45)
turtle.goto(60,45)
turtle.goto(60,30)

turtle.end_fill()

turtle.done()