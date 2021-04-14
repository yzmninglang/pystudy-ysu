import random
while True:
    pcchoice=random.randint(1,99)%3
    while True:
        try:
            
            print("Please input what you want to input:")
            print("0.Stone\n1.Scissor\n2.Cloth\n3.Quit")
            choice=eval(input())
            if choice in (0,1,2,3):
                break
            else:
                print("aha! It looks like what you input is incorrect")
        except:
            print("Please input number ok?")
    if choice==3:
        break
    if choice==pcchoice:
        print("you think same! ")
    elif choice-pcchoice==-1 or choice-pcchoice==2:
        print("you win!")
    else:
        print("you lose!")
    print()
