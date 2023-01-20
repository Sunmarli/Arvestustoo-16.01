
from module1 import *

salasonad=[]
logins=[]


while True:
    sel=int(input("For registration put 1 \nFor Authorization put 2\nFor exit put 3\n"))
    if sel!=1 and sel!=2:
       print("Goodbye! :(")
       break
    if sel==1: #Registration
        nick=input("Nickname: ")   
        logins.append(nick)
        que=input(str("Random pass?Y/N _"))
        if que=="Y":
            s=salasona(10)
            print("Your random password is: ", s,"\nWelcome!")
            salasonad.append(s)
            print(salasonad)
            print(logins)
        else:
            while True:
                sona=input("Write your password longer than 5 letters.")
                isesalasona(sona) 
                salasonad.append(sona)
                print(salasonad)
                break
    if sel==2: #Authorization 
        name=input("Nickname: ")  
        if name in logins:
            for i in logins:
                for j in salasonad:
                    if i==j:
                        break
            print("Welcome ", name,"!!!")
            break
        else:
            print("Not registered. Choose registration")
    continue




