try:
    x = int(input("What's x? "))
    print(f"x is {x}")
except ValueError:
    print("X is not an integer")