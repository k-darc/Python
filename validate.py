import re # Regular expression import (RegEx)

email = input("What your email? ").strip()

if re.search(r"^\w|\.+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE): #\w = a-z and A-Z and 0-9 and _
    print("Valid")
else:
    print("INVALID!")
