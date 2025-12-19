tasks = [] #Creating a var, type array.

def addTask(): #Defining a function that handles adding a new task.
    print("\n") #Prints out a new empty line.
    task = input("Enter a new task: ") #Gets the user's input. Task's title.
    tasks.append(task) #Adds the new task at the end of the array.
    print(f"'{task}' has been added to the task list.") #Prints out a confirmation that the new task is added.

def listTasks(): #Defining a function that handles listing all tasks.
    print("\n") #Prints out a new empty line.
    if tasks: #Checks if the array is populated. If it is, then...
        print("Current tasks: ") #Prints out a header.
        print("---------------") #Prints out a decorative element for the header.
        for index, task in enumerate(tasks): #A for loop that utilizes the enumerate() function to loop over the array while keeping track of the index.
            print(f"#{index + 1} {task}") #Prints out every value (task) in the array and it's index. There is an increase of the index by one, it helps out with the visual numeration.
    else: #But, if the array is empty.
        print("There are no tasks currently.") #Prints out a message that there are no tasks, yet.
        print("-----------------------------") #Prints out a decorative element for the header.

def removeTask(): #Defining a function that handles removing a task.
    print("\n") #Prints out a new empty line.
    try: #Opening a try-except block to handle input and catch any invalid attempts.
        taskToDelete = int(input("Enter the # to delete: ")) #Gets the user's input. Task's number.
        if taskToDelete >= 0 and taskToDelete <= len(tasks): #If statement that checks if the given input is in range of 0 and the length of the array.
            tasks.pop(taskToDelete - 1) #Removes the element by its index with the .pop() method. There is a decrease of the index by one because of the visual numeration.
            print(f"Task #{taskToDelete} has been removed.") #Prints out the number of the task that has been deleted.
        else: #If the user's input is too high or too low...
            print(f"Task #{taskToDelete} does not exist.") #Prints out an invalid input message.
    except: #If the user's input cannot be transformed into an int, then...
        print("Invalid input.") #Prints out an invalid input message.

if __name__ == "__main__": #Checks if the script is being run directly, rather than being imported.
    print("\n") #Prints out a new empty line.
    while True: #A while loop that runs forever unless it's manually stopped.
        print("\n") #Prints out a new empty line.
        listTasks() #Calls out function listTasks().
        print("\n") #Prints out a new empty line.
        print("1. Add a new task") #Prints out option 1.
        print("2. Delete a task") #Prints out option 2.
        print("3. Quit") #Prints out option 3.

        choice = input("Enter your choice: ") #Gets the user's input. Option's number.

        if choice == "1": #If the input is "1".
            addTask() #Calls out function addTask().
        elif choice == "2": #If the input is "2".
            removeTask() #Calls out function removeTask().
        elif choice == "3": #If the input is "3".
            break #Breaks out of the while loop, quits the app.
        else: #Cheks for invalid user input.
            print("Invalid input. Please try again.") #Prints out an invalid input message.
    print("\n") #Prints out a new empty line.
    print("Goodbye.") #Prints out a goodbye message.