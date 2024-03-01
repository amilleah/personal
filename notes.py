import os

ROOT = '/Users/amilleahrodriguez/notes/'

def open_notebook():
    name = str(input("enter a name for your note: "))
    file_name = ROOT + name + ".txt"

    while os.path.exists(file_name):
        choice = input("that already exists. do you want to (e)dit or (c)reate a new file? ").lower()
        if choice == 'e':
            with open(file_name, 'a') as file:
                str(text_input = input("start writing: "))
                file.write("\n" + text_input)
            print("noted! saved to " + name + ".txt")
            return
        elif choice == 'c':
            name = str(input("enter a name for your note: "))
            file_name = ROOT + name + ".txt"
        else:
            print("sorry! please enter 'e' to edit or 'c' to create a new file.")
            continue

    with open(file_name, 'w') as file:
        text_input = str(input("start writing: "))
        file.write(text_input)

    print("noted! saved to " + name + ".txt")

open_notebook()
