from colorama import Fore, Back, Style
class ToDoList:
    def __init__(self) -> None:
        self.task_details = {} # task_id: task_name pair
        # self.task_completed = {} # When completed it remove task from task details add it to task completed

    def add_task(self, task):
        key = len(self.task_details)
        self.task_details[key+1] = task
        print("Task added Successfully")

    def delete_task(self, task_id):
        # Deleting a particular key from the dictionary
        if task_id not in self.task_details.keys():
            print(Fore.YELLOW + "No Such task found")
            return
        del self.task_details[task_id]
        print(Fore.YELLOW + "Task deleted Successfully")

    def list_task(self):
        print(Fore.LIGHTGREEN_EX + "Task details")
        for i, task in self.task_details.items():
            print(Fore.GREEN + f"{i}. Title: {task}")