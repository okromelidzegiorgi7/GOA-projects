from turtle import *


speed(3)
width(7)

# სახლის კედელი
width(7)
color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

# კარი
forward(70)
color("yellow")
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()

# სახურავი
penup()
goto(0, 200)
setheading(0)
pendown()
color("red")

left(45)
forward(141)
right(90)
forward(141)

#ფანჯარა
penup()
goto(200, 150)

exitonclick()


