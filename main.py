#   a117_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl

# create an empty list of turtles
my_turtles = []


# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["gold", "purple", "orange", "green", "blue", "red"]

for s in turtle_shapes:
  t = trtl.Turtle(shape=s)
  t.penup()
  t.color(turtle_colors.pop())
  t.pencolor("black")
  my_t
 
#  
startx = 0
starty = 0
startDir = -45
#
for t in my_turtles:
  t.goto(startx, starty)  
  t.pendown()  
  t.setheading(startDir)
  t.forward(50)
  

#	
  startx = t.xcor + 50
  starty = t.ycor + 50
  startDir += 45

wn = t.Screen()
wn.mainloop()