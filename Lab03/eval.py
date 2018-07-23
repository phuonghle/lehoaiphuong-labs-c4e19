
# definition

# arguments

def calc(x, y, rand_op):

    res = 0

    # print out the equation

    if rand_op == "+":
        res = x + y
    elif rand_op == "-":
        res = x - y
    elif rand_op == "*":
        res = x * y
    elif rand_op == "/":
        res = x / y

    return(res) # -> trả ra ngoài vòng nhưng ko lưu giá trị, ko call ngoài def đc


# call
# res2 = calc(3, 7, "-")
# print(res2) 