def main():
    x = int(input("What is x?")
    print("x squared is", square(x))

def square(n):
    return n * n

main()

# Colon-Comma "print({z:,})" in a format string tells the reader to add a separater. Floats can represent numbers accurately...
#   forever, they have to round as there is not enough memory in a PC.
# "print({"z:.2f"})" specify an f strings, how many digits you want to print.