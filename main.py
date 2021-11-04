#Names of Partners: Albert Yang Period 2
#   a117_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl
t=trtl.Turtle()
# create an empty list of turtles
my_turtles = []


# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold"]

turtlecolor = 0

if(turtlecolor==0):
  t.pencolor("yellow")
while(turtlecolor==1):
  t.pencolor("purple")
while(turtlecolor==2):
  t.pencolor("orange")
while(turtlecolor==3):
  t.pencolor("green")
while(turtlecolor==4):
  t.pencolor("blue")
while(turtlecolor==5):
  t.pencolor("red")

for s in turtle_shapes:
  t = trtl.Turtle(shape=s)
  t.penup()
  t.color(turtle_colors.pop())
  my_turtles.append(t)
  turtlecolor +=1
 
#  
startx = 0
starty = 0
startDir = 90
#
for t in my_turtles:
  t.goto(startx, starty)  
  t.pendown()  
  t.setheading(startDir)
  t.right(45)
  t.forward(50)
#	
  startx = t.xcor()
  starty = t.ycor()
  startDir = t.heading()

wn = trtl.Screen()
wn.mainloop()