from turtle import Turtle, Screen

screen = Screen()
screen.setup(width = 500, height = 400)
user_bet = screen.textinput(title = "Make your bet", prompt="Which turtle will win the race? Enter a color:")
turtle_colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_pos = [-70, -40, -10, 20, 50, 80]

for turtles in range(0,6):
    tim = Turtle(shape="turtle")
    tim.color(turtle_colors[turtles])
    tim.penup()
    tim.goto(x=-230, y=y_pos[turtles])




screen.exitonclick()