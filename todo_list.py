thelist = {} #A dictionary to store the to-do list in
toleave = False #Setting up a variable to control the terminal loop
print('''Welcome to the list terminal!
     Commands:
         ADD - Adds a new task to the list
         EXIT - Exits the terminal
         VIEW - Shows the current to do list
         COMPLETE - Completes a task
         REMOVE - Removes a task''')
while not toleave:
    cmd = str(input("")).upper() #Gets the user's command and makes it all caps
    if cmd == "ADD": #If the command is ADD
        task = input("Name of task? ")
        thelist.update({task:False}) #Creates a new entry in the dictionary with the task inputted
        print("Task successfully added.")
    elif cmd == "VIEW":
        for x,y in thelist.items(): #For each key in the dictionary
            if y: #If the value at the key is True
                print(x + ": Completed")
            else:
                print(x + ": Incomplete")
    elif cmd == "COMPLETE":
        task = input("Name of task? ")
        if task in thelist: #If the named task is found in the dictionary
            thelist[task] = True #Set the task's status to true
            print("Successfully completed.")
        else:
            print("Unrecognized task")
    elif cmd == "REMOVE":
        task = input("Name of task? ")
        if task in thelist: #If the named task is in the dictionary
            del thelist[task] #Removes the task from the dictionary
            print("The task was successfully removed")
        else:
            print("Unrecognized task")
    elif cmd == "CLEAN":
        newlist = thelist.copy() #Creates a new list that's a copy of the original
        for i in thelist.keys(): #For each key in the list
            if thelist[i] == True: #If the key has a True value
                del newlist[i] #Deletes the key from the copied list
        thelist = newlist #Sets the main list to the copied one, with items deleted if applicable
    elif cmd == "EXIT":
        toleave = True #Breaks the while loop
    else: 
        print("Command not recognized")