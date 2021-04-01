import time
print()
for i in range(1,12):
    if i in (1,6,11):
        print("             {:^10s}".format('-'*25))
    else:
        print("             {0}           {0}           {0}".format("|"))


scale = 50
print('Windows 正在启动...'.center(scale, '-'))
t = time.perf_counter()
for i in range(scale+1):
    a = '|'*i
    b = '.'*(scale-i)
    c = (i/scale)*100
    print('\r[{}{}]{:^3.0f}%'.format(a,b,c), end='')
    time.sleep(0.05)
t -= time.perf_counter()
print("\n此次开机共花费{:.2}s".format(-t))
