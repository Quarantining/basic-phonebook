# simple phonebook program

# displays version on title screen
version = "1.6"

selected_password = "123AbC@!_"

# phonebook entries
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


# prints title screen
print(f"""- - - - - - - - - - - - - - - - -
basic phonebook             

"search" --> search entry 
"add" --> add entry
"delete" --> delete entry
"delete all" --> removes all entries
"list" --> lists all entries 
"change password" --> changes password
"stop" --> ends program 
                            v{version}
- - - - - - - - - - - - - - - - -
""")


# searches for key value (name).
def search_name(search):
    print(phonebook.get(search, "entry not found")) # prints entry (if found) otherwise says it cannot locate it.


# doesn't work.
def search_num():
    print("currently unavailable") # this is a work in progress so it's not available yet.


# allows user to add entry. elif to prevent duplicate names.
def add_entries(name, number):
    if name in phonebook:  # checks if new name already exists.
        print(f"{name} already exists in phonebook.")  # tells user their name already exists.
    else:
        phonebook[name] = number  # adds key and value using vars above
        print(f"entry added: {name} --> {number}.")  # prints new entry


# allows user to delete entries.
def delete_entries(name):
    if name in phonebook:
        confirm = input(f"delete {name}? (yes/no): ")  # makes sure user wants to delete name.
        if confirm == "yes":  # "yes" --> deletes.
            del phonebook[name]  # removes name from phonebook.
            print(f"{name} removed.")  # tells user the name was removed.
        elif confirm == "no":  # "no" --> action canceled.
            print(f"{name} was not removed.")
        else:
            print("invalid input.")  # invalid input.


# allows user to list all entries
def list_entries():
    # Calculate the longest name length
    longest_name = max(len(name) for name in phonebook)  # finds longest name
    # Show all entries
    for key, value in phonebook.items():
        # Calculate the number of dots needed
        dot = "." * (longest_name - len(key) + 10)  # calculates the difference
        print(f"{key}{dot}{value}")


def delete_all():
    confirm_delete = input("are you sure? (yes/no): ")
    if confirm_delete == "yes":
        password = input("enter password: ")
        if password == selected_password:
            phonebook.clear()
            print("phonebook cleared")
        else:
            print("Incorrect Password.")

    elif confirm_delete == "no":
        print("process canceled.")
    else:
        print("Invalid Input")


def change_password():
    user_input = input("do you want to change password? (yes/no): ")
    if user_input == "yes":
        change_password = input("change password: ")
        selected_password = change_password
        print(f"password changed to {change_password}")
    elif user_input == "no":
        print("password not changed.")
    else:
        print("Invalid Input.")



while True:
    user_input = input("> ")
    try:
        # search name
        if user_input == "search":

            search_type = input("how do you want to search? (name/number): ")

            # checks for key value (name).
            if search_type == "name":
                search = input(str("enter name --> ")) # prompts user to enter name to search for
                search_name(search)

            # checks for value (number).
            elif search_type == "number":
                search_num()


        # adds entry
        elif user_input == "add":
            name = input("enter new name: ")  # adds key
            number = input("enter new number: ")  # adds value
            add_entries(name, number) # calls function

        # deletes an entry
        elif user_input == "delete":
            name = (input("enter name to delete: ")) # name to remove
            delete_entries(name) # calls function

        # shows all entries
        elif user_input == "list":
            list_entries() # calls function (no argument needed).

        # delete all entries
        elif user_input == "delete all":
            delete_all() # will prompt confirmation and password before clearing.

        # change password
        elif user_input == "change password":
            change_password()


        # stops program
        elif user_input == "stop":
            confirm_stop = input("are you sure? (yes/no): ") # stop confirmation

            if confirm_stop == "yes":
                print("stopping..")
                break # ends program

            elif confirm_stop == "no":
                print("")

            else:
                print("Invalid Input. Please try again.") # if user enters invalid input.

        else:
            print("Invalid Input. Please try again.") # if user enters invalid input.
    # to avoid errors.
    except KeyError:
        print("KeyError")
    except ValueError:
        print("ValueError")





# list of things to add:
    # better error handling.
    # allow for upper/lower inputs.
    # way to edit an existing entry.
    # clear main menu for better interaction.
    # once a mode is selected, loop it until user either completes an action or exist. (this way it wont
    # exit even after you input a invalid value).

    # added clear method (with password).
    # added way to change password.
