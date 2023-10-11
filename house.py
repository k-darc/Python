name = input("What's your name? ")

match name:
    case "Harry" | "Hermione" | "Ron": # the bar | acts as an or
        print("Gryffindor")
    case "Draco":
        print("Slytherine")
    case _:
        print("Who?")
