#1st Object-oriented Programming (OOP) project + Examples

# from turtle import *
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("CadetBlue2")

# my_screen = Screen()
# print(my_screen.canvheight)

# timmy.forward(100)
# my_screen.exitonclick()

from prettytable import *

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
# table.align["Pokemon Name"] = "l"
# table.align["Type"] = "l"
print(table)