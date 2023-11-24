from colorama import Fore, Back, Style
class ToDoList:
    def __init__(self, cursor, list_name) -> None:
        self.task_details = {} # task_id: task_name pair
        # self.task_completed = {} # When completed it remove task from task details add it to task completed
        self.cursor = cursor
        self.list_name = list_name
        self.cursor.execute(f"CREATE TABLE {self.list_name} (name TEXT)")

    def add_task(self, task_name):
        self.cursor.execute(f"INSERT INTO {self.list_name} VALUES ('{task_name}')")
        print("Task added Successfully")

    def delete_task(self, task_name):
        # Deleting a particular key from the dictionary
        all_names = self.cursor.execute(f"SELECT * FROM {self.list_name}").fetchall()[0]
        print(all_names)
        if task_name not in all_names:
            print(Fore.YELLOW + "No Such task found")
            return
        # del self.task_details[task_id]
        self.cursor.execute(f"DELETE FROM {self.list_name} WHERE name={task_name};")
        print(Fore.YELLOW + "Task deleted Successfully")

    def list_task(self):
        rows = list(self.cursor.execute(f"SELECT * FROM {self.list_name}").fetchall())
        print(Fore.LIGHTGREEN_EX + "Task details")
        for row in rows:
            print(Fore.GREEN + f"Task: {row[0]}")