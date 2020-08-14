# initials program 
from turtle import *

# Do not change these lines (and do not create your own turtle... use t for your initials
t = Turtle()
t.speed(3)

# first initials (well, it is a box...)
t.up()
t.pencolor('red')
t.pensize(3)
t.forward(200)
t.left(90)
t.down()
t.forward(200)
t.left(90)
t.forward(400)
t.left(90)
t.forward(400)
t.left(90)
t.forward(400)
t.left(90)
t.forward(200)

t.reset()


# add your initials below and then call t.reset(), like above, so that 
# the turtle goes back to the initial state for the next initials to state
# (the pencolor and pensize are also reset).
# draw your initials with a different pensize and pencolor

t.pencolor('green')
t.pensize(3)
t.left(90)
t.down()
t.forward(80)
t.left(180)
t.up()
t.forward(80)
t.left(150)
t.down()
t.forward(55)
t.right(120)
t.down()
t.forward(55)
t.left(150)
t.down()
t.forward(80)
t.right(180)
t.up()
t.forward(80)
t.left(90)
t.up()
t.forward(10)
t.down()
t.forward(1)
t.up()
t.forward(10)
t.left(90)
t.down()
t.forward(80)
t.right(90)
t.down()
t.forward(40)
t.left(180)
t.up()
t.forward(40)
t.left(90)
t.up()
t.forward(80)
t.left(90)
t.down()
t.forward(45)

t.reset()







# leave the input() function at the bottom of the code
input('hit enter to exit')




