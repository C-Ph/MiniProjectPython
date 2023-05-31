tasks = []

def frint():
    print("================")


def add_task(task):
    tasks.append(task)
    print("Task added successfully.")


def view_tasks():
    if tasks:
        print("Tasks:")
        frint()
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
            """if tasks: check the "tasks" list is not empty.
            enumerate() คือ iterate over a sequence function 
            list, tuple, or string 
            enumerate(collection-name, start=0(optional))
            f-string(formatted string)"""
    else:
        frint()
        print("No tasks found.")
    frint()


def delete_task(task_index):
    if task_index >= 1 and task_index <= len(tasks):
        delete = tasks.pop(task_index - 1)
        print(f"Deleted task: {delete}")
        """from index 1 to the length of the list
        1 <= task_index <= len(tasks)
        len() number of items(tasks) 
        is used because list indices are zero-based"""
    else:
        print("Invalid task index.")


# Main program loop
while True:
    print("\n===== Task Manager =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Quit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        task = input("Enter task: ")
        add_task(task)
        #Append the task to the tasks list,Is not function to return
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        task_index = int(input("Enter task index to delete: "))
        delete_task(task_index)
    elif choice == "4":
        print("Exiting Task Manager...")
        break
    else:
        print("Invalid choice. Please try again.")