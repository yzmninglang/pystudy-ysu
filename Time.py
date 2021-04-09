import datetime 
#All of function return need't recieve parameter ,main 0f them
    #return a dictionary and the struct is {Y,M,D,H,m},only one 
    #function "SubtractionTime" need two {Y,M,D,H,m} and return a
    # dictionary contain two str
#This is a quick module to use time designed by yuzhimin
#GetNowTime : return {Y,M,D,H,m}
#GetInput_YMD :return {Y,M,D,H,m} you have input year,month,day
#GetInput_HM :return {Y,M,D,H,m} you have input hour and minute
#Get_YMD_HM() :return {Y,M,D,H,m} you have input y,m,d,h,m
#both of them consist of a parameter "timestamp" which is used to rank



def GetNowTime():
    now=datetime.datetime.now()
    time={"year":now.year,"month":now.month,"day":now.day,"hour":now.hour,
        "minute":now.minute,"timestamp":now.timestamp()}
    return time

# print(GetNowTime())
def GetInput_YMD():
    YMD=input("Please input Year Month and Day(Y-M-D):")
    decide =True
    while YMD!='q' and decide!=False:
        try:
             YMD=YMD.split("-")
             time_1=datetime.datetime(int(YMD[0]),int(YMD[1]),int(YMD[2]),0,0,0)
             decide=False
             # print(time_1.timestamp())
             time={"year":time_1.year,"month":time_1.month,"day":time_1.day,"hour":0,
        "minute":0,"timestamp":time_1.timestamp()}
             return time
        except:
             print("sorry ,It seems that you have input someything wrong!!")
             YMD=input("Please input Year Month and Day(Y-M-D):")



def GetInput_HM():
    now=datetime.date.today()
    HM=input("Please input Hour and minute(H-M):")
    HM=HM.split("-")
    while eval(HM[0])>=24 or eval(HM[1])>60 or eval(HM[1])<0 or eval(HM[0])<0:
        print("sorry ,what you have entered is illegal,Please input again!!")
        HM=input("Please input Hour and minute(H-M):")
        HM=HM.split("-")
    time_1=datetime.datetime(int(now.year),int(now.month),int(now.day),eval(HM[0]),eval(HM[1]),0)
    time={"year":now.year,"month":now.month,"day":now.day,"hour":eval(HM[0]),
        "minute":eval(HM[1]),"timestamp":time_1.timestamp()}
    # print(time)
    return time   #a dictionary 
                  #{'year':,'month','day','hour','minuite','timestamp'}


def SubtractionTime(large , small):       #recieve a dictionary which consist of 
                                        #{'year':,'month','day','hour','minuite'}
    large=datetime.datetime(large["year"],large["month"],large["day"],large['hour'],large["minute"],0)
    small=datetime.datetime(small["year"],small["month"],small['day'],small['hour'],small["minute"],0)
    delta=large-small
    # print(delta)
    if 'day' in str (delta):
        hour=int(str(delta).split('day,')[0])*24+int(str(delta).split('day,')[1].split(":")[0])
        minute=int(str(delta).split('day,')[1].split(":")[1])
        minutes=hour*60+minute
        result=str(hour)+'h '+str(minute)+ 'm '
        result={"name":result,"Rank":minutes}
    else:
        hour=str(large-small).split(':')[0]
        minute=str(large-small).split(":")[1]
        minutes=int(hour)*60+int(minute)
        result=str(hour)+'h '+str(minute)+ 'm '
        result={"name":result,"Rank":minutes}
    # print(result)
    return result      #a dictionary contain 'name'  and 'Rank',name is str and rank is number





def Get_YMD_HM():
    YMD=GetInput_YMD()
    HM=GetInput_HM()
    time=datetime.datetime(int(YMD['year']),int(YMD['month']),int(YMD['day']),int(HM['hour']),int(HM['minute']),0)
    Time={"year":time.year,'month':time.month,'day':time.day,'hour':time.hour,'minute':time.minute,'timestamp':time.timestamp()}
    return Time



def Getstr(time):
    time_str=str(time['year'])+'-'+str(time['month'])+'-'+str(time['day'])
    h_m=str(time['hour'])+':'+str(time['minute'])
    time={"YMD":time_str,"HM":h_m,"timestamp":time["timestamp"]}
    return time

# Getstr(GetNowTime())


