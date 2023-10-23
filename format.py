import re

name = input("What's your name? ").strip()
if matches := re.search(r"^(.+), *(.+)$", name): # the parenthesis are "captured" and then returned as the last name and first name
    name = matches.group(2) + " " + matches.group(1)
print(f"hello, {name}")