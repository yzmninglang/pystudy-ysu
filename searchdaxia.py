while True:
    print("Please input the name of heroes(exit to quit):")
    content=input()
    hero={"yuzhimin":{"magic":"good","attack":"plain"},
            "zhangtuo":{"magic":"plain","attack":"good"},
            "yangzi":{"magic":"good","attack":"good"}
            }
    if content=="exit":
        break
    print("Please input your choices 1.magic,0.attack")
    while True:
        try:
            choice=eval(input())
            if choice in (1,0):
                break
            else:
                print("sorry number out of range,please input again:")
        except:
            print("Sorry ,what you input have something wrong!:Please input again:")
    if choice==1:
        y="magic"
    else:
        y="attack"
    if content in hero:
        print("Find it! hero---- {}' {} is {} ".format(content,y,hero[content][y]))
    else:
        print("sorry ,I can't find it ,How about change a name")
    print()
