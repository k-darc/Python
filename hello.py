# Asking user for their name
name = input("What is your name? ")

# Remove the whitespace from a string(str)
name = name.strip()

# Capitalize users name
name = name.title()

#Say hello to user
print(f"Hello, {name}")

print(f"Hello, \"{name}\"") # These back slashes show how to use quotes in a format string.

# Use plus operator to concat 2 srtings/arguments, any more and use commas or algorithms.
# Passing multiple args to "print" will add a space after the string. Do "hello," and not "hello, " or use end="" to override the...
#   default value for print.
# Inside parentheses is read first.
