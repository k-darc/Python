def main():
    name = input("What is your name? ")
    print(hello(name))

def hello(to="world"): # the to="" means a default in case the programmer doesn't call hello with an argument
    return f"hello, {to}"

if __name__ == "__main__":
    main()

# Use plus operator to concat 2 srtings/arguments, any more and use commas or algorithms.
# Passing multiple args to "print" will add a space after the string. Do "hello," and not "hello, " or use end="" to override the...
#   default value for print.
# Inside parentheses is read first.
