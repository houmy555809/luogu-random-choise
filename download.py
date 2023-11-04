from requests import get
import urllib
from urllib import parse
import re
import time
import random
difficulty={}
tag={}
translation={"true":[],"false":[]}
submit={}
accepted={}
acrate={}
header={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}
def fetch(name):
    url="https://www.luogu.com.cn/problem/"+name
    print(name,end=" ")
    try:
        html=get(url,headers=header).text
    except Exception as e:
        print("ERR",e)
        return
    try:
        txt=urllib.parse.unquote(html)
        sdiff=re.findall("[0-9]",re.findall("\"difficulty\":[0-9]",txt)[0])[0]
        if not sdiff in difficulty.keys():
            difficulty[sdiff]=[name]
        else:
            difficulty[sdiff].append(name)
        stag=re.findall("[0-9]+",re.findall("\"tags\":[\[\]0-9,]+",txt)[0])
        for i in stag:
            if not i in tag.keys():
                tag[i]=[name]
            else:
                tag[i].append(name)
        stransl=re.findall("(true|false)",re.findall("\"wantsTranslation\":[a-z]+",txt)[0])[0]
        translation[stransl].append(name)
        ssubmit=int(re.findall("[0-9]+",re.findall("\"totalSubmit\":[0-9]+",txt)[0])[0])
        if not ssubmit in submit:
            submit[ssubmit]=[name]
        else:
            submit[ssubmit].append(name)
        saccept=int(re.findall("[0-9]+",re.findall("\"totalAccepted\":[0-9]+",txt)[0])[0])
        if not saccept in accepted:
            accepted[saccept]=[name]
        else:
            accepted[saccept].append(name)
        sacrate=int(round(saccept/ssubmit*100))
        if not sacrate in acrate:
            acrate[sacrate]=[name]
        else:
            acrate[sacrate].append(name)
        print("SUCCESS")
    except Exception as e:
        print("ERR",e)
for i in range(1000,10000):
    name="P"+str(i)
    fetch(name)
    time.sleep(2)
with open("difficulty.txt","a") as file:
    file.truncate(0)
    for i in difficulty.keys():
        file.write(str(i)+" ")
        for j in difficulty[i]:
            file.write(str(j)+" ")
        file.write("\n")
    file.close()
with open("tag.txt","a") as file:
    file.truncate(0)
    for i in tag.keys():
        file.write(str(i)+" ")
        for j in tag[i]:
            file.write(str(j)+" ")
        file.write("\n")
    file.close()
with open("translation.txt","a") as file:
    file.truncate(0)
    for i in translation.keys():
        file.write(str(i)+" ")
        for j in translation[i]:
            file.write(str(j)+" ")
        file.write("\n")
    file.close()
with open("submit.txt","a") as file:
    file.truncate(0)
    for i in submit.keys():
        file.write(str(i)+" ")
        for j in submit[i]:
            file.write(str(j)+" ")
        file.write("\n")
    file.close()
with open("accepted.txt","a") as file:
    file.truncate(0)
    for i in accepted.keys():
        file.write(str(i)+" ")
        for j in accepted[i]:
            file.write(str(j)+" ")
        file.write("\n")
    file.close()
with open("acrate.txt","a") as file:
    file.truncate(0)
    for i in acrate.keys():
        file.write(str(i)+" ")
        for j in acrate[i]:
            file.write(str(j)+" ")
        file.write("\n")
    file.close()
