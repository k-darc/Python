import re

email = input("What your email? ").strip()

if re.search(r".+@.+\.edu", email):
    print("Valid")
else:
    print("INVALID!")