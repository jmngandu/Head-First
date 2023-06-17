import turtle 
slowpoke = turtle.Turtle()
slowpoke.shape('turtle')
def make_square(the_turtle):
    for i in range(1000):
        the_turtle.forward(100)
        the_turtle.right(144)
make_square(slowpoke)
turtle.mainloop()