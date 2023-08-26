# password generator
while 1:
    import random
    length=int(input(' enter password length  :'))
    char="abcdefghijklmnopqrstuvwxyz"
    num="1234567890"
    sp="!@#$%^&*():?|~"
    for index in range(length):
        print(random.choice(char+num+sp),end=" ")
        
  
    
    