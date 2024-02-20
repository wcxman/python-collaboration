thelist = {} #A dictionary to store the to-do list in
toleave = False #Setting up a variable to control the terminal loop
print('''Welcome to the list terminal!
      Commands:
          ADD - Adds a new task to the list
          EXIT - Exits the terminal
          VIEW - Shows the current to do list''')
while not toleave:
    cmd = str(input("")).upper() #Gets the user's command and makes it all caps
    if cmd == "ADD": #If the command is ADD
        task = input("Name of task? ")
        thelist.update({task:False}) #Creates a new entry in the dictionary with the task inputted
    elif cmd == "VIEW":
        for x,y in thelist.items(): #For each key in the dictionary
            if y: #If the value at the key is True
                print(x + ": Completed")
            else:
                print(x + ": Incomplete")
    elif cmd == "EXIT":
        toleave = True #Breaks the while loop
    else: 
        print("Command not recognized")