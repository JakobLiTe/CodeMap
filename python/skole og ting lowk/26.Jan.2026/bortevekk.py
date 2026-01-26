from turtle import *
speed(10)
shape("turtle")

sides = 12
length = 60
angle = 360 / sides
for i in range(sides):
    if i % 2 == 0:
        pencolor("red")
    else :
        pencolor("blue")
    forward(length)
    left(angle)
done()
