op = input("Pick Operation: ")
x = input("First number: ")
y = input("Second number: ")

if op == "add":
    print(int(x) + int(y))
elif op == "mult":
    print(int(x) * int(y))
elif op == "sub":
    print(int(x) - int(y))
elif op == "div":
    print(int(x) / int(y))