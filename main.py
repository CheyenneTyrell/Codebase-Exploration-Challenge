from task_manager import TaskManager
from storage import save_tasks, load_tasks
from export_utils import export_to_csv


def menu():
    print("\n--- TASK MANAGER ---")
    print("1. Create Task")
    print("2. View Tasks")
    print("3. Update Status")
    print("4. Delete Task")
    print("5. Run Overdue Check")
    print("6. Export CSV")
    print("0. Exit")


def main():
    tm = TaskManager()
    tm.tasks = load_tasks()
    tm.next_id = len(tm.tasks) + 1

    while True:
        menu()
        choice = input("Select option: ")

        if choice == "1":
            title = input("Title: ")
            desc = input("Description: ")
            priority = input("Priority (LOW/MEDIUM/HIGH): ")
            due = input("Due date (YYYY-MM-DD): ") + "T00:00:00"

            tm.create_task(title, desc, priority, due)
            save_tasks(tm.tasks)

        elif choice == "2":
            for t in tm.get_tasks():
                print(vars(t))

        elif choice == "3":
            tid = int(input("Task ID: "))
            status = input("New status (TODO/IN_PROGRESS/DONE): ")
            tm.update_status(tid, status)
            save_tasks(tm.tasks)

        elif choice == "4":
            tid = int(input("Task ID: "))
            tm.delete_task(tid)
            save_tasks(tm.tasks)

        elif choice == "5":
            tm.update_overdue_tasks()
            save_tasks(tm.tasks)

        elif choice == "6":
            export_to_csv(tm.tasks)
            print("Exported to CSV!")

        elif choice == "0":
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()