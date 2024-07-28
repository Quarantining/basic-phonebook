# simple phonebook program

# displays version on title screen
version = "1.4"

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

"search" --> search entry 
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
    try:
        # search name
        if user_input == "search":
            search_type = input("how do you want to search? (name/number): ")
            
            if search_type == "name":
                search = input(str("enter name --> ")) # prompts user to enter name to search for
                print(phonebook.get(search, "entry not found")) # prints entry if found

        # adds entry
        elif user_input == "add":
            name = input("enter new name: ") # adds key
            number = input("enter new number: ") # adds value
            if name in phonebook: # checks if new name already exists.
                print(f"{name} already exists in phonebook.") # tells user their name already exists.
            else:
                phonebook[name] = number # adds key and value using vars above
                print(f"entry added: {name} --> {number}.") # prints new entry

        # deletes an entry
        elif user_input == "delete":
           name = (input("enter name to delete: ")) # name to remove
           if name in phonebook:
               confirm = input(f"delete {name}? (yes/no): ") # makes sure user wants to delete name.
               if confirm == "yes": # "yes" --> deletes
                   del phonebook[name] # removes name from phonebook
                   print(f"{name} removed.") # tells user name was removed
               elif confirm == "no": # "no" --> action cancled.
                   print(f"{name} was not removed.")
               else:
                   print("invalid input.") # invalid input

        # shows all entries
        elif user_input == "list":
            # Calculate the longest name length
            longest_name = max(len(name) for name in phonebook) # finds longest name
            # Show all entries
            for key, value in phonebook.items():
                # Calculate the number of dots needed
                dot = "." * (longest_name - len(key) + 10) # calculates the difference
                print(f"{key}{dot}{value}")

        # stops program
        elif user_input == "stop":
            confirm_stop = input("are you sure? (yes/no): ")
            if confirm_stop == "yes":
                print("stopping..")
                break
            elif confirm_stop == "no":
                print("")
            else:
                print("Invalid Input. Please try again.")
        else:
            print("Invalid Input. Please try again.")
    except KeyError:
        print("KeyError")
    except ValueError:
        print("ValueError")
