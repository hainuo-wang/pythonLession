import turtle

turtle.pensize(4)
turtle.pencolor("yellow")
turtle.fillcolor("red")
turtle.begin_fill()
for _ in range(5):
    turtle.forward(200)
    turtle.right(144)
turtle.end_fill()
turtle.mainloop()
