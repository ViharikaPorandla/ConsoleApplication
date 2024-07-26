if __name__ == "__main__":
    while True:
        print("\nTask Manager")
        print("1. Create Task")
        print("2. Display Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            task_id = int(input("Enter task ID: "))
            name = input("Enter task name: ")
            description = input("Enter task description: ")
            create_task(task_id, name, description)
        elif choice == '2':
            display_tasks()
        elif choice == '3':
            task_id = int(input("Enter task ID to update: "))
            name = input("Enter new task name (leave blank to skip): ")
            description = input("Enter new task description (leave blank to skip): ")
            status = input("Enter new task status (leave blank to skip): ")
            update_task(task_id, name or None, description or None, status or None)
        elif choice == '4':
            task_id = int(input("Enter task ID to delete: "))
            delete_task(task_id)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")
