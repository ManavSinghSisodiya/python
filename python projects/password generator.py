# password generator
while 1:
    import random
    length=int(input(' enter password length  :'))
    char="abcdefghijklmnopqrstuvwxyz"
    num="1234567890"
    sp="!@#$%^&*():?|~"
    for index in range(length):
        a=random.choice(char+num+sp)
        print(a,end="")
        
  
print('hello')
    