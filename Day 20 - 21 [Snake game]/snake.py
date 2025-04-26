from turtle import *
STARTING_POS = [(0,0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake:
    
    def __init__(self):
        self.snakes = []
        self.create_snake()
    
    def create_snake(self):
        for position in STARTING_POS:
            new_snake = Turtle("square")
            new_snake.color("white")
            new_snake.pu()
            new_snake.goto(position)
            self.snakes.append(new_snake)

    def move(self):
        for snake_num in range(len(self.snakes)-1, 0, -1):
            new_x = self.snakes[snake_num - 1].xcor()
            new_y = self.snakes[snake_num -1].ycor()
            self.snakes[snake_num].goto(new_x, new_y)
        self.snakes[0].fd(MOVE_DISTANCE)