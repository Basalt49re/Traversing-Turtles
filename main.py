#   a117_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl

# create an empty list of turtles
my_turtles = []
my_colors = []
direction = 45

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["gold", "purple", "orange", "green", "blue", "red"]

for s in turtle_shapes:
  t = trtl.Turtle(shape=s)
  my_turtles.append(t)

#  
startx = 0
starty = 0

#
for t in my_turtles:
  t.goto(startx, starty)    
  #t.right(45)
  t.setheading(direction)
  t.forward(50)
  direction = t.heading()

#	
  startx = startx + 50
  starty = starty + 50
  direction = direction - 45

wn = trtl.Screen()
wn.mainloop()