tasks = []


def add_task(task): #parameters
    tasks.append(task)
    print("Task added successfully.")


def view_tasks():
    if tasks:
        print("Tasks:")
        print("========================")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
            """if tasks: check the "tasks" list is not empty.
            enumerate() คือ iterate over a sequence function 
            list, tuple, or string 
            enumerate(collection-name, start=0(optional))
            f-string(formatted string)"""
    else:
        print("========================")
        print("No tasks found.")
    print("========================")

def search_tasks():
    searhch_results = []
    for add_searhchlist in tasks:
        if add_searhchlist.lower().startswith(searhchs.lower()):
            """startswith() มาช่วยเปรียบเทียบจริงเท็จว่า
            add_searhchlist.lower()ขึ้นต้นด้วยsearhchs.lower()ไหมใช่จะทำงาน"""
            searhch_results.append(add_searhchlist)

    if searhch_results:
        print("Tasks starting with the letter", searhchs + ":")
        #+เชื่อมstringให้ติดกันไม่มีเว้นวรรค
        print("========================")
        for index, searhch_results in enumerate(searhch_results, start=1):
            print(f"{index}. {searhch_results}")
            """ Or for result in searhch_results:
            print(result) """
        print("========================")
    else:
        print("No tasks found starting with the letter", searhchs)


def delete_task(task_index): #parameters
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
    print("3. Search Tasks")
    print("4. Delete Task")
    print("5. Quit")
    print("========================\n")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        task = input("Enter task: ")
        add_task(task) #argument
        #Append the task to the tasks list,Is not function to return
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        searhchs = input("Enter an alphabet letter : ")
        search_tasks()
    elif choice == "4":
        task_index = int(input("Enter task index to delete: "))
        delete_task(task_index) #argument
    elif choice == "5":
        print("See you later, Thankyou!!")
        break
    else:
        print("Invalid choice. Please try again.")
