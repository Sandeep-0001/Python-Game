import random
n=input("Enter Y/y if you want to play\n")
com=random.randint(1,100)
while(n=='Y' or n=='y'):
    user=int(input("Enter your Choice Number\n"))
    if (com==user):
        print("You Correct Guess!!",com)
        break
    elif(user<com):
        print("Your Number is Small")
    elif(user>com):
        print("Your Number is Big")

    else:
        print("SOmething WRong")


