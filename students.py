with open("students.csv") as file:
    for line in file:
        line.rstrip().split(",")