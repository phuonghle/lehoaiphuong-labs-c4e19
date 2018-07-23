from random import *
# from eval import calc
import eval

print("* " * 20)


# random x, y, op, err [-1, 0, 1] -> display_res
x = randint(1, 10)
y = randint(1, 10)
op = ["+", "-", "*", "/"]
rand_op = choice(op)
err = [-1, 0, 1]
rand_err = choice(err)


display_res = 0

res = eval.calc(x, y, rand_op)

# print out the equation


display_res = res + rand_err
print("{} {} {} = {}".format(x, rand_op, y, display_res))

print("* " * 20)
# ask

ques = input("Y/N? ").upper()

# check 

if ques == "Y":
    if rand_err == 0:
        print("Yay")
    else:
        print("You are wrong")
elif ques == "N":
    if rand_err == 0:
        print("You are wrong")
    else:
        print("Yay")

