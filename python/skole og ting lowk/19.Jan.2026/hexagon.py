import turtle
t = turtle.Turtle()
turtle.speed(100)
turtle.pencolor("red")
turtle.shape("turtle")

forward = 5
forward_change = 0.1
max_forward = 112

for i in range(20000):
    turtle.forward(forward)
    turtle.left(10)

    forward += forward_change

    if forward > max_forward or forward < 2:
        forward_change *= -1
turtle.end_fill()