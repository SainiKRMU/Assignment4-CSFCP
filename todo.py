tasks = []

def show_menu():
    print("\n===== TO-DO LIST MENU =====")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Enter your choice (1-4): ")

    try:
        if choice == "1":
            task = input("Enter a new task: ")
            if task.strip() == "":
                print("Task cannot be empty!")
            else:
                tasks.append(task)
                print("Task added!")

        elif choice == "2":
            print("\nYour Tasks:")
            if not tasks:
                print("No tasks found.")
            else:
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task}")

        elif choice == "3":
            if not tasks:
                print("No tasks to remove.")
                continue
            print("\nSelect a task to remove:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
            try:
                remove_index = int(input("Task number: "))
                tasks.pop(remove_index - 1)
                print("Task removed!")
            except (ValueError, IndexError):
                print("Invalid input. Enter a valid task number.")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Enter 1–4.")
    except Exception as e:
        print("An unexpected error occurred:", e)
