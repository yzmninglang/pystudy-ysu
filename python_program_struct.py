import random
q=-1
m=5
a=input("请输入数字区间(Min-Max):")
b=a.split('-')
while q==-1:
    try:
        min_,max_=int(b[0]),int(b[1])
        secret=random.randint(min_,max_)
        guess=-1
        while guess!=secret:
            try:
                if m <=0:
                    q=0
                    print("很遗憾，您到最后都没有猜对，正确答案是{}".format(secret))
                    break
                print("你还有{}机会".format(m))
                guess=eval(input("请输入猜测的数字(范围:{}-{}):".format(min_,max_)))
                if guess==secret:
                    q=0
                    print("恭喜你，答对了！")
                    break
                else:
                    print("再接再厉!")
                    m-=1
                    if guess>min_ and guess<max_:
                        if guess>=secret:
                            max_=guess
                        else:
                            min_=guess
            except:
                print("对不起，您必须输入整数！")
        
    except:
        print("对不起，您输入的区间有问题，请重新输入")
        a=input("请输入数字区间(Min-Max):")
        b=a.split('-')