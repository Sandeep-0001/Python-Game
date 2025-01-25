import random
# Rock for 1 , paper for 2 and Scissor for 3

while(1):
    com=random.choice([1,2,3])
    user=input("Enter your Choice Rock(r),Paper(p),Scissor(s)\n")
    dict={'r':1,'p':2,'s':3}
    you=dict[user]

    if (com==you):  
     print("Draw!!")
    elif(com==1 and you==3):
        print("********Computer Win********")
        print("Computer Choose Rock")
    elif(com==1 and you==2):
        print("********You Win********")
        print("Computer Choose Rock")
    elif(com==2 and you==3):
        print("********You Win********")
        print("Computer Choose paper")
    elif(com==2 and you==1):
        print("******Computer Win******")
        print("Computer Choose paper")
    elif(com==3 and you==2):
        print("******Computer Win******")
        print("Computer Choose Scissor")
    elif(com==3 and you==1):
        print("********You Win********")
        print("Computer Choose Scissor")
    else:
        print("SOmething WRong")
    n=input("Enter Q/q if you want to Quit and Y/y for continue\n")
    if(n=='q' or n=='Q'):
        break