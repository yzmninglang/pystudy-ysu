a=eval(input())
b=eval(input())
c=eval(input())
if a==0 and b==0 :
    print("Data error")
elif a==0 :
    solve=-c/b
    print(solve)
elif b**2-4*a*c<0:
    print("该方程无实数解")
else :
    delte=(b**2-4*a*c)**0.5
    solve_1=(-b-delte)/(2*a)
    solve_2=(-b+delte)/(2*a)
    if solve_1==solve_2:
        print(solve_1)
    elif solve_1>solve_2:
        print("{} {}".format(solve_2,solve_1))
    else:
        print("{} {}".format(solve_1,solve_2))


