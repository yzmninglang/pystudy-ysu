import msvcrt
import sys
import os
import csv
import data
import time
def home():
    os.system('cls')
    select=[" ","1-显示时间记录","2-添加时间记录","3-删除时间记录","4-修改时间记录","5-分析时间记录","6-退出系统"]
    print()
    for i in range(0,17):
        if i in (0,16):
            print("             {:^10s}".format('='*25))
        elif i==1:
            print("            |","{}".format("时间记录与管理系统").center(14),"|")
        elif i%2==1 or i==2:
            print("            {0}                         {0}".format("|"))
        elif i!=14:
            print("            |","{}".format(select[i//2-1]).center(17),"|")
        elif i==14 :
                                    print("            |","{}".format(select[i//2-1]).center(19),"|")    
    choice=msvcrt.getch()
    decide(eval(choice))
    # print(eval(choice))


def decide(choice):
    if choice==1:
        TimeRecordH()
    elif choice==2:
        AddTimeH()
    elif choice==3:
        DeleteTime()
    elif choice==4:
        ChangeTime()
    elif choice==5:
        AnalysisUi()
    else :
        print("see you!")
        sys.exit()



def TimeRecordH():
    os.system('cls')
    choice='p'
    i=1
    while choice!='q':
        data.Datashow((0,10))
        print("Please input what do you want to do[n-next page;s-search;p-picture;q-quit]:")
        choice=msvcrt.getch().decode('UTF-8')  
        # print(choice)
        if choice=='n':
            # os.system('cls')
            try:
                i+=1
                # time.sleep(5)
                print("Please input what do you want to do[n-next page;s-search;p-picture;q-quit]:")
                data.Datashow(((i-1)*10,i*10))
                choice=msvcrt.getch().decode('UTF-8')
            except:
                print("sorry,data is over")
                # time.sleep()
                continue
        elif choice=='s':
            print("Please enter the type you want to search[1.time,2-category,3-content]:")
            choice=eval(msvcrt.getch())
            if choice==1:
                print("Input by form [M-D or search by Y]:")


        elif choice==3:
            # DeleteTime()
            pass
        elif choice==4:
            # ChangeTime()
            pass
        elif choice==5:
            # AnalysisUi()
            pass
        else :
            print("see you!")
            sys.exit()


def AddTimeH():
    pass




def DeleteTime():
    pass


def ChangeTime():
    pass


def AnalysisUi():
    os.system('cls')
    select=[" ","1-时饼图","2-雷达图","3-柱形图","4-主界面"]
    print()
    for i in range(0,12):
        if i in (0,11):
            print("             {:^10s}".format('='*25))
        elif i==1:
            print("            |","{}".format("分析时间记录").center(14),"   |")
        elif i%2==1 or i==2:
            print("            {0}                         {0}".format("|"))
        elif i!=9:
            print("            |","{}".format(select[i//2-1]).center(17),"   |")
        elif i==9   :
                                    print("            |","{}".format(select[i//2-1]).center(19),"|")    
    choice=eval(msvcrt.getch())
    if choice ==1:
        pass
        # Piechart()s
    elif choice==3:
        pass
        # Barchart()
    elif choice==2:
        pass
        # Radar()
    else:
        home()
    # decide(choice)
    # print(eval(choice))

    pass

def main(): 
    home()
main()