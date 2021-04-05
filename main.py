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
    i=0;j=10
    while choice!='q':
        hang=data.Datashow((i,j))
        # if i==0:
        #     hang=data.Datashow((i,(i+1)*10))
        # else:
        #     hang=data.Datashow(((i-1)*10,i*10))
        # i+=1
        i,j=j,j+10
        print(i)
        print("Please input what do you want to do?\n[n-next page;s-search;p-picture;q-quit]:")
        choice=msvcrt.getch().decode()  
        print(choice)
        if choice=='n':
            # os.system('cls')
            try:
                # print(i)
                # time.sleep(5)
                if hang-j>10  :
                    # print(i)
                    # if i==1:
                    #     data.Datashow((i,j))
                    # else:
                    #     data.Datashow(((i-1)*10,i*10))
                    data.Datashow((i,j))
                    print(i)
                    # i+=1
                    i,j=j,j+10
                    print("Please input what do you want to do?\n[n-next page;s-search;p-picture;q-quit]:")
                    choice=msvcrt.getch()
                else:
                    pass
                    i=j
                    data.Datashow((i,hang))
                    print(i)
                    i,j=0,10
                    print("Please input what do you want to do?\n[n-next page;s-search;p-picture;q-quit]:")
                    choice=msvcrt.getch().decode()
            except:
                print("sorry,data is over")
                # time.sleep()
                continue
        elif choice=='s':
            print("\rPlease enter the type you want to search?\n[1.time,2-category,3-content]:")
            choice=eval(msvcrt.getch())
            if choice==1:
                print("\rInput by form [M-D or search by Y]:")
                date=input()
                os.system('cls')
                data.searchbytime(date) 
                choice=eval(msvcrt.getch())

#give a delete function
                # if '-' in date :
                #     data.searchbytime()
                #     # time.sleep(10)
                # else:
                #     date.searchbyyear()
                    # time.sleep(10)

        elif int(choice)==2:
                #search by category
                print("\rPlease input Category:")
                Category=input()
                os.system('cls')
                data.SearchByCate(Category) 
                choice=eval(msvcrt.getch())
            

            # DeleteTime()
            # pass
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