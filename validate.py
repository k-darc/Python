email = input("What your email? ").strip()

if "@" in email:
    print("Valid")
else:
    print("Invalid")