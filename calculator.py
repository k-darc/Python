x = float(input("What is x? "))
y = float(input("What is y? "))

z = round(x / y, 2)

print(f"{z:.2f}")
# Colon-Comma "print({z:,})" in a format string tells the reader to add a separater. Floats can represent numbers accurately...
#   forever, they have to round as there is not enough memory in a PC.
# "print({"z:.2f"})" specify an f strings, how many digits you want to print.