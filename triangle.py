import math as m 
def decide(a,b,c):
    if(a+b>c and a+c>b and b+c>a):
        return True
    else:
        return False

def area(a,b,c):
    p=(a+b+c)/2
    s=m.pow(p*(p-a)*(p-b),0.5)
    return s

def main():
    a = float(eval(input("请输入第一条边:")))
    b = float(eval(input("请输入第二条边:")))
    c = float(eval(input("请输入第三条边:")))
    while (decide(a,b,c) != True):
        print("对不起，您输入的三个数字无法构成三角形，请重新输入！！")
        a = float(eval(input("请输入第一条边:")))
        b = float(eval(input("请输入第二条边:")))
        c = float(eval(input("请输入第三条边:")))
    areas=area(a,b,c)
    print("三角形({},{},{}) 的面积是 {:.2f}".format(a,b,c,areas))

if __name__=='__main__':
    main()
