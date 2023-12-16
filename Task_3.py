def show_menu():
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task as done")
    print("4. Quit")

def add_task(tasks, new_task):
    tasks.append(new_task)
    print("Task added!")
    print()

def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        print()
    else:
        print("Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
        print()

def mark_task_done(tasks, task_index):
    if 1 <= task_index <= len(tasks):
        print(f"Marking task '{tasks[task_index - 1]}' as done.")
        del tasks[task_index - 1]
        print()
    else:
        print("Invalid task index.")
        print()

def main():
    tasks = []
    while True:
        show_menu()
        print()
        choice = input("Enter your choice: ")

        if choice == "1":
            new_task = input("Enter the task: ")
            add_task(tasks, new_task)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            task_index = int(input("Enter the task number to mark as done: "))
            mark_task_done(tasks, task_index)
        elif choice == "4":
            print("Quitting the Task-3.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()