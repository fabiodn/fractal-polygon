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

def draw_polygon(sides , l  , position, save = False):
        alpha = 180 / sides
        turtle.penup()
        restore_turtle_state(turtle, position)
        turtle.setheading(0)
        turtle.pendown()

        turtle.forward(l)
        if(save):
                stack.append(get_turtle_state(turtle))
        for s in range(1,sides-1):
                turtle.left(alpha*2)
                turtle.forward(l)
                if(save):
                        stack.append(get_turtle_state(turtle))
        turtle.left(alpha*2)
        turtle.forward(l)




def draw_inverted_polygon(sides = 3, l = 100):
        alpha = 180 / sides
        turtle.penup()
        restore_turtle_state(turtle, stack.popleft())
        turtle.pendown()

        turtle.left(alpha)
        turtle.forward(l)
        stack.append(get_turtle_state(turtle))
        for s in range(1,sides):
                turtle.left(alpha*2)
                turtle.forward(l)
                stack.append(get_turtle_state(turtle))

def draw_fractal_polygon(sides, l ):
        iterations = 5
        
        for i in range(iterations):
                turtle.color("#00{:02x}ff".format(int(255*i/iterations)))
                turtle.pensize(int(10*(1-i/iterations)))
                turtle.screen.tracer(0, 0)
                n = len(stack)
                for s in range(n*sides):
                        if s < n:
                                draw_polygon(sides, l/2, stack[s], True)
                        else:
                                draw_polygon(sides, l/2, stack[s], False)
                turtle.screen.update()
                l = l / 2

def init(turtle):
        """init stack and turtle"""
        turtle.left(90)
        stack.append(get_turtle_state(turtle))

def draw_relative_polygon(sides, l,position, heading):
        alpha = 180 / sides
        turtle.penup()
        restore_turtle_state(turtle, position)
        turtle.setheading(turtle.heading() + heading)
        turtle.pendown()

        stack.append(get_turtle_state(turtle))
        turtle.forward(l)
        stack.append(get_turtle_state(turtle))
        for s in range(1,sides-1):
                turtle.left(alpha*2)
                turtle.forward(l)
                stack.append(get_turtle_state(turtle))
        turtle.left(alpha*2)
        turtle.forward(l)
        #stack.append(get_turtle_state(turtle))

def draw_relative_polygon_init(sides, l):
        alpha = 180 / sides

        turtle.forward(l)
        stack.append(get_turtle_state(turtle))
        for s in range(1,sides):
                turtle.left(alpha*2)
                turtle.forward(l)
                stack.append(get_turtle_state(turtle))


def draw_fractal_relative_polygon(sides, l, iteration= 0):
        draw_relative_polygon_init(sides, l)
        l = l/2
        alpha = 180 / sides
        
        for j in range(5):
                n = len(stack)
                for i in range(n):        
                        alpha = (alpha*2*i)%360
                        print("i:{} iteration:{} alpha:{}".format(i, iteration, alpha))
                        position = stack.popleft()

                        draw_relative_polygon(sides, l,position,alpha)
                iteration = iteration + 1
                l= l/2

def main():
        init(turtle)
        draw_breadth_first(iterations = 10, branches= 3, alpha = 60)
        #save result as post script file
        ts = turtle.getscreen()
        ts.getcanvas().postscript(file="post_script_result.ps")

def tresso_formula(l, n):
        b = 360/n * int((n-1)/4)
        b = math.radians(b)
        l = l/2 * (1+ (math.sin(b/2)*math.cos(b)) / (math.tan(math.pi/n)*math.cos(math.pi/n)))**-1
        return l

def test_tresso_formula(sides):
        l=100
        iterations = 5
        bho = 5

        alpha = 360 / sides
        stack.append(get_turtle_state(turtle))
        for j in range(bho):
                for i in range(iterations):
                        turtle.penup()
                        restore_turtle_state(turtle, stack.popleft())
                        turtle.pendown()
                        for s in range(0,sides):
                                stack.append(get_turtle_state(turtle))
                                turtle.forward(l)
                                turtle.left(alpha)
                l = tresso_formula(l, sides)



def main_2():
        sides = 12
        l = 300
        stack.append(get_turtle_state(turtle))
        #draw_polygon(sides, l, stack[0], False)
        #draw_fractal_polygon(sides, l)
        #draw_fractal_relative_polygon(3, 100)
        test_tresso_formula(sides)
turtle = tu.Turtle()
stack = deque()
main_2()
input("Press Enter to continue...")