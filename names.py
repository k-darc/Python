name = input("What's your name? ")

with open("names.txt", "a") as file:
    file.write(f"{name}\n")



# each name entered on run will exist in names.txt. "Code names.txt" to see what you have added "rm names.txt" to delete the file.
# "file = open("names.txt", "w")" the W means write, but it opens the file and recreates it with brand new content, and does not append.
#    use A to rewrite and append.