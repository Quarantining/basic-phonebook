# user should be able to enter a name and get returned a phone number.
# user can delete existing entries in the phone book.
# user can add new entries into the phone book.
# user can list all entries in the phone book.

# list of things to add:
    # more default phonebook entries (done)
    # more descriptive comments
    # error handling
    # when deleting an entry, show the phone number. Ex) "Removed Bob "123""
    # actually remember to update the version number


# displays version on title screen
version = "1.1"

# entries
phonebook = {
    "Yuki Tanaka": "555-1234",
    "Minji Kim": "555-5678",
    "John Smith": "555-8765",
    "Priya Sharma": "555-4321",
    "Marie Dubois": "555-9876",
    "Hans Müller": "555-6789",
    "Lucas Silva": "555-3456",
    "Wei Zhang": "555-7890",
    "Amina Adamu": "555-2468",
    "Ivan Petrov": "555-1357"
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
        search = input(str("enter name --> ")) # prompts user to enter name to search for
        print(phonebook.get(search, "entry not found")) # prints entry if found

    # adds entry
    elif user_input == "add":
        name = input("enter new name: ") # adds key
        number = input("enter new number: ") # adds value
        phonebook[name] = number # adds key and value using vars above
        print(f"entry added: {name} --> {number}.") # prints new entry

    # deletes an entry
    elif user_input == "delete":
       name = (input("enter name to delete: ")) # name to remove
       del phonebook[name] # removes name from phonebook
       print(f"{name} removed.") # tells user name was removed

    # shows all entries
    elif user_input == "list":
        print(phonebook)

    # stops program
    elif user_input == "stop":
        break
    else:
        print("Invalid Input. Please try again.")
