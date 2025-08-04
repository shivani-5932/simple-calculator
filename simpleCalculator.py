def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
def userinput():
    list=["Add","Subtract","Multiply","Divide","Exit"]
    print("SIMPLE CALCULATOR \n Select Operation:")
    for i in range(len(list)):
         print(f"{i+1}. {list[i]}")
    choice=input("Enter your choice ")
    if(choice.capitalize()!="Exit"):
         n1=float(input("Enter first number: "))
         n2=float(input("Enter second number: "))
    match choice.capitalize():
        case "1" | "Add":
           print(f"Result: {add(n1,n2)}")
           userinput()
        case "2" | "Subtract":
           print(f"Result: {subtract(n1,n2)}")
           userinput()
        case "3" | "Multiply":
           print(f"Result: {multiply(n1,n2)}")
           userinput()
        case "4" | "Divide":
            print(f"Result: {divide(n1,n2)}")
            userinput()
        case "Exit":
            print("Thanks for using this simple calculator app. Hope it helped you.")
        case _:
            print("Invalid choice! Try again.")
            userinput()
userinput()

    



