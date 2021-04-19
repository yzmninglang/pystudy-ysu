import msvcrt
import sys
import os
import csv
import time
import datetime 
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import re
import requests
import json

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
    if os.path.exists('./data.csv')==True:
        with open('data.csv','rt',encoding='utf-8') as csvfile:
            read= csv.reader(csvfile)
            read=list(read)
        for i in range(len(read)):
            read[i][-1]=i
        read=Changedate(read)
    else:
        read=[]

    return read
def Getdata(Two_dim_arry):
    content_time={}
    cate_time={}
    for x in Two_dim_arry:
       content_time[x[3]]=content_time.get(x[3],0)+int(x[2]) 
       cate_time[x[1]]=cate_time.get(x[1],0)+int(x[2])
    res=[content_time,cate_time]
    return res
print(Getdata(FetchData()))