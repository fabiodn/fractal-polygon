import turtle as tu
import random 
from collections import deque

stack = deque()
stack_heading = deque()
c = 100
#recursion

def get_turtle_state(turtle):
    """ Return turtle's current heading and position. """
    return turtle.heading(), turtle.position()

def restore_turtle_state(turtle, state):
    """ Set the turtle's heading and position to the given values. """
    turtle.setheading(state[0])
    turtle.setposition(state[1][0], state[1][1])

def draw2(l,iterations):
    l = 3*l/4
    #turtle.screen.tracer(0, 0)
    for i in range(2**iterations):
        turtle.penup()
        restore_turtle_state(turtle, stack.popleft())
        turtle.pendown()

        draw_leaf(l)
        turtle.backward(l)
        #turtle.screen.update()
        #print(stack)
    
    draw2(l, iterations+1)

def draw3(iterations, branches = 2, alpha = 60):
    l=100
    for j in range(iterations): 
        print(j)
        turtle.color("#00{:02x}ff".format(int(255*j/iterations)))
        turtle.pensize(int(10*(1-j/iterations)))
        turtle.screen.tracer(0, 0)
        for i in range(branches**j):
            turtle.penup()
            restore_turtle_state(turtle, stack.popleft())
            turtle.pendown()

            draw_leaf(l, branches, alpha)

        turtle.screen.update()
        l = 3*l/4

def draw_leaf(l, branches = 2, alpha = 60 ):
    turtle.left(alpha/2)
    increment = alpha * 1/(branches-1)
    turtle.forward(l)
    stack.append(get_turtle_state(turtle))
    turtle.backward(l)
    for b in range(1,branches):
        turtle.right(increment)   
        turtle.forward(l)
        stack.append(get_turtle_state(turtle))
        turtle.backward(l)



def init_stack():
    turtle = tu.Turtle()
    turtle.left(90)
    stack.append(get_turtle_state(turtle))
    return turtle

turtle = init_stack()

draw3(6, 3, 245)
ts = turtle.getscreen()
ts.getcanvas().postscript(file="C:\\Users\\Administrator\\Desktop\\duck.ps")

input("Press Enter to continue...")
