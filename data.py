import csv

    # for i in range(len(read)):
    #     for m in range(len(read[0])):
    #         print(read[i][m].center(5," "),end='')
    #     print('\n')
    # print(a[2])
    # print(list(enumerate(read)))
def display(Two_dim_arry):
    print("Date{0}Cate{0}Time{0}Content".format(" "*6))
    read=Two_dim_arry
    for i in range(len(read)):
        for m in range(len(read[0])):
            print(read[i][m].center(8," "),end='')
        print('\n')
with open('data.csv','rt',encoding='utf-8') as csvfile:
    read= csv.reader(csvfile)
    read=list(read)
    display(read)