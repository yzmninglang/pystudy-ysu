import msvcrt
import sys
import os
import csv
import time
import datetime 
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import requests
import json
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

def TimeRecordH():
    choice=0
    def insearch():
        choice=0
        while choice not in (1,2,3):
            print("Please input what type you want to search(1.Cate,2.Date,3.Act):")
            choice=eval(msvcrt.getch())
        if choice==1:
            print("Please input Cate:")
            cate=input()
            list_=search(string=cate,type_="cate")
            display(list_)

        elif choice==2:
            print("Please input Date:")
            date=input()
            list_=search(string=date,type_="date")
            display(list_)
        elif choice==3:
            print("Please input activity:")
            act=input()
            list_=search(string=act,type_="cont")
            display(list_)
    def indelete():
        print("Please input the number you want to delete(or Interval):")
        numbers=input()
        deldata(number=numbers)
        choice()
    def inadd():
        AddDataUI()
        choice()
    def insend():
        i=0
        while i<3:
            try:
                SecondWechat("csv")
                i=4
            except:
                i=i+1
                print("The {} Time,sorry,it have something wrong!".format(i))
                time.sleep(1)
        choice()
    def choice():
        data=FetchData()
        choice=''
        n=0
        while len(choice)==0 or choice== '\n':
            os.system('cls')
            display(data[n:n+10])
            print("Press Enter to next page(s to search):")
            choice=input()
            # print(choice)
            if n+10<len(data):
                n=n+10
            else:
                n=0
        if choice=='s':
            insearch()
        if choice=='d':
            indelete()
        if choice=='a':
            inadd()
        if choice=="w":
            insend()
        if choice=="p":
            inpicture()
            pass
    


    choice()
    # elif choice

    

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

def display(Two_dim_arry):
    os.system('cls')
    print("Number{0}Date{0}Cate{0}Time{0}Content".format(" "*6))
    read=Two_dim_arry
    for i in range(len(read)):
        print(read[i][-1],end=" "*9)
        for m in range(len(read[0])):
            if m<4:
                print(read[i][m].center(8," "),end='')
        print('\n')


def FetchData():# return 2d_array   
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
    with open('data.csv','rt',encoding='utf-8') as csvfile:
        read= csv.reader(csvfile)
        read=list(read)
    for i in range(len(read)):
        read[i][-1]=i
    read=Changedate(read)

    return read


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
    # print(act)

def deldata(number):
    number=str(number)
    # print("Please input number you want to del(or Interval):")
    # number=input()
    def SaveDate(Two_dim_arry):
        for i in range(len(Two_dim_arry)):
            Two_dim_arry[i][-1]=i
        with open('data.csv', 'w', newline='',encoding="utf-8") as csvfile:
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

def search(type_,string):
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
            if cont in data[i][3]:
                Ans.append(data[i])
        return Ans
    if type_=="date":
        return SearchBydate(string)
    elif type_=="cate":
        return SearchBycate(string)
    elif type_=="cont":
        return SearchBycont(string)

    # Cate="跑步"
    # ans=SearchBycont(Cate)
    # display(ans)
 
def DataVisual(char):
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
    def Pie(data):

            labels=list(data[1].keys())
            sizes=list(data[1].values())
            out=sizes.index(max(sizes))
            basic=[0 for i in range(len(sizes))]
            basic[out]=0.1
            axes1=plt.subplot(1,2,1)
            explode = tuple(basic)
            axes1.set_title("Category-Time Pie",fontdict={"fontsize":16,"color":"blue"})
            plt.pie(sizes,labels=labels,explode=explode,autopct='%1.1f%%',shadow=True,startangle=150)
            labels=list(data[0].keys())
            sizes=list(data[0].values())
            out=sizes.index(max(sizes))
            basic=[0 for i in range(len(sizes))]
            basic[out]=0.1
            axes2=plt.subplot(1,2,2)
            explode = tuple(basic)
            axes2.set_title("Content-Time Pie",fontdict={"fontsize":16,"color":"blue"})
            plt.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%',shadow=True,startangle=150)
            plt.show()
    def Rel(data):
            labels=list(data[1].keys())
            sizes=list(data[1].values())
            axes1=plt.subplot(1,2,1)
            axes1.set_title("Category-Time Pie",fontdict={"fontsize":16,"color":"blue"})
            plt.bar(labels,sizes)
            labels=list(data[0].keys())
            sizes=list(data[0].values())
            axes2=plt.subplot(1,2,2)
            axes2.set_title("Content-Time Pie",fontdict={"fontsize":16,"color":"blue"})
            plt.bar(labels,sizes)
            plt.show()
    def Radar(datas):
            matplotlib.rcParams['font.family']='SimHei'
            matplotlib.rcParams["font.sans-serif"]='SimHei'
            labels=list(datas[1].keys())
            sizes=list(datas[1].values())
            axes1=plt.subplot(1,2,1,polar=True)
            size=len(sizes)
            data=np.array(sizes)
            angle=np.linspace(0,2*np.pi,size,endpoint=False)
            data=np.concatenate((data,[data[0]]))
            angle=np.concatenate((angle,[angle[0]]))
            plt.plot(angle,data,'bo-',color='g',linewidth=2)
            plt.fill(angle,data,facecolor='g',alpha=0.25)
            plt.thetagrids(angle*180/np.pi,labels)
            # plt.figtext(0.25,0.95,'Category-Time Radar',ha='center')
            axes1.set_title("Category-Time Radar",fontdict={"fontsize":13,"color":"blue"})
            #second picture
            plt.grid(True)
            labels=list(datas[0].keys())
            sizes=list(datas[0].values())
            axes2=plt.subplot(1,2,2,polar=True)
            size=len(sizes)
            data=np.array(sizes)
            angle=np.linspace(0,2*np.pi,size,endpoint=False)
            data=np.concatenate((data,[data[0]]))
            angle=np.concatenate((angle,[angle[0]]))
            plt.plot(angle,data,'bo-',color='g',linewidth=2)
            plt.fill(angle,data,facecolor='g',alpha=0.25)
            plt.thetagrids(angle*180/np.pi,labels)
            axes2.set_title("Content-Time Radar",fontdict={"fontsize":13,"color":"blue"})
            plt.show()
    data=Getdata(data)
    if char=='pie':
        Pie(data)
    elif char=='rel':
        Rel(data)
    elif char=='radar':
        Radar(data)

# def TimeRecordUi():
#     pass
        
def SecondWechat(filetype):
    def send_data(companyid,appid,secret):
        def uploadimg(filename, access_token):
            from requests_toolbelt import MultipartEncoder
            
            post_file_url = f"https://qyapi.weixin.qq.com/cgi-bin/media/upload?access_token={access_token}&type=file"
            if filetype=="image":
                m =MultipartEncoder(  {"filename":"1.png","file": ('1.png', open(filename, 'rb'),'text/plain')})
            elif filetype=="csv":
                m=MultipartEncoder(  {"filename":"data.csv","file": ('data.csv', open("data.csv", 'rb'),'text/plain')})
            # print(m.content_type)
            # print(m.content_length)
            r = requests.post(url=post_file_url, data=m, headers={'Content-Type': m.content_type})
            r=json.loads(r.text)
            # print(r)
            return r["media_id"]
        def gettoken():
                url="https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={}&corpsecret={}".format(companyid,secret)
                mes=json.loads(requests.get(url=url).text)
                token=mes["access_token"]
                return token
        send_url = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=' + gettoken()
        if filetype=="image":
            send_values = {
                "touser": "@all",
                #"toparty": self.TOPARY,    #设置给部门发送
                "msgtype": "image",
                "agentid": appid,
                "image": {
                "media_id": uploadimg("1.png",gettoken())
                },
                "safe": "0"
            }
        else:
            send_values = {
                "touser": "@all",
                #"toparty": self.TOPARY,    #设置给部门发送
                "msgtype": "file",
                "agentid": appid,
                "file": {
                "media_id": uploadimg("data.csv",gettoken())
                },
                "safe": "0"
            }
        send_msges=(bytes(json.dumps(send_values), 'utf-8'))
        respone = requests.post(send_url, send_msges)
        respone = respone.json()
        return respone["errmsg"]


    send_data(companyid,appid,secret)
home()
# SecondWechat("csv")

# def TimeRecordH():



# def main(): 
#     home()
# main()




# Sortbytime(FetchData())

# display(FetchData())
# Changedata(FetchData())


# Sortbytime(FetchData())
    




# AddDataUI()


# display(FetchData())
# Changedata()

# display(FetchData())
# deldata()
# display(FetchData())






# AddData(["2020-5-26","娱乐",32,"打游戏",32])

# search()


# def ChangeUI():
#     Please
# AddData(["2023-1-21","run",23,'game'])

#Data visualization
# DataVisual('radar')

























# import data
# import time
# import category
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

