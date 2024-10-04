import json


# Function to load tasks from a file
def load_tasks(filename):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []


# Function to save tasks to a file
def save_tasks(filename, tasks):
    with open(filename, 'w') as f:
        json.dump(tasks, f, indent=4)


# Function to display tasks
def display_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return
    for idx, task in enumerate(tasks, 1):
        status = "Completed" if task['completed'] else "Pending"
        print(f"{idx}. {task['description']} (Priority: {task['priority']}) - {status}")


# Function to add a new task
def add_task(tasks):
    description = input("Enter task description: ")
    priority = input("Enter task priority (low, medium, high): ").lower()
    tasks.append({"description": description, "priority": priority, "completed": False})


# Function to mark task as completed
def complete_task(tasks):
    task_num = int(input("Enter task number to mark as completed: "))
    if 1 <= task_num <= len(tasks):
        tasks[task_num - 1]['completed'] = True
    else:
        print("Invalid task number!")


# Function to remove a task
def remove_task(tasks):
    task_num = int(input("Enter task number to remove: "))
    if 1 <= task_num <= len(tasks):
        tasks.pop(task_num - 1)
    else:
        print("Invalid task number!")


# Main function
def main():
    filename = 'tasks.json'
    tasks = load_tasks(filename)

    while True:
        print("\nTo-Do List")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Remove Task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            complete_task(tasks)
        elif choice == '4':
            remove_task(tasks)
        elif choice == '5':
            save_tasks(filename, tasks)
            print("Tasks saved. Exiting...")
            break
        else:
            print("Invalid option. Try again.")


if __name__ == '__main__':
    main()
