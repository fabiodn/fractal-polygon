# Tresso Fractal Polygons
![alt text](https://github.com/fabiodn/test/blob/master/output/fractal_inverted_pentagon.png)
## Draw fractal polygon where the polygons are repeated inside each other
FractalPolygon is the class that wraps all the functions.  
main_draw_fractal_polygon is the main function (entry point) to draw Fractal.  

Attributes to play with:
```
def main_draw_fractal_polygon(self,
    sides,iterations = None,
    draw_side_method=None,
    change_color_level=None,
    color_palette=None):
```

```
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
```

Example:  
```
fractalPolygon = FractalPolygon()
fractalPolygon.main_draw_fractal_polygon(sides=5, 
        iterations=5,  
        draw_side_method="inner_semi_circle",
        change_color_level="polygon", 
        color_palette="olympic")
```

### Output
The postscript result is saved inside "output" folder.  
It automatically transalates the postscript file into .png but you have to install  
[ImageMagick](https://imagemagick.org/script/download.php)  
[GPL GhostScript](https://www.ghostscript.com/download.html)  

## Tresso Formla
Calculates the size of the inner polygon's side so that the inners polygons touch each other but do not overlap.
![alt text](https://github.com/fabiodn/fractal-polygon/blob/master/Tresso_formula.jpg)