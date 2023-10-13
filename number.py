while True:
    try:
        x = int(input("What's x? "))
        break
    except ValueError:
        print("X is not an integer")

print(f"X is {x}")

# Order of Operations error - the input is passing the string to the int function as its argument, the int function is the error.
# If you TRY this code, and there is a ValueError, it'll now show the "not an integer"