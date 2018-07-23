# Write a Python function that draws a square, named draw_square, 
# takes 2 arguments: length and square_color, 
# where length is the length of its side and square_color is the square_color of its bound 
# (line color)



from turtle import *

def draw_square(lenght_square, square_color):

    # shape("turtle")
    # speed(-1)

    color(square_color)

    for i in range(4):
        forward(lenght_square * 100)
        right(90)
    



    mainloop()

# draw_square(100, "yellow")