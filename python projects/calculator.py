def addition(a,b):
    return a+b

while 1:
    a=float(input('enter first no:-'))
    b=float(input('enter second no:-'))
    print("What would you like to do:-")
    print("1. Addition")
    print("2. Subtraction")
    print("3  Multiplication")
    print("4. Division")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    
    if choice==1:
        print('a+b=',a+b)
    if choice==2:
        print('a-b=',a-b)
    if choice==3:
        print('a*b=',a*b)
    if choice==4:
        print('a%,b=',a%b)
    if choice==5:
        print(int(a),'+',int(b),'=',addition(a,b))
    else:
        continue
        

    