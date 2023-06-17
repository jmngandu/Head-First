import turtle 
slowpoke = turtle.Turtle()
slowpoke.shape('turtle')
def make_square(the_turtle):
    the_turtle.forward(100)
    the_turtle.right(90)
    the_turtle.forward(100)
    the_turtle.right(90)
    the_turtle.forward(100)
    the_turtle.right(90)
    the_turtle.forward(100)
    the_turtle.right(90)
make_square(slowpoke)
turtle.mainloop()