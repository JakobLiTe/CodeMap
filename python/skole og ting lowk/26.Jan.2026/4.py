from turtle import *

speed(10)
shape("turtle")

sides = 5
angle = 360 / sides
distance = 100

for i in range(sides):
    for i in range(5):
        if distance == 50:
            distance = 100
        elif distance == 100:
            distance = 50

    forward(distance)
    right(angle)

done()