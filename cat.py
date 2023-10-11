def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What is N? "))
        if n > 0:
            return n

def meow(n):
    for _ in range(n):
        print("meow")

main()

# underscores are used for variables that you immediately call, no need to name them.
