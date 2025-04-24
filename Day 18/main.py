from turtle import *
import random

# colors = ["aquamarine", "beige", "black", "BlueViolet", "brown", "CadetBlue", "cyan", "DeepPink"]
# directions = [0, 90, 180, 270]
tim = Turtle()
colormode(255)
tim.shape("turtle")
tim.pensize(20)

def random_color():
    r = random.randint(0, 255)    
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

# Challenge 1: Draw a square (100 x 100)
# tim.fd(100)
# tim.lt(90)
# tim.fd(100)
# tim.lt(90)
# tim.fd(100)
# tim.lt(90)
# tim.fd(100)

# Challenge 2: Dashed line
# for _ in range(15):
#     tim.fd(10)
#     tim.up()
#     tim.fd(10)
#     tim.down()

# Challenge 3: Draw shapes (triangle, square, pentagon, hexagon, heptagon, octagon, nonagon, decagon)

# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.rt(angle)

# for shape_side_n in range(3,11):
#     draw_shape(shape_side_n)

tim.speed("fastest")
# Challenge 4: Random walk
for _ in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))



screen = Screen()
screen.exitonclick()