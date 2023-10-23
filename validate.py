import re

email = input("What your email? ").strip()

if re.search(r"^[a-zA-Z0-9_]+@[^@]+\.edu$", email):
    print("Valid")
else:
    print("INVALID!")