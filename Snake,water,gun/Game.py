import random
# Snake for 1 ,Water for 2 and Gun for 3

while(1):
    com=random.choice([1,2,3])
    user=input("Enter your Choice Snake(s),Water(w),Gun(g)\n")
    dict={'s':1,'w':2,'g':3}
    you=dict[user]

    if (com==you):  
     print("Draw!!")
    elif(com==1 and you==2):
        print("********Computer Win********")
        print("Computer Choose Snake")
    elif(com==1 and you==3):
        print("********You Win********")
        print("Computer Choose Snake")
    elif(com==2 and you==1):
        print("********You Win********")
        print("Computer Choose Water")
    elif(com==2 and you==3):
        print("******Computer Win******")
        print("Computer Choose Water")
    elif(com==3 and you==1):
        print("******Computer Win******")
        print("Computer Choose Gun")
    elif(com==3 and you==2):
        print("********You Win********")
        print("Computer Choose Gun")
    else:
        print("SOmething WRong")
    n=input("Enter Q/q if you want to Quit and Y/y for continue\n")
    if(n=='q' or n=='Q'):
        break