import turtle
import random
turtle = list()
def setup(): #Let's define a function called setup to create and position our turtles
    global turtles
    startline = -480 #The startline variable just holds the x coordinate of the starting line; you'll see how this is used below
    turtle_ycor = [-40, -20, 0, 20, 40]
    turtle_color = ['blue', 'red', 'purple', 'brown', 'green'] #Here are the initial values we need for each turtles attribute, stored in two separate parallel lists. 
    for i in range(0, len(turtle_ycor)): #Let's iterate over the number of turtles.
        new_turtle = turtle.Turtle() #And for each we'll instantiate
        new_turtle.shape('turtle') #a new turtle, make its shape a turtle, and set its position on the grid from our list.
        new_turtle.setpos(startline, turtle_ycor[i])
        new_turtle.color(turtle_color[i])
        turtles.append(new_turtle)
setup()
turtle.mainloop() #Don't forget to call the setup function, and remember we need our turtle.mainloop.