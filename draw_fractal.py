import turtle as tu
import random 
from collections import deque
import math

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

def tresso_formula(l, n):
        """Calculate the size of the inner polygon's side so that the inners polygons touch each other but do not overlap"""
        b = 360/n * int((n-1)/4)
        b = math.radians(b)
        d = math.pi/n + b/2 
        l = l/2 * (1+ (math.sin(b/2)*math.cos(d)) / (math.tan(math.pi/n)*math.cos(math.pi/n)))**-1
        return l
def calcucalte_side_len(sides_number, diameter):
        """Calculate the side's length of a polygon with n sides so that it fits a circle with defined diameter"""
        l = diameter*math.sin(math.pi/sides_number)
        return l

def draw_tresso_fractal_polygon(sides, height = 400, iterations = 5, tresso = True):
        """draw a fractal as polygon that repeats itself inside """
        #calculate side len and angle
        side_len = calcucalte_side_len(sides, height)
        #set next iteration side len formula
        if(tresso):
                next_len_formula = tresso_formula
        else:
                next_len_formula = lambda side_len, sides : side_len/2
        #save first point to start
        stack.append(get_turtle_state(turtle))
        for i in range(iterations):
                #progressively change color and pensize
                turtle.color("#00{:02x}ff".format(int(255*i/iterations)))
                turtle.pensize(int(10*(1-i/iterations)))
                turtle.screen.tracer(0, 0)
                for j in range(sides**i):
                        #move pen to next point and draw single polygon
                        turtle.penup()
                        restore_turtle_state(turtle, stack.popleft())
                        turtle.pendown()
                        draw_polygon(sides, side_len)

                side_len = next_len_formula(side_len, sides)
                turtle.screen.update()

def draw_polygon(sides, side_len):
        """draw polygon with n sides of side length."""   
        alpha = 360 / sides      
        for s in range(sides):
                stack.append(get_turtle_state(turtle))
                turtle.forward(side_len)
                turtle.left(alpha)

def draw_fractal_tree(branches):
        turtle.left(90)
        stack.append(get_turtle_state(turtle))
        draw_breadth_first(iterations = 10,branches= branches, alpha = 60)

#init turtle and stack golabal variable
turtle = tu.Turtle()
stack = deque()
#draw 
draw_tresso_fractal_polygon(sides=5)
#save result
ts = turtle.getscreen()
ts.getcanvas().postscript(file="post_script_result.ps")
input("Press Enter to continue...")