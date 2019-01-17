import turtle as tu
import random 
from collections import deque

def get_turtle_state(turtle):
    """ Return turtle's current heading and position. """
    return turtle.heading(), turtle.position()

def restore_turtle_state(turtle, state):
    """ Set the turtle's heading and position to the given values. """
    turtle.setheading(state[0])
    turtle.setposition(state[1][0], state[1][1])

def draw_depth_infinite(l,iterations=0):
        """ Draw infinite fractal """
        l = 3*l/4
        #turtle.screen.tracer(0, 0)
        for i in range(2**iterations):
                turtle.penup()
                restore_turtle_state(turtle, stack.popleft())
                turtle.pendown()
                draw_leaf(l)
                turtle.backward(l)
        draw_depth_infinite(l, iterations+1)

def draw_breadth_first(iterations, branches = 2, alpha = 60):
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
        l = l * ((branches-1)/branches)

def draw_leaf(l, branches = 2, alpha = 60 ):
        """draw leaf with a total angle alpha and branches"""
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


def init(turtle):
        """init stack and turtle"""
        turtle.left(90)
        stack.append(get_turtle_state(turtle))

def main():
        init(turtle)
        draw_breadth_first(iterations = 10, branches= 3, alpha = 60)
        #save result as post script file
        ts = turtle.getscreen()
        ts.getcanvas().postscript(file="post_script_result.ps")
        input("Press Enter to continue...")

turtle = tu.Turtle()
stack = deque()
main()