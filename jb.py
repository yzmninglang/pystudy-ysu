import jieba

txt=open("./honglou.txt",'r',encoding='utf-8').read()

exclude={"我们",'出来','那里','奶奶' ,'自己' ,'一面' ,'只见' ,'两个', '没有', '怎么', '太太', '众人' ,'如今','说道','知道','姑娘','起来','这里','一个','什么','你们'}
words=jieba.lcut(txt)
counts={}
for word in words:
    if word=="老太太":
        word="贾母"
    if len(word)==1:
        continue
    else:
        counts[word]=counts.get(word,0)+1
for word in exclude:
    del(counts[word])
items=list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(10):
    word,count=items[i]
    print("{0:<10}{1:>5}".format(word,count))



