import re

name = input("What's your name? ").strip()
matches = re.search(r"^(.+), (.+)$", name) # the parenthesis are "captured" and then returned as the last name and first name
if matches:
    last = matches.group(1)
    first = matches.group(2)
    name = f"{first} last"
print(f"hello, {name}")