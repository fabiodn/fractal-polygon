import turtle as tu
import random 
from collections import deque
import math
import io
import os
from PIL import Image

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

def draw_tresso_fractal_polygon(sides, height = 800, iterations = 7, tresso = True):
        """draw a fractal as polygon that repeats itself inside """
        #calculate side len and angle
        side_len = calcucalte_side_len(sides, height)
        #set next iteration side len formula
        if(tresso):
                next_len_formula = tresso_formula
        else:
                next_len_formula = lambda side_len, sides : side_len/2
        #save first point to start
        turtle.penup()
        turtle.setposition(-350,-350 )
        stack.append(get_turtle_state(turtle))
        turtle.pendown()
        for i in range(iterations):
                #progressively change color and pensize
                pick_color(turtle, i, iterations)
                turtle.pensize(int(10*(1-i/iterations)))
                turtle.screen.tracer(0, 0)
                for j in range(sides**i):
                        #pick_color(turtle, j, iterations)
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

def pick_color(turtle, i, iterations):
        rainbow = ["#9400D3", "#4B0082", "#0000FF", "#00FF00", "#FFFF00", "#FF7F00", "#FF0000"]
        #next_color = rainbow[i%iterations]
        next_color = "#00{:02x}ff".format(int(255*i/iterations))
        turtle.color(next_color)
        return next_color

def save(file_name):
        ts = turtle.getscreen()
        ts.screensize(1200, 1200)
        ts.setup(width=1.0, height=1.0, startx=None, starty=None)
        ts.getcanvas().postscript(file="{}.ps".format(file_name))
        os.system("convert -density 1000 {}.ps {}.png".format(file_name, file_name))

#init turtle and stack golabal variable
turtle = tu.Turtle()
stack = deque()
#draw 

draw_tresso_fractal_polygon(sides=5, iterations= 5)
#save result
save("fractal")

input("Press Enter to continue...")
