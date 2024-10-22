class Task:
    def __init__(self, description, due_date=None):
        self.description = description
        self.due_date = due_date
        self.completed = False

    def mark_complete(self):
        self.completed = True

    def update_task(self, new_description, new_due_date=None):
        self.description = new_description
        self.due_date = new_due_date
def add_task(tasks):
    description = input("Enter task description: ")
    due_date = input("Enter due date (optional): ")
    tasks.append(Task(description, due_date))
    print("Task added!")
def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    for i, task in enumerate(tasks, 1):
        status = "Completed" if task.completed else "Pending"
        due = f" (Due: {task.due_date})" if task.due_date else ""
        print(f"{i}. {task.description}{due} - {status}")
def update_task(tasks):
    view_tasks(tasks)
    task_index = int(input("Enter the task number to update: ")) - 1
    if 0 <= task_index < len(tasks):
        new_description = input("Enter new description: ")
        new_due_date = input("Enter new due date (optional): ")
        tasks[task_index].update_task(new_description, new_due_date)
        print("Task updated!")
    else:
        print("Invalid task number.")
def mark_complete(tasks):
    view_tasks(tasks)
    task_index = int(input("Enter the task number to mark as complete: ")) - 1
    if 0 <= task_index < len(tasks):
        tasks[task_index].mark_complete()
        print("Task marked as complete!")
    else:
        print("Invalid task number.")
def remove_task(tasks):
    view_tasks(tasks)
    task_index = int(input("Enter the task number to remove: ")) - 1
    if 0 <= task_index < len(tasks):
        del tasks[task_index]
        print("Task removed!")
    else:
        print("Invalid task number.")
def main():
    tasks = []
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Mark Task as Complete")
        print("5. Remove Task")
        print("6. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            update_task(tasks)
        elif choice == '4':
            mark_complete(tasks)
        elif choice == '5':
            remove_task(tasks)
        elif choice == '6':
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
