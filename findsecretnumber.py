import random
x= random.randint(1,1000000)
t=0
a=0
lst=[]
print("Welcome to THE SECRET NUMBER")
g = int(input("Enter a number:"))
while g!=0:
    if g>x:
        print(g,"is too high")
        t+=1
        print(x)
        g=int(input("Enter a number:"))
    elif g<x:
        print(g,"is too low")
        print(x)
        t+=1
        g=int(input("Enter a number:"))
    elif g==x:
        print("Congratulations!!!")
        print("You found the secret number in",t,"times.")
        lst.append(t)
        print(lst)
        del t
        t=0
        a = input("Do you want to play again? (y/n):")
        while a:
            if a=='y':
                x=random.randint(1,1000000)
                g=int(input("Enter a number:"))
                break
            elif a=='n':
                print("Best:",min(lst))
                print("GOOD BYE")
                g=0
                break
            else:
                print("Please Select y/n")
                a = input("Do you want to play again? (y/n)")