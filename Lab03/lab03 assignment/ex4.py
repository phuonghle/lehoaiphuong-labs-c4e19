# Now, another programmer named ‘T.Anh’ will use your code in exercise 3. He writes as follows:
from ex3 import draw_square
from turtle import *


for i in range(30):
    draw_square(i * 5, 'red')
    left(17)
    penup()
    forward(i * 2)
    pendown()

mainloop()