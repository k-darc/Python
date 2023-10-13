def main():
    x = get_int("What's x? ")
    print(f"X is {x}")


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass

main()

# If you TRY this code, and there is a ValueError, it'll now show the "not an integer"