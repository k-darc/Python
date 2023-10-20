names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"hello, {name}")

# each name entered on run will exist in names.txt. "Code names.txt" to see what you have added "rm names.txt" to delete the file.
# "file = open("names.txt", "w")" the W means write, but it opens the file and recreates it with brand new content, and does not append.
#    use A to rewrite and append.

# with open("names.txt") you do not need the "r" here, as when opening a file to read it, R is the default to read and not write.