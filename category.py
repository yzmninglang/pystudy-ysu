# import codecs
import json
import os

#Creategory, you give a str category and it will automatically add to json
#Getcategory ,give a number it will give you a category
#Changecategory , you give two strings one is before and the other is changed value


def GetCategory(number):
    with open('./Category.json','r') as f:
        dic=json.load(f)
        return dic[str(number)]
# print(GetCategory('2'))

def ChangeCategory(before,after):
    try:
        with open("./Category.json",'r')as f:
            dic=json.load(f)
            Key=list(dic.values()).index(before)
            dic[str(Key)]=after
            writejson(dic)
    except:
        Addnumbertojson(before)

def Creategory(cates):    #give a new Category(str) ,that will be writed into json file
    if os.path.exists("./Category.json")==False:
        f=open("./Category.json",'w')
        f.close()
    if os.path.getsize('./Category.json')==0 :
        Addnumbertojson(cates)
    else:
        with open('./Category.json','rb') as f:
            value=json.load(f).values()
            print(value)
            if cates in value:
                pass
            else:
                Addnumbertojson(cates)
    f=open("./Category.json",'r')
    dic=json.load(f)
    return max(list(dic.keys()))



def Addnumbertojson(str_):
    if os.path.getsize('./Category.json')==0 :
        key=0
        dic={key:str_}
        writejson(dic)
    else:
        with open ('./Category.json','r') as f:
            # key=int(max(list(json.load(f).keys())))+1
            dic=json.load(f)
            key=int(max(list(dic.keys())))+1
            # print(dic)
            dic[key]=str_
            f.close
        writejson(dic)



def writejson(dic,path='./Category.json'):
    with open(path,'w')as f:
        json.dump(dic,f)
    f.close()

# print(Creategory("ysu"))
# Addnumbertojson("bainqao")

# ChangeCategory('yuzhimin','qq')