def interface():
    print(""" 
    1 - add new note 
    2 - show all notes 
    3 - change the note 
    4 - delete the note 
    5 - break 
    """)
    choice = input("choice number: ")
    return choice


def answering(choice):
    if choice == "1":
        add_new_note()
    if choice == "2":
        show_all_notes()
    if choice == "3":
        change_note()
    if choice == "4":
        delete_note()
    if choice == "5":
        print("Thanks, bye")
        exit()


def save(note):
    name = input("Enter the name of the file: ")
    with open(name, "a+") as f:
        f.write(note)
        f.write("\n")


def add_new_note():
    name = input("Enter the name of the file: ")
    with open(name, "a+") as f:
        new = input("Add new note: ")
        f.write(new + "\n")


def show_all_notes():
    filename = input("Enter the name of the file: ")
    with open(filename, "r+") as f:
        all_notes = f.readlines()
        for i in all_notes:
            print(i)


def change_note():
    file = input("Enter the file to change the note in: ")
    with open(file, "w+") as f:
        f.readlines()
        k = input("if you want to delete a note - press d, if you want to add it - press a: ")
        if k == "d":
            delete_note()
        elif k == "a":
            add_new_note()


def delete_note():
    deleting = input("Enter the file to delete the note in: ")
    with open(deleting, "r") as f:
        lines = f.readlines()
        print(lines)

    with open(g, "w") as f:
        note_to_delete = input("Enter the note to delete: ")
        print(f'h /{note_to_delete}/')
        for line in lines:
            print(f'line /{line[:-1]}/, h /{note_to_delete}/')
            if line[:-1] != note_to_delete:
                f.write(line)


def main():
    choice = interface()
    answering(choice)


while True:
    main()
