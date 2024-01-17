from datetime import datetime

TASKS_FILE = 'tasks.txt'

def load_tasks():
    try:
        with open(TASKS_FILE, 'r') as file:
            tasks = [line.strip().split('|') for line in file]
    except FileNotFoundError:
        tasks = []
    return tasks

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        for task in tasks:
            file.write(f'{task[0]} | {task[1]} | {task[2]}\n')

def add_task():
    description = input('Enter task description: ')
    due_date = input('Enter due date (YYYY-MM-DD, press Enter if none): ')
    
    tasks = load_tasks()
    new_task = [False, description, due_date]
    tasks.append(new_task)
    save_tasks(tasks)
    print(f'Task "{description}" added successfully.')

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print('No tasks found.')
    else:
        print("Tasks:")
        for idx, task in enumerate(tasks, start=1):
            status = "Completed" if task[0] == 'True' else "Pending"
            due_date = f', Due: {task[2]}' if task[2] else ''
            print(f'{idx}. [{status}] {task[1]}{due_date}')

def main():
    print("Simple Command Line Task Manager")

    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            add_task()
        elif choice == '2':
            list_tasks()
        elif choice == '3':
            print("Exiting Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
