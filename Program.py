import re
import matplotlib.pyplot as plt
import pinyin as p
import numpy as np
def ParseBool():
    while True:
        print("Remove non 中文 symbols 0 - no, 1 - yes:")
        inp=input()
        if(inp=="1"):
            return True
        elif(inp=="0"):
            return False

print("Enter path to text file UTF8:")
path=input()
RemoveNonChineseWords=ParseBool()

lines=[]
with open(path,encoding="UTF8") as file:
    for line in file:
        cleanLine=(re.sub('\W+','', line))
        if(RemoveNonChineseWords):
            for v in re.findall(r'[\u4e00-\u9fff]+', cleanLine):
                lines.append(v)
        else:
            lines.append(cleanLine)

Dictionary={}

for line in lines:
    for symbol in line:
        if symbol in Dictionary:
            Dictionary[symbol]+=1
        else:
            Dictionary[symbol]=1

listedDictionary=list(Dictionary)
listedDictionary.sort(key=lambda x:Dictionary[x],reverse=True)
id=1
with open("Ready.txt",encoding="UTF8",mode="w") as file:
    for symbol in listedDictionary:
        #print(symbol)
        line=str(id)+" - "+str(Dictionary[symbol])+". "+symbol+" - "+p.get(symbol)
        print(line,file=file)
        #print(line)
        id+=1

x=range(1,len(listedDictionary)+1)
#x=listedDictionary #Так не прокатит т.к. в шрифте нету китайских иероглифов.
y=list(map(lambda v: Dictionary[listedDictionary[v]],range(0,len(listedDictionary))))
#print(x)
#print(y)
plt.bar(x, y)
plt.show()