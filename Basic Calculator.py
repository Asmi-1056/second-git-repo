#Asmi Purarkar
#Basic Calculator

def add(a,b):
    return a+b
    
def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

while ( next != 'no' ):
    ch=input("Enter choice(add,sub,mul,div):")
    a=int(input("Enter number:"))
    b=int(input("Enter number:"))
    if (ch == 'add'):
        print("addition is:",add(a,b))
    elif (ch == 'sub'):
        print("subtraction is:",sub(a,b))
    elif (ch == 'mul'):
        print("multiplication is:",mul(a,b))
    elif (ch == 'div'):
        if (b==0):
            print("can not divide by zero")
        else:
            print("division is:",div(a,b))
    else :
        print("invalid choice")
    next=input("If you want to continue then yes else no:")