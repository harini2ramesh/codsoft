import os

# File to store tasks
FILE_NAME = "to do list.txt"

# Load tasks from the file if it exists
def load_tasks():
    tasks = []
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as f:
            for line in f:
                status, description = line.strip().split(',', 1)
                tasks.append({'description': description, 'status': status})
    return tasks

# Save tasks to the file
def save_tasks(tasks):
    with open(FILE_NAME, 'w') as f:
        for task in tasks:
            f.write(f"{task['status']},{task['description']}\n")

# Add a new task
def add_task(tasks, description):
    task = {
        'description': description,
        'status': 'pending'
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task '{description}' added successfully!")

# Update an existing task
def update_task(tasks, task_id, description):
    if 0 <= task_id < len(tasks):
        tasks[task_id]['description'] = description
        save_tasks(tasks)
        print(f"Task {task_id} updated successfully!")
    else:
        print("Invalid task ID.")

# Delete a task
def delete_task(tasks, task_id):
    if 0 <= task_id < len(tasks):
        deleted_task = tasks.pop(task_id)
        save_tasks(tasks)
        print(f"Task '{deleted_task['description']}' deleted successfully!")
    else:
        print("Invalid task ID.")

# Mark a task as complete
def complete_task(tasks, task_id):
    if 0 <= task_id < len(tasks):
        tasks[task_id]['status'] = 'completed'
        save_tasks(tasks)
        print(f"Task {task_id} marked as complete!")
    else:
        print("Invalid task ID.")

# View all tasks
def view_tasks(tasks):
    if tasks:
        for idx, task in enumerate(tasks):
            status = task['status']
            description = task['description']
            print(f"{idx}. [{status}] {description}")
    else:
        print("No tasks found!")

# Main function to drive the CLI
def main():
    tasks = load_tasks()

    while True:
        print("\nTo-Do List Application")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task as Complete")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            description = input("Enter task description: ").strip()
            add_task(tasks, description)
        elif choice == '3':
            task_id = int(input("Enter task ID to update: "))
            description = input("Enter new task description: ").strip()
            update_task(tasks, task_id, description)
        elif choice == '4':
            task_id = int(input("Enter task ID to delete: "))
            delete_task(tasks, task_id)
        elif choice == '5':
            task_id = int(input("Enter task ID to mark as complete: "))
            complete_task(tasks, task_id)
        elif choice == '6':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
