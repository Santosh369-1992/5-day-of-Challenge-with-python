
role=input("are you Fresher or experienced?")
if(role== "fresher"):
    print("choose one of these options")
    print("1.web developement")
    print("2.App developement")
    print("3.Ds Machine Learning,AI")
    choice=int(input(" choose between 1-3"))
    if(choice==1):
        print("Learn HTML,CSS,JS,Python,DJango")
    elif choice==2:
        print("Learn Java+ DSA+Build Projects")
    elif choice==3:
        print("Learn Python maths R.")
    else :
        print("out of options")
elif(role=="experienced"):
    print("choose one of these options")
    print("1.Data Aalytics")
    print("2.Cloud Computing")
    print("3.Front End")
    choice=int(input(" choose between 1-3"))
    if(choice==1):
        print("Learn python,Excel,PowerBI")
    elif choice==2:
        print("Learn DevOps and Python for automation")
    elif choice==3:
        print("Learn Python ,DJango for Backend")
    else :
        print("out of options")
