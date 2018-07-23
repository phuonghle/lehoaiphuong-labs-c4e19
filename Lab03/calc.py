
x = int(input("x = "))
op = input("Operation(+, -, *, /): ")
y = int(input("y = "))

print("* " * 20)

res = 0

if op == "+":
    res = x + y
elif op == "-":
    res = x - y
elif op == "*":
    res = x * y
elif op == "/":
    res = x / y
else:
    print("Buzz")
    break

# nên rút print ra ngoài
print("{0} {1} {2} = {3}".format(x, op, y, res))





# def calc


