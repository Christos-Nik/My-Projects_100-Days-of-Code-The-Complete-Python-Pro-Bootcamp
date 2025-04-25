from turtle import Turtle, Screen
import random

race_mode = False
screen = Screen()
screen.setup(width = 500, height = 400)
user_bet = screen.textinput(title = "Make your bet", prompt="Which turtle will win the race? Enter a color:")
turtle_colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_pos = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtles in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(turtle_colors[turtles])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_pos[turtles])
    all_turtles.append(new_turtle)

if user_bet:
    race_mode = True

while race_mode:

    for turtle in all_turtles:
        if turtle.xcor() >= 230:
            race_mode = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print(f"You've won! The {winning_turtle} turtle is the winner!!!")
            else:
                print(f"You've lost! The {winning_turtle} turtle is the winner!!!")
        
        rand_dist = random.randint(0, 10)
        turtle.forward(rand_dist)




screen.exitonclick()