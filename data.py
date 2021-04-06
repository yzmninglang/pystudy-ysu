import pandas as pd 
import Time as t
import os
import time

#This is a code use to test
cloumns=['Date','Category','Time','Content','Timestamp','Rank'] 
def CreateData():
    # cloumns=['Date','Category','Time','Content','Timestamp','Rank'] 
    df=pd.DataFrame(columns=cloumns)
    df.to_csv('./data1.csv')
    # print(df)
# CreateData()
def Datashow(tuple,path='./data1.csv'):
    os.system('cls')
    df = GetshowForm()
    print(df.iloc[tuple[0]:tuple[1],:])
    return df.shape[0]   #pass the dateframe hang
    # time.sleep(5)
# print(Datashow((10,20)))
def search():
    # print(str(cloumns[0:2]))
    print("Please input type what you want to find(1.Data;2.Cate;3.Content):")
def GetshowForm():
    df = pd.read_csv('./data3.csv',index_col=None)
    df2 = df[["Date","Time","Category","Content"]]
    # print(df2)
    return df2
# GetshowForm()    
def searchbytime(date):
    df = GetshowForm()
    if '-' in date :
        # print(type(t.GetNowTime()['year']))
        # print(date.split())
        date=date.split("-")[1]+'/'+date.split('-')[0]+'/'+str(t.GetNowTime()['year'])
        # print(df)
        print(df.loc[(df["Date"]==date)])
        # os.system('cls')
    else:
        # df=df["Date"].fillna("None")
        print(df[df['Date'].str.contains(date,na=False)])

        
    # else:
    #     # date.searchbyyear()
    #     time.sleep(10)
# searchbytime('2020')
# search()

def Add(begin_time,over_time,category,content):
    df = pd.read_csv('./data1.csv',index_col=0)
    sub=t.SubtractionTime(begin_time , over_time)
    begin_time=t.Getstr(begin_time)
    print(sub)
    df = df.append([{'Date':'{}'.format(begin_time['YMD']),'Category':'{}'.format(category),'Time':'{}'.format(sub['name']),'Content':'{}'.format(content),'Timestamp':int(begin_time['timestamp']),'Rank':sub["Rank"]}], ignore_index=True,sort=False)
    df.to_csv('data1.csv',index=False, encoding='utf-8')

def SearchByCate(Category) :
    df =GetshowForm()
    print(df[df['Category'].str.contains(Category,na=False)])


# SearchByCate("读书")

def  SearchByContent(content):
    df=GetshowForm()
    print(df[df['Content'].str.contains(content,na=False)])
    

def Addbycost(begin_time,category,content):
    df = pd.read_csv('./data1.csv',index_col=0)
    sub=t.SubtractionTime(begin_time , over_time)
    begin_time=t.Getstr(begin_time)
    print(sub)
    df = df.append([{'Date':'{}'.format(begin_time['YMD']),'Category':'{}'.format(category),'Time':'{}'.format(sub['name']),'Content':'{}'.format(content),'Timestamp':int(begin_time['timestamp']),'Rank':sub["Rank"]}], ignore_index=True)
    df.to_csv('data1.csv',index=False, encoding='utf-8')
# Add(t.GetNowTime(),t.GetNowTime(),'q2q','baidu')
