import sqlite3
from task import ToDoList
from colorama import Fore

connection = sqlite3.connect("todo.db")

cursor = connection.cursor()

todo = ToDoList(cursor=cursor, list_name="demo")

while True:
    # print options for user
    print(Fore.WHITE,"\nTodo List Menu:")
    print(Fore.BLUE, "1. Add Task")
    print(Fore.BLUE, "2. List Tasks")
    print(Fore.BLUE, "3. Mark Task as Completed")
    print(Fore.BLUE, "4. Quit")
    
    usr_input = int(input(Fore.RED + "Enter your choice:"))

    if usr_input == 1:
        # If input is 1, call the corressponding function
        task_input = input(Fore.RED + "Enter the task name:")
        todo.add_task(task_input)
    
    elif usr_input == 2:
        # If input is 2, list all tasks in the list
        todo.list_task()

    elif usr_input == 3:
        # If input is 3, first show all current tasks
        # then take input and delete the required task
        todo.list_task()
        i = input(Fore.RED + "Enter task name:")
        todo.delete_task(i)

    elif usr_input == 4:
        # Break out of the code if input is 4
        break