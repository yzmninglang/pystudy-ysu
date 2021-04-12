import msvcrt
import sys
import os
import csv
import datetime 
import matplotlib.pyplot as plt
# import data
# import time
# import category
def home():

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


def GetNowTime():
    now=datetime.datetime.now()
    time={"year":now.year,"month":now.month,"day":now.day,"hour":now.hour,
        "minute":now.minute,"timestamp":now.timestamp()}
    return time


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

# def main(): 
#     home()
# main()
def display(Two_dim_arry):
    print("Number{0}Date{0}Cate{0}Time{0}Content".format(" "*6))
    read=Two_dim_arry
    for i in range(len(read)):
        print(read[i][-1],end=" "*9)
        for m in range(len(read[0])):
            if m<4:
                print(read[i][m].center(8," "),end='')
        print('\n')


def FetchData():# return 2d_array   
    with open('data.csv','rt',encoding='utf-8') as csvfile:
        read= csv.reader(csvfile)
        read=list(read)
    for i in range(len(read)):
        read[i][-1]=i
    return read
#def AddData(one_dim_list):  #[Date,Cate,Time,Content,number](Don't worry about date)
    def DecideDate(date):
        if str(date).count('-')==1:
            date=str(GetNowTime()['year'])+"-"+str(date)
        else:
            date=str(date)
        return date
    def SaveDate(Two_dim_arry):
        for i in range(len(Two_dim_arry)):
            Two_dim_arry[i][-1]=i
        with open('data.csv', 'w', newline='',encoding="utf-8") as csvfile:
            writer  = csv.writer(csvfile)
            for row in Two_dim_arry:
                writer.writerow(row)
    one_dim_list[0]=DecideDate(one_dim_list[0])
    data=FetchData()
    data.append(one_dim_list)
    SaveDate(data)

def Sortbydate(Two_dim_arry):
    def Changedate(Two_dim_arry):
        def decide(time):
            time=str(time).split("-")
            for i in range(1,3):
                if len(time[i])==1:
                    # print(time)
                    time[i]="0"+str(time[i])
                    # print(time)
            res = str(time[0])+'-'+str(time[1])+'-'+str(time[2])
            return res
                
        for x in Two_dim_arry:
            x[0]=decide(x[0])
        # display(Two_dim_arry)
        return Two_dim_arry
    Two_dim_arry=Changedate(Two_dim_arry)
    a=sorted(Two_dim_arry,key=(lambda x:x[0].replace('-','')[-8:]),reverse=True)
    return a 
    # display(Two_dim_arry)
    # print(Two_dim_arry)
    # display(a)
# Sortbytime(FetchData())

# display(FetchData())
# Changedata(FetchData())
def Sortbytime(Two_dim_arry):
    def Changedate(Two_dim_arry):
        def decide(time):
            time=str(time).split("-")
            for i in range(1,3):
                if len(time[i])==1:
                    # print(time)
                    time[i]="0"+str(time[i])
                    # print(time)
            res = str(time[0])+'-'+str(time[1])+'-'+str(time[2])
            return res
                
        for x in Two_dim_arry:
            x[0]=decide(x[0])
        # display(Two_dim_arry)
        return Two_dim_arry
    Two_dim_arry=Changedate(Two_dim_arry)
    Two_dim_arry=sorted(Two_dim_arry,key=(lambda x:x[2]),reverse=True)
    display(Two_dim_arry)
# Sortbytime(FetchData())
    

def Changedata():
    print("Please input which data you want to change:")
    choice=eval(input())
    data=FetchData()
    def ReplaceCate(content,Category):
        def SaveData(Two_dim_arry):
            for i in range(len(Two_dim_arry)):
                Two_dim_arry[i][-1]=i
            with open('data.csv', 'w', newline='',encoding="utf-8") as csvfile:
                writer  = csv.writer(csvfile)
                for row in Two_dim_arry:
                    writer.writerow(row)
        data=FetchData()
        for x in data:
            if x[3]==content:
                x[1]=Category
            else :
                continue
        SaveData(data)

    def AddData(one_dim_list):  #[Date,Cate,Time,Content,number](Don't worry about date)
        def DecideDate(date):
            if str(date).count('-')==1:
                date=str(GetNowTime()['year'])+"-"+str(date)
            else:
                date=str(date)
            return date
        def SaveDate(Two_dim_arry):
            for i in range(len(Two_dim_arry)):
                Two_dim_arry[i][-1]=i
            with open('data.csv', 'w', newline='',encoding="utf-8") as csvfile:
                writer  = csv.writer(csvfile)
                for row in Two_dim_arry:
                    writer.writerow(row)
        one_dim_list[0]=DecideDate(one_dim_list[0])
        data=FetchData()
        data.append(one_dim_list)
        SaveDate(data)
    print("Date:{},Please input new date:".format(data[choice][0]))
    date=input()
    if len(date)==0:
        date=data[choice][0]
    print("Time:{},Please input new time:".format(data[choice][2]))
    time=input()
    if len(time)==0:
        time=data[choice][2]
    else:
        time=int(time)
    print("Content:{},Please input new content:".format(data[choice][3]))
    content=input()
    if len(content)==0:
        content=data[choice][3]    
    print("Category:{},Please input new Category:".format(data[choice][1]))
    Cate=input()
    if len(Cate)==0:
        Cate=data[choice][1]
    del data[choice]
    act=[date,Cate,time,content,0]
    deldata(choice)
    ReplaceCate(act[3],act[1])
    AddData(act)



def AddDataUI():
    def searchcatebycontent(content):
        data=FetchData()
        for i in range(len(data)):
            if content == data[i][3]:
                return data[i][1]
        return False
    def AddData(one_dim_list):  #[Date,Cate,Time,Content,number](Don't worry about date)
        def DecideDate(date):
            if str(date).count('-')==1:
                date=str(GetNowTime()['year'])+"-"+str(date)
            else:
                date=str(date)
            return date
        def SaveDate(Two_dim_arry):
            for i in range(len(Two_dim_arry)):
                Two_dim_arry[i][-1]=i
            with open('data.csv', 'w', newline='',encoding="utf-8") as csvfile:
                writer  = csv.writer(csvfile)
                for row in Two_dim_arry:
                    writer.writerow(row)
        one_dim_list[0]=DecideDate(one_dim_list[0])
        data=FetchData()
        data.append(one_dim_list)
        SaveDate(data)
    print("Please input date(No input year default is Today ):")
    date=input()
    if len(date)==0:
        Time=GetNowTime()
        date=str(Time["year"])+'-'+str(Time["month"])+'-'+str(Time["day"])
    print("Please input Time you have cost")
    time=eval(input())
    print("Please input Content you have to do")
    content=input()
    if searchcatebycontent(content)==False:
        print("Please input Cate:")#
        Cate=input()
    else:
        Cate=searchcatebycontent(content)

    act=[date,Cate,time,content,0]
    AddData(act)
    print(act)

# AddDataUI()


def deldata(number):
    number=str(number)
    # print("Please input number you want to del(or Interval):")
    # number=input()
    def SaveDate(Two_dim_arry):
        for i in range(len(Two_dim_arry)):
            Two_dim_arry[i][-1]=i
        with open('data.csv', 'with', newline='',encoding="utf-8") as csvfile:
            writer  = csv.writer(csvfile)
            for row in Two_dim_arry:
                writer.writerow(row)
    def decide(number):
        if '-' in number:
            a=int(number.split('-')[0])
            b=int(number.split('-')[1])
            return a,b
        else:
            return False
    if decide(number) ==False:
        data=FetchData()
        del data[int(number)]
        SaveDate(data)
    else:
        begin,end=decide(number)
        data=FetchData()
        for i in range(begin,end+1):
            del data[begin]
        SaveDate(data)

# display(FetchData())
# Changedata()

# display(FetchData())
# deldata()
# display(FetchData())


def search():
    def SearchBydate(date):
        data=FetchData()
        Ans = []
        for i in range(len(data)):
            if date in data[i][0]:
                Ans.append(data[i])
        return Ans
    def SearchBycate(Cate):
        data=FetchData()
        Ans=[]
        for i in range(len(data)):
            if Cate in data[i][1]:
                Ans.append(data[i])
        return Ans
    def SearchBycont(cont):
        data=FetchData()
        Ans=[]
        for i in range(len(data)):
            if Cate in data[i][3]:
                Ans.append(data[i])
        return Ans
    Cate="跑步"
    ans=SearchBycont(Cate)
    display(ans)
 
# AddData(["2020-5-26","娱乐",32,"打游戏",32])

# search()


# def ChangeUI():
#     Please
# AddData(["2023-1-21","run",23,'game'])

#Data visualization
def DataVisual():
    data=FetchData()
    plt.rcParams['font.sans-serif']=['SimHei']
    def Getdata(Two_dim_arry):
        content_time={}
        cate_time={}
        for x in Two_dim_arry:
           content_time[x[3]]=content_time.get(x[3],0)+int(x[2]) 
           cate_time[x[1]]=cate_time.get(x[1],0)+int(x[2])
        res=[content_time,cate_time]
        return res
    def Pie(choice,data):
        if choice.lower()=='c':
            labels=list(data[1].keys())
            sizes=list(data[1].values())
            # print(len(labels),len(sizes))
            # print("I am here")
            plt.pie(sizes,labels=labels,autopct='%1.1f%%',shadow=False,startangle=150)
            plt.show()
        elif choice.lower()=='a':
            labels=list(data[0].keys())
            sizes=list(data[0].values())
            plt.pie(sizes,labels=labels,autopct='%1.1f%%',shadow=False,startangle=150)
            plt.show()
    def Rel(choice,data):
        if choice.lower()=='c':
            labels=list(data[1].keys())
            sizes=list(data[1].values())
            plt.bar(labels,sizes)
            plt.show()
        else:
            labels=list(data[0].keys())
            sizes=list(data[0].values())
            plt.bar(labels,sizes)
            plt.show()

    data=Getdata(data)
    Rel('c',data)

DataVisual()


























# def TimeRecordH():
#     os.system('cls')
#     choice='p'
#     i=0;j=10
#     while choice!='q':
#         hang=data.Datashow((i,j))
#         # if i==0:
#         #     hang=data.Datashow((i,(i+1)*10))
#         # else:
#         #     hang=data.Datashow(((i-1)*10,i*10))
#         # i+=1
#         i,j=j,j+10
#         print(i)
#         print("Please input what do you want to do?\n[n-next page;s-search;p-picture;q-quit]:")
#         choice=msvcrt.getch().decode()  
#         print(choice)
#         if choice=='n':
#             # os.system('cls')
#             try:
#                 # print(i)
#                 # time.sleep(5)
#                 if hang-j>10  :
#                     # print(i)
#                     # if i==1:
#                     #     data.Datashow((i,j))
#                     # else:
#                     #     data.Datashow(((i-1)*10,i*10))
#                     data.Datashow((i,j))
#                     print(i)
#                     # i+=1
#                     i,j=j,j+10
#                     print("Please input what do you want to do?\n[n-next page;s-search;p-picture;q-quit]:")
#                     choice=msvcrt.getch()
#                 else:
#                     pass
#                     i=j
#                     data.Datashow((i,hang))
#                     print(i)
#                     i,j=0,10
#                     print("Please input what do you want to do?\n[n-next page;s-search;p-picture;q-quit]:")
#                     choice=msvcrt.getch().decode()
#             except:
#                 print("sorry,data is over")
#                 # time.sleep()
#                 continue
#         elif choice=='s':
#             print("\rPlease enter the type you want to search?\n[1.time,2-category,3-content]:")
#             choice=eval(msvcrt.getch())
#             if choice==1:
#                 print("\rInput by form [M-D or search by Y]:")
#                 date=input()
#                 os.system('cls')
#                 data.searchbytime(date) 
#                 choice=eval(msvcrt.getch())

#                                             #give a delete function
#                 # if '-' in date :
#                 #     data.searchbytime()
#                 #     # time.sleep(10)
#                 # else:
#                 #     date.searchbyyear()
#                     # time.sleep(10)

#             elif choice==2:
#                 #search by category
#                 print("\rPlease input Category:")
#                 Category=input()
#                 os.system('cls')
#                 data.SearchByCate(Category) 
#                 choice=eval(msvcrt.getch())
#                 if choice=='q':
#                     data.Datashow((1,10))

#             elif choice==3:
#                 print("\rPlease input Content")
#                 content=input()
#                 os.system('cls')
#                 data.SearchByContent(content)
#                 choice=str(msvcrt.getch())
#                 if choice=='q':
#                     data.Datashow((1,10))
        

#             # DeleteTime()
#             # pass
#         elif choice=='p':
#             AnalysisUi()

#         else :
#             print("see you!")
#             sys.exit()


# def AddTimeH():
#     data.Datashow((0,10))
#     print("Please input what type data you want to enter\n[1.time,2.clock,3.date and clock]:")
#     choice=msvcrt.getch()
#     if choice==1:
#         print("Please input how much time you have cost:")
#         time=eval(input())
#         print("Please input the content of activity:")
#         content=input()
#         if judge(content):
#             addbytime(,content,time,data.GetCateBycontent(content))
#         else:
#             print("Please input the Category:")
#             category=input()


#     elif choice==2:
#         print("Please input how much time you have cost:")
#         time=eval(input())
#         print("Please input the content of activity:")
#         if judge(content):
#             addbyclock(content,time,data.GetCateBycontent(content))
#         else:
#             print("Please input the Category:")
#             category=input()
#             addbyclock(content,time,data.GetCateBycontent(content))

            

#     elif choice==3:
#         addbydate()
# # def getinputdata():
# #     data=input("Pla")


# def judge(content):

#     pass
# # def addbydate():
# #     s



# def DeleteTime():
#     pass


# def ChangeTime():
#     pass

