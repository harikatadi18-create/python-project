print("Welcome to To-Do List Application!!")
#list to store tasks
tasks=[]

def load_tasks():
    try:
        with open("tasks.txt","r") as file:
            for line in file:
                task, status= line.strip().split("|")
                tasks.append({"task":task, "status":status})
    except FileNotFoundError:
        pass

def save_tasks():
    with open("tasks.txt","w") as file:
        for task in tasks:
            file.write(task["task"]+ "|" + task["status"] + "\n")

#functions to display menu
def show_menu():
    print("welcome to To-Do List Application")
    print("\n....Menu.........")
    print("1.Add tasks")
    print("2.view tasks")
    print("3.Mark task as completed")
    print("4.Delete task")
    print("5.Exit")

load_tasks()

while True:
    show_menu()
    choice=input("Enter your choice: ")
    if choice == "1":
        task=input("enter new task: ")
        tasks.append({"task":task, "status":"Pending"})
        save_tasks()
        print("Task added successfully!!")
    elif choice == "2":
        if not tasks:
            print("No tasks available")
        else:
            print("\n your tasks")
            for index, task in enumerate(tasks,start=1):
                print(f"{index}.{task['task']} [{task['status']}]")
                save_tasks()
    elif choice == "3":
        if not tasks:
            print("No tasks available")
        else:
            for index, task in enumerate(tasks,start=1):
                print(f"{index}.{task['task']} [{task['status']}]")
            try:
                task_number=int(input("Enter task number to mark as completed: "))
                if 1<= task_number <= len(tasks):
                    tasks[task_number - 1]["status"] = "completed"
                    save_tasks()
                    print("task mark as completed!")
                else:
                    print("invalid task number. ")
            except ValueError:
                print("please enter a valid number")
    elif choice == "4":
        if not tasks:
            print("No tasks available")
        else:
            for index, task in enumerate(tasks,start=1):
                print(f"{index}.{task['task']} [{task['status']}]")
            try:
                task_number=int(input("Enter task number to mark as completed: "))
                if 1<= task_number <= len(tasks):
                    removed_task=tasks.pop(task_number - 1)
                    save_tasks()
                    print(f"task '{removed_task['task']}' deleted successfully!!")
                else:
                    print("invalid task number. ")
            except ValueError:
                print("please enter a valid number")
        print("delete task selected")
    elif choice == "5":
        save_tasks()
        print("exit from program!!")
        break
    else:
        print("Invalid choice!")