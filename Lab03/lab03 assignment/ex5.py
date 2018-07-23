# Write a Python function that draws a star, named draw_star, take 3 parameters: x, y, and length. 
# Where x, y are the location of the star, length is the length of its side


from turtle import *



def draw_star(x, y, length):
    
    up()
    goto(x, y)
    down()

    for i in range(5):
        right(144)
        forward(length)



    mainloop()

draw_star(15, 15, 100)