todo_list = []

while True:
    print("\n--- TO-DO LIST ---")
    print("1. Add a new task")
    print("2. View all tasks")
    print("3. Remove a task")
    print("4. Exit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        task = input("Enter a new task: ")
        todo_list.append(task)
        print("Task added.")

    elif choice == '2':
        if len(todo_list) == 0:
            print("No tasks in the list.")
        else:
            print("\nYour Tasks:")
            i = 0
            while i < len(todo_list):
                print(str(i + 1) + ". " + todo_list[i])
                i += 1

    elif choice == '3':
        if len(todo_list) == 0:
            print("No tasks to remove.")
        else:
            i = 0
            while i < len(todo_list):
                print(str(i + 1) + ". " + todo_list[i])
                i += 1
            try:
                task_num = int(input("Enter the task number to remove: "))
                if task_num >= 1 and task_num <= len(todo_list):
                    removed = todo_list.pop(task_num - 1)
                    print("Task '" + removed + "' removed.")
                else:
                    print("Invalid task number.")
            except:
                print("Please enter a valid number.")

    elif choice == '4':
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
