#Temperature Conversion Tool
def cel(n):
    temp=(n-32)*5/9
    print('celcius temperature is:',temp)
    return temp
    
def fah(n):
    temp=(9/5)*n+32
    print('fahrenheit tempeature is:',temp)
    return temp

while ( next != 'no' ):
    ch=input("Enter conversion choice(cel or fah):")
    n=int(input("Enter temperature to convert:"))
    if (ch == 'cel'):
        cel(n)
    elif (ch == 'fah'):
        fah(n)
    else :
        print("invalid choice")
    next=input("If you want to continue then yes else no:")
