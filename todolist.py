import json
import os

FILE_NAME = "todo_list.json"

def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

def display_tasks(tasks):
    if not tasks:
        print("No tasks yet!")
    else:
        for i, task in enumerate(tasks, start=1):
            status = "✓" if task["completed"] else "✗"
            print(f"{i}. [{status}] {task['title']} (Due: {task.get('due', 'N/A')})")

def main():
    tasks = load_tasks()

    while True:
        print("\n1. View Tasks\n2. Add Task\n3. Mark Complete\n4. Delete Task\n5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            title = input("Task title: ")
            due = input("Due date (optional): ")
            tasks.append({"title": title, "due": due, "completed": False})
            save_tasks(tasks)
        elif choice == "3":
            display_tasks(tasks)
            task_num = int(input("Enter task number to mark complete: ")) - 1
            if 0 <= task_num < len(tasks):
                tasks[task_num]["completed"] = True
                save_tasks(tasks)
        elif choice == "4":
            display_tasks(tasks)
            task_num = int(input("Enter task number to delete: ")) - 1
            if 0 <= task_num < len(tasks):
                del tasks[task_num]
                save_tasks(tasks)
        elif choice == "5":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()



