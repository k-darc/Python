import re

name = input("What's your name? ").strip()
matches = re.search(r"^(.+), (.+)$", name) # the parenthesis are "captured" and then returned as the last name and first name
if matches:
    name = matches.group(2) + " " + matches.group(1)
print(f"hello, {name}")