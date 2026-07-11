def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    if y==0:
        return "Error! Cannot divided by 0"
    return x/y
while True:
    print("=== CALCULATOR===") 
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("5.Exit")
    choice=input("Enter chioce 1/2/3/4/5:")
    if choice=='5':
        print("Thankyou for using calculater")
        break
    try:
        num_1=float(input("Enter first number:"))
        num_2=float(input("Enter second number:"))

        if choice=='1':
            print("Result",add(num_1,num_2))
        elif choice=='2':
            print("Result",subtract(num_1,num_2))
        elif choice =='3':
            print("Result",multiply(num_1,num_2))
        elif choice=='4':
            print("Result",divide(num_1,num_2))
        else:
            print("Invalid choice!Enter a number from 1 to 5")
    except:
            print("Error!Just write numbers")
print("Calculator closed!")