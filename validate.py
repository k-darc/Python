import re

email = input("What your email? ").strip()

if re.search("@", email):
    print("Valid")
else:
    print("INVALID!")