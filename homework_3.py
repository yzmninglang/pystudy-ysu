a=eval(input())
def isseven(number):
    if number%7==0:
        return True
    elif number%10==7:
        return True
    else:
        return False

for i in range(1,a+1,1):
    if isseven(i):
        print(i)