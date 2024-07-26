# user should be able to enter a name and get returned a phone number.
# user can delete existing entries in the phone book.
# user can add new entries into the phone book.
# user can list all entries in the phone book.

version = "1.0"

# entries
phonebook = {
    "Bob": 123,
    "Five": 456
}

# title screen
print(f"""- - - - - - - - - - - - - - - - -
basic phonebook             

"search" --> search by name 
"add" --> add entry
"delete" --> delete entry
"list" --> lists all entries 
"stop" --> ends program 
                            v{version}
- - - - - - - - - - - - - - - - -
""")

while True:
    # user selection
    user_input = input("> ")

    # search name
    if user_input == "search":
        search = input(str("enter name --> "))
        print(phonebook.get(search, "entry not found"))

    # adds entry
    elif user_input == "add":
        name = input("enter new name: ")
        number = input("enter new number: ")
        phonebook[name] = number
        print(f"entry added: {name} --> {number}.")

    # deletes an entry
    elif user_input == "delete":
       name = (input("enter name to delete: "))
       del phonebook[name]
       print(f"{name} removed.")

    # shows all entries
    elif user_input == "list":
        print(phonebook)

    # stops program
    elif user_input == "stop":
        break
    else:
        print("Invalid Input. Please try again.")
