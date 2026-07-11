
tasks=["Morning walk","Eating Breakfast","Go outside for a long drive"]
def Add_task():
    new_task=input("Write task:")
    tasks.append(new_task)
    print("New task added successfully!")
    
def view_tasks():
    print("__Your tasks__")
    if len(tasks)==0:
        print("No task yet")
    else:
        i=1
        for task in tasks:
            print(i,".",task)
            i=i+1
def delete_task():
    view_tasks()
    if len(tasks)==0:
        return
    try:
        num=int(input("Enter task number to delete:"))
        if num>=1 and num<=len(tasks):
            removed=tasks.pop(num-1)
            print(removed,"deleted successfully!")
        else:
            print("Wrong number")
    except:
        print("Just write numbers")
while True:
    print("1.Add_task")
    print("2.view_tasks")
    print("3.delete_task")
    print("4.Exit")
    choice=input("Choose option:")
    if choice=="1":
        Add_task()
    elif choice=="2":
        view_tasks()
    elif choice=="3":
        delete_task()
    elif choice=="4":
        print("Bye! Have a productive day")
        
        break
                

    
