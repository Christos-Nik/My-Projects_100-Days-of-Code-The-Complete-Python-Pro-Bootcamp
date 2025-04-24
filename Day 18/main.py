from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.color("blue")

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




screen = Screen()
screen.exitonclick()