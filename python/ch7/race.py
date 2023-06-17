 #Don't forget to call the setup function, and remember we need our turtle.mainloop.import turtle
import random
turtle = list()
def setup(): #Let's define a function called setup to create and position our turtles
    global turtles
    startline = -620 #The startline variable just holds the x coordinate of the starting line; you'll see how this is used below
    screen = turtle.Screen()
    screen.setup(1290,720)
    screen.bgpic('pavement.gif')
    turtle_ycor = [-40, -20, 0, 20, 40]
    turtle_color = ['blue', 'red', 'purple', 'brown', 'green'] #Here are the initial values we need for each turtles attribute, stored in two separate parallel lists. 
    for i in range(0, len(turtle_ycor)): #Let's iterate over the number of turtles.
        new_turtle = turtle.Turtle() #And for each we'll instantiate
        new_turtle.shape('turtle') #a new turtle, make its shape a turtle, and set its position on the grid from our list.
        new_turtle.penup()
        new_turtle.setpos(startline, turtle_ycor[i])
        new_turtle.color(turtle_color[i])
        new_turtle.pendown()
        turtles.append(new_turtle)
def race():
    global turtles
    winner = False
    finishline = 590
    while not winner:
        for current_turtle in turtles:
            move = random.randint(0,2)
            current_turtle.forward(move)
            xcor = current_turtle.xcor()
            if (xcor >= finishline):
                winner = True
                winner_color = current_turtle.color()
                print('The winner is', winner_color[0])
setup()
race()
turtle.mainloop()