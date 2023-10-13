def main():
    x = get_int()
    print(f"X is {x}")

def get_int():
    while True:
        try:
            x = int(input("What's x? "))
        except ValueError:
            print("X is not an integer")
        else:
             break
    return x

main()

# If you TRY this code, and there is a ValueError, it'll now show the "not an integer"