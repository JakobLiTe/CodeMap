from turtle import *

speed(10)
shape("turtle")

sides = 10
length = 80
angle = 360 // sides

for i in range(sides):
    if i % 2 == 0:
        pencolor("green")
    else:
        pencolor("purple")
    forward(length)
    right(angle)
done()
