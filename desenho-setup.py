import turtle
# Selecionar com o mouse + Ctrl + D = seleciona todas as variáveis que tenha a palavra que você selecionou com o mouse.
turgo = turtle.goto

turtle.fillcolor("black")



turtle.pensize(1)
turtle.color("black")
turtle.speed(10)

#Monitor
turgo(0,100)
turgo(170,100)
turgo(170,0)
turgo(0,0)
turtle.penup()
turgo(10,10)
turtle.pendown()

turtle.begin_fill()
turgo(10,90)
turgo(160,90)
turgo(160,10)
turgo(10,10)
turtle.end_fill()
turgo(85,10)
turgo(85,-30)
turgo(95,-30)
turgo(95,10)
turgo(95,-30)
turgo(140,-30)
turgo(140,-40)
turgo(40,-40)
turgo(40,-30)
turgo(95,-30)

#Teclado
turtle.penup()
turgo(95,-80)
turtle.pendown()
turgo(180,-80)
turgo(170,-120)
turgo(0,-120)
turgo(10,-80)
turgo(95,-80)
turgo(180,-80)

#Gabinete
turtle.penup()
turgo(270,-80)
turtle.pendown()
turgo(270,110)
turgo(370,110)
turgo(370,-80)
turgo(270,-90)
turgo(270,0)
turgo(270,-90)
turgo(255,-40)
turgo(255,120)
turgo(355,120)
turgo(370,110)
turgo(270,110)
turgo(255,120)

#Mesa
turtle.penup()
turgo(-70,-15)
turtle.pendown()
turgo(-150,-140)
turgo(390,-140)
turgo(400,-15)
turgo(370,-15)
turtle.penup()
turgo(255,-15)
turtle.pendown()
turgo(95,-15)
turtle.penup()
turgo(85,-15)
turtle.pendown()
turgo(-70,-15)

#Teclas
turtle.penup()
turgo(15,-80)
turtle.pendown()
turgo(5,-120)
turgo(10,-120)
turgo(20,-80)
turgo(25,-80)
turgo(15,-120)
turgo(20,-120)
turgo(30,-80)
turgo(35,-80)
turgo(27,-115)
turgo(32,-115)
turgo(40,-80)
turgo(45,-80)
turgo(37,-115)
turgo(42,-115)
turgo(50,-80)
turgo(55,-80)
turgo(47,-115)
turgo(52,-115)
turgo(60,-80)
turgo(65,-80)
turgo(55,-120)

turtle.done()