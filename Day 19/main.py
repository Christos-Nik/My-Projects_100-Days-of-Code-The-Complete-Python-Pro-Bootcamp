from turtle import Turtle, Screen 

c = Turtle()
screen = Screen()

def move_forward():
    c.fd(10)


screen.listen() # Set focus on TurtleScreen (in order to collect key-events).
screen.onkey(key="space", fun=move_forward) # Bind function to key-release event of key. In this case, when user press "space" the turtle moves forward for 10 units
screen.exitonclick()