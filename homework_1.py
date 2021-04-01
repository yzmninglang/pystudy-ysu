a=input()
b=a
if b.isdigit()==False:
    print("输入错误")
elif int(b)%2==0 :
    print("{}是一个偶数".format(b))
else:
    print("{}是一个奇数".format(b))