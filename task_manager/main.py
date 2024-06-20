# main.py

from models.task import Task
from data.data_access import load_tasks, save_tasks, add_task


def main():
    while True:
        print("1. Add task")
        print("2. Cancel tasks")
        print("3. View tasks")
        print("4. Mark task as completed")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            task_id = int(input("Enter task ID: "))
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            task = Task(task_id, title, description)
            add_task(task)
        elif choice == "2":
            task_id = int(input("Enter task ID to cancel: "))
            tasks = load_tasks()
            for i in range(len(tasks)):
                if tasks[i].task_id == task_id:
                    tasks.pop(i)
                    print(f"Task {task_id} is cancelled.")
                    break
            else:
                print(f"No task found with ID {task_id}")
            save_tasks(tasks)
            tasks = load_tasks()
            for task in tasks:
                print(task)
        elif choice == "3":
            tasks = load_tasks()
            for task in tasks:
                print(task)
        elif choice == "4":
            task_id = int(input("Enter task ID to mark as completed: "))
            tasks = load_tasks()
            for task in tasks:
                if task.task_id == task_id:
                    task.mark_completed()
                    print(f"Task {task_id} marked as completed.")
                    break
            else:
                print(f"No task found with ID {task_id}")
            save_tasks(tasks)
        elif choice == "5":
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()  