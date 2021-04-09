import csv
with open('data.csv','rt',encoding='utf-8') as csvfile:
    read= csv.reader(csvfile)
    a=list(read)
    print(a[2])
    # print(list(enumerate(read)))