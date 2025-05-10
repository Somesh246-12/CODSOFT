#Task-1 --> To-do-list

def task():
    tasks=[]
    print("---WELCOME---")

    total_task=int(input("How many tasks you want to add:"))
    for i in range(1,total_task+1):
        task_name=input(f"Enter task {i} = ").lower()
        tasks.append(task_name)

    print(f"Today's tasks are:\n{tasks}")

    while True:
        operation = int(input("\n1-Add\n2-Update\n3-Delete\n4-view\n5-Exit/stop\nWhat do you want to do? "))

        if operation == 1:
            add = input("Enter the task you want to add:").lower()
            tasks.append(add)
            print(f"Task {add} has been added successfully...")
        elif operation == 2:
            updated_value=input("Enter the task name you want to update:").lower()
            if updated_value in tasks:
                up=input("Enter new task:").lower()
                ind=tasks.index(updated_value)
                tasks[ind]=up
                print(f"Updated task is {up}")  

            else:
                print("Task not found..")

        elif operation == 3:
            del_value=input("Which task you want to delete?:")
            if del_value in tasks:
                ind=tasks.index(del_value)
                del tasks[ind]
                print(f"Task {del_value} has been deleted successfully...")

            else:
                print("Task not found..")

        elif operation == 4:
            print(f"Total tasks = {tasks}")

        elif operation == 5:
            print("Closing the program...")
            print("THANKYOU")
            break
        else:
            print("Invalid input")                      
task()      