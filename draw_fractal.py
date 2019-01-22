import turtle as tu
from collections import deque
import math
import os

class FractalPolygon:
        def __init__(self):
                self.polygons = 0
                self.sides = 0
                self.turtle = tu.Turtle()
                self.turtle.color("#FFFFFF")
                self.stack = deque()

        def draw_tresso_fractal_polygon(self, sides, height = 700, iterations = 5, tresso = True,  draw_side_method = None, change_color_level = "polygon" , color_palette = "rainbow"):
                """draw a fractal as polygon that repeats itself inside """
                #calculate side len and angle to fit the heught of the window
                side_len = self.calcucalte_side_len(sides, height)
                #set next iteration side len formula
                if(tresso):
                        next_len_formula = self.tresso_formula
                else:
                        next_len_formula = lambda side_len, sides : side_len/2
                change_side_color = False
                if change_color_level == "side":
                        change_side_color = True
                # set and save first point to start
                self.turtle.penup()
                self.turtle.setposition(-350, (-height+150)/2 )
                self.stack.append(self.get_turtle_state(self.turtle))
                self.turtle.pendown()
                #set counters
                self.polygons = 0
                self.sides = 0
                total_polygon = 0
                for i in range(iterations):
                        total_polygon = total_polygon + sides**i
                self.turtle.screen.tracer(0, 0)
                for i in range(iterations):
                        #progressively change color and pensize
                        if change_color_level == "iteration":
                                next_color = self.pick_color(i, color_palette)
                                self.turtle.color(next_color)
                        self.turtle.pensize(int(10*(1-i/iterations)))
                        for j in range(sides**i):
                                #move pen to next point and draw single polygon
                                self.turtle.penup()
                                self.restore_turtle_state(self.turtle, self.stack.popleft())
                                self.turtle.pendown()
                                if change_color_level == "polygon":
                                        next_color = self.pick_color(self.polygons, color_palette)
                                        self.turtle.color(next_color)
                                self.draw_polygon(sides, side_len, draw_side_method, change_side_color, color_palette)
                                self.polygons = self.polygons + 1

                        side_len = next_len_formula(side_len, sides)
                        self.turtle.screen.update()

        def draw_polygon(self, sides, side_len, draw_side , change_side_color = False, color_palette = "rainbow"):
                """draw polygon with n sides of side length."""   
                alpha = 360 / sides      
                for s in range(sides):
                        self.stack.append(self.get_turtle_state(self.turtle))
                        if change_side_color:
                                next_color = self.pick_color(self.sides, color_palette)
                                self.turtle.color(next_color)
                        draw_side(self.turtle, side_len)
                        self.sides = self.sides + 1
                        self.turtle.left(alpha)
        #region draw side methods
        def draw_line(self,turtle,  side_len):
                turtle.forward(side_len)

        def draw_double_semi_circle(self,turtle, side_len):
                turtle.right(90)
                turtle.circle(side_len/4, 180)
                turtle.circle(-side_len/4, 180)
                turtle.left(90)

        def draw_inner_semi_circle(self,turtle, side_len):
                turtle.left(90)
                turtle.circle(-side_len/2, 180)
                turtle.left(90)
        def draw_outer_semi_circle(self,turtle, side_len):
                turtle.right(90)
                turtle.circle(side_len/2, 180)
                turtle.right(90)
        #endregion 
        
        #region draw depth breadth
        def draw_depth_infinite(self, l,iterations=0):
                """ Draw infinite fractal """
                l = 3*l/4
                #self.turtle.screen.tracer(0, 0)
                for i in range(2**iterations):
                        self.turtle.penup()
                        self.restore_turtle_state(self.turtle, self.stack.popleft())
                        self.turtle.pendown()
                        self.draw_leaf(l)
                        self.turtle.backward(l)
                self.draw_depth_infinite(l, iterations+1)

        def draw_breadth_first(self, iterations, branches = 2, alpha = 60):
                l=100
                for j in range(iterations): 
                        print(j)
                        self.turtle.color("#00{:02x}ff".format(int(255*j/iterations)))
                        self.turtle.pensize(int(10*(1-j/iterations)))
                        self.turtle.screen.tracer(0, 0)
                        for i in range(branches**j):
                                self.turtle.penup()
                                self.restore_turtle_state(self.turtle, self.stack.popleft())
                                self.turtle.pendown()

                                self.draw_leaf(l, branches, alpha)

                        self.turtle.screen.update()
                        l = l * ((branches-1)/branches)

        def draw_leaf(self, l, branches = 2, alpha = 60 ):
                """draw leaf with a total angle alpha and branches"""
                self.turtle.left(alpha/2)
                increment = alpha * 1/(branches-1)
                self.turtle.forward(l)
                self.stack.append(self.get_turtle_state(self.turtle))
                self.turtle.backward(l)
                for b in range(1,branches):
                        self.turtle.right(increment)   
                        self.turtle.forward(l)
                        self.stack.append(self.get_turtle_state(self.turtle))
                        self.turtle.backward(l)
        #endregion
        def draw_fractal_tree(self,branches):
                self.turtle.left(90)
                self.stack.append(self.get_turtle_state(self.turtle))
                self.draw_breadth_first(iterations = 10,branches= branches, alpha = 60)


        #region save load self.turtle state
        def get_turtle_state(self, turtle):
                """ Return self.turtle's current heading and position. """
                return turtle.heading(), turtle.position()

        def restore_turtle_state(self, turtle, state):
                """ Set the self.turtle's heading and position to the given values. """
                turtle.setheading(state[0])
                turtle.setposition(state[1][0], state[1][1])
        #endregion
        #region tresso and math formulas
        def tresso_formula(self, l, n):
                """Calculate the size of the inner polygon's side so that the inners polygons touch each other but do not overlap"""
                b = 360/n * int((n-1)/4)
                b = math.radians(b)
                d = math.pi/n + b/2 
                l = l/2 * (1+ (math.sin(b/2)*math.cos(d)) / (math.sin(math.pi/n)))**-1
                return l

        def calcucalte_side_len(self,sides_number, diameter):
                """Calculate the side's length of a polygon with n sides so that it fits a circle with defined diameter"""
                l = diameter*math.sin(math.pi/sides_number)
                return l
        #endregion

        def pick_color(self, index, color_palette_name = "rainbow"):
                        rainbow = ["#9400D3", "#4B0082", "#0000FF", "#00FF00", "#FFFF00", "#FF7F00", "#FF0000"]
                        olympic = ["#0085C7", "#F4C300", "#000000", "#009F3D", "#DF0024"]
                        pastel = ["#ffb3ba","#ffdfba","#ffffba","#baffc9","#bae1ff"]
                        balance = ["#17191b","#519fa5","#f29e92","#9f2112","#371608"]

                        if color_palette_name == "rainbow":
                                colors = rainbow
                        if color_palette_name == "olympic":
                                colors = olympic
                        if color_palette_name == "pastel":
                                colors = pastel
                        if color_palette_name == "balance":
                                colors = balance

                        next_color = colors[(index)%len(colors)]
                        return next_color

        def save(self, file_name):
                #build name
                file_name = "output\\{}".format(file_name)
                if os.path.exists("{}.ps".format(file_name)) :
                        i = 0
                        while os.path.exists("{}_{}.ps".format(file_name, i)):
                                i += 1
                        file_name = "{}_{}".format(file_name, i)

                print("Saving {}.png".format(file_name))
                ts = self.turtle.getscreen()
                ts.getcanvas().postscript(file="{}.ps".format(file_name))
                os.system("convert -density 1000 {}.ps {}.png".format(file_name, file_name))



        def main_draw_fractal_polygon(self, sides,iterations = None, draw_side_method=None ,change_color_level=None,color_palette=None):
                """Draw and save fracral polygon
                
                Parameters
                ----------
                sides : int
                        number of sides of the polygon
                iterations : int
                        number of iterations
                draw_side_method : string
                        "line", "outer_semi_circle","inner_semi_circle", "double_semi_circle"
                change_color_level : string
                        change color at each "iteration", "polygon" or "side"
                color_palette : string
                        "rainbow", "olympic", "pastel", "balance"
                """
                #set default number of iterations
                if iterations == None:
                        iterations = 5
                #set color level and palette
                height = 700
                if draw_side_method == None:
                        draw_side = self.draw_line
                        height = 700
                if draw_side_method == "line":
                        draw_side = self.draw_line
                        height = 700
                if draw_side_method == "inner_semi_circle": 
                        draw_side = self.draw_inner_semi_circle
                        height = 700
                if draw_side_method == "outer_semi_circle": 
                        draw_side = self.draw_outer_semi_circle
                        height = 500
                if draw_side_method == "double_semi_circle":
                        draw_side = self.draw_double_semi_circle
                        height = 600
                
                if change_color_level == None:
                        change_color_level = "side"
                if color_palette == None:
                        color_palette = "rainbow"
                #draw
                ts = self.turtle.getscreen()
                ts.screensize(1200, 1200)
                ts.setup(width=1.0, height=1.0, startx=None, starty=None)
                fractal = FractalPolygon()
                fractal.draw_tresso_fractal_polygon(sides =sides,
                        height=height,
                        iterations=iterations,
                        draw_side_method=draw_side ,
                        change_color_level=change_color_level,
                        color_palette=color_palette)
                #save result
                self.save("fractal_{}sides_{}".format(sides, color_palette))
                input("Press Enter to continue...")

#example
fractalPolygon = FractalPolygon()
fractalPolygon.main_draw_fractal_polygon(sides=5, 
        iterations=5,  
        draw_side_method="inner_semi_circle",
        change_color_level="polygon", 
        color_palette="olympic")