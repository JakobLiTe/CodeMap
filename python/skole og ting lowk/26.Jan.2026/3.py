from turtle import *

speed(0)
shape("turtle")

sides = 30
length = 20
angle = 360 / sides

for i in range(sides):
    if i % 3 == 0:
        pencolor("red")
    elif i % 3 == 1:
        pencolor("blue")
    else:
        pencolor("black")
    forward(length)
    right(angle)
done()