
from turtle import *
import math

# Name your Turtle.
t = Turtle()

# Set Up your screen and starting position.
setup(500,300)
### Write your code below:
begin_fill()
pencolor("red")
fillcolor("green")
numsides=8
angle=360/numsides
for hops in range(numsides):
    forward(50)
    right(angle)
end_fill()

# Close window on click.
exitonclick()
