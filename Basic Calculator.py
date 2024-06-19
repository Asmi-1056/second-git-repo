#Basic Calculator

def Add(a,b):
    return a+b
    
def Sub(a,b):
    return a-b

def Mul(a,b):
    return a*b

def Div(a,b):
    return a/b

while ( new != 'no' ):
    ch=input("Enter choice(Add,Sub,Mul,Div):")
    a=int(input("Enter number:"))
    b=int(input("Enter number:"))
    if (ch == 'Add'):
        print("Addition is:",Add(a,b))
    elif (ch == 'Sub'):
        print("Subtraction is:",Sub(a,b))
    elif (ch == 'Mul'):
        print("Multiplication is:",Mul(a,b))
    elif (ch == 'Div'):
        if (b==0):
            print("Cannot divide by zero")
        else:
            print("Division is:",Div(a,b))
    else :
        print("Invalid choice")
    new=input("If you want to continue then yes else no:")
