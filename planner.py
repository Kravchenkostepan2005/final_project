def interface():
    print("""
    1 - add new note
    2 - show all notes
    3 - change the note
    4 - delete the note
    5 - break
    """)
    k = input("choice number: ")
    return k


def answering(k):
    if k == "1":
        add_new_note()
    if k == "2":
        show_all_notes()
    if k == "3":
        change_note()
    if k == "4":
        delete_note()
    if k == "5":
        print("Thanks, bye")
        exit()


def save(note):
    with open("1.txt", "a+") as f:
        f.write(note)
        f.write("\n")


def add_new_note():
    b = input("Enter the name of the file: ")
    with open(b, "a+") as f:
        a = input("Add new note: ")
        f.write(a + "\n")


def show_all_notes():
    with open("1.txt") as f:
        all_notes = f.readlines()
        for i in all_notes:
            print(i)


def change_note():
    g = input("Enter the file to change the note in: ")
    with open(g + ".txt", "w+") as f:
        f.readlines()
        k = input("if you want to delete a note - press d, if you want to add it - press a: ")
        if k == "d":
            delete_note()
        elif k == "a":
            add_new_note()


def delete_note():
    g = input("Enter the file to delete the note in: ")
    with open(g + ".txt", "r+") as f:
        lines = f.readlines()
    with open(g + ".txt", "w+") as f:
        h = input("Enter the note to delete: ")
        for line in lines:
            if line != "nickname_to_delete" + "\n":
                f.write(line)


delete_note()


def main():
    choice = interface()
    answering(choice)
