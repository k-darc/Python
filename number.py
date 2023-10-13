try:
    x = int(input("What's x? "))
except ValueError:
    print("X is not an integer")

print(f"x is {x}")

# Order of Operations error - the input is passing the string to the int function as its argument, the int function is the error