todo_list = []

def show_tasks():
    if not todo_list:
        print("No tasks in the list")
    else:
        for i, task in enumerate(todo_list, start=1):
            print(i, task)

while True:
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Show Tasks")
    print("4. Exit")
    choice = input("Choose an option (1-4):")

    if choice == '1':
        task = input("Enter task: ")
        todo_list.append(task)
        print("Task added")
    elif choice == '2':
        show_tasks()
        try:
            index = int(input("Enter task number to remove:"))
            if 1 <= index <= len(todo_list):
                removed = todo_list.pop(index-1)
                print("Removed:", removed)
            else:
                print("Invalid task number")
        except ValueError:
            print("Enter a valid number")
    elif choice == '3':
        show_tasks()
    elif choice == '4':
        print("Exiting To-Do List")
        break
    else:
        print("Invalid choice")
