# try this either as a .py file or in the python shell
import turtle
# the distance we want the pointer to travel each time
DIST = 100

for i in range(0, 4):
    turtle.forward(DIST)
    turtle.right(90)

turtle.forward(DIST / 8)
turtle.left(90)
turtle.forward(DIST - DIST/ 12)
turtle.right(90)
turtle.forward(DIST - DIST/ 30)
turtle.right(90)
turtle.forward(DIST - DIST/ 12)

turtle.getscreen()._root.mainloop()