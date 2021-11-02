#   a117_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as t

# create an empty list of turtles
my_turtles = []


# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["gold", "purple", "orange", "green", "blue", "red"]

for s in turtle_shapes:
  t.shape(s)
  my_turtles.append(s)
  t.penup()
  t.color(turtle_colors.pop())
  t.append(t)
#  
startx = 0
starty = 0
startDir = -45
#
for t in my_turtles:
  t.goto(startx, starty)    
  #t.right(45)
  t.setheading(startDir)
  t.forward(50)
  

#	
  startx = startx + 50
  starty = starty + 50
  startDir = startDir + 45

wn = trtl.Screen()
wn.mainloop()