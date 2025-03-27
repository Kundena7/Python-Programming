import random
n = random.randint(1,100)
while True:
    print ("Guess the number")
    x = int(input("the number is"))
    if(x<n):
     print("too low")    
    elif(x>n):
     print("too high")
    else:
     print("commom number")
