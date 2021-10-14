from random import randint
x=randint(1,10)
print("you have three chances!")
if((x-2)<0):
    clue=print("clue:above the number  ",x-2)
else:
    clue=print("clue:below the number",x+2)
    
for i in range(0,3):
    user_input=int(input("guess the number:"))
    if(user_input==x):
            print("hurray! you guessed the number!")
            break
    elif(i==2):
        print("you are out of chances")
        break
    else:
        print("wrong! try again")
        continue
y=input("enter 'E' to exit :")
if(y=='E'):
    print("Exit")
else:
    print("please press 'E' to exit!")
    a=input()
    if(a=='E'):
        print("exit")
    
       
    

