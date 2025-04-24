from turtle import Turtle, Screen 

c = Turtle()
screen = Screen()

def move_forward():
    c.fd(10)


screen.listen()
screen.onkey(key="space", fun=move_forward)
screen.exitonclick()