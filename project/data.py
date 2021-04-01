import pandas as pd 
import Time as t

def CreateData():
    cloumns=['Date','Category','Time','Content','Timestamp','Rank'] 
    df=pd.DataFrame(columns=cloumns)
    df.to_csv('./data1.csv')
    # print(df)
# CreateData()
def Datashow():
    df = pd.read_csv('./data1.csv',index_col=0)
    print(df)
def Add(begin_time,over_time,category,content):
    df = pd.read_csv('./data1.csv',index_col=0)
    sub=t.SubtractionTime(begin_time , over_time)
    begin_time=t.Getstr(begin_time)
    print(sub)
    df = df.append([{'Date':'{}'.format(begin_time['YMD']),'Category':'{}'.format(category),'Time':'{}'.format(sub['name']),'Content':'{}'.format(content),'Timestamp':int(begin_time['timestamp']),'Rank':sub["Rank"]}], ignore_index=True,sort=False)
    df.to_csv('data1.csv',index=False, encoding='utf-8')

def Addbycost(begin_time,category,content):
    df = pd.read_csv('./data1.csv',index_col=0)
    sub=t.SubtractionTime(begin_time , over_time)
    begin_time=t.Getstr(begin_time)
    print(sub)
    df = df.append([{'Date':'{}'.format(begin_time['YMD']),'Category':'{}'.format(category),'Time':'{}'.format(sub['name']),'Content':'{}'.format(content),'Timestamp':int(begin_time['timestamp']),'Rank':sub["Rank"]}], ignore_index=True)
    df.to_csv('data1.csv',index=False, encoding='utf-8')
Add(t.GetNowTime(),t.GetNowTime(),'q2q','baidu')
