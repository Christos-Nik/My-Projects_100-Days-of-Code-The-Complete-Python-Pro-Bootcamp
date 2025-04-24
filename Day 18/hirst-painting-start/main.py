###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import colorgram
rgb_colors = []
colors = colorgram.extract("C:\\Users\Christos\\Documents\\GitHub\\My-Projects_100-Days-of-Code-The-Complete-Python-Pro-Bootcamp\\Day 18\\hirst-painting-start\\image.jpg", 30)
for color in colors:
    rgb_colors.append(color.rgb)

print(rgb_colors)