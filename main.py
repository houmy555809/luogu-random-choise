from random import *
accepted={}
acrate={}
difficulty={}
submit={}
tag={}
translation={}
match=[]
from tkinter import *
loading=Tk()
loading.title("Loading...")
ltxt=Label(loading,font=("consolas",50),text="Loading...")
ltxt.pack()
lstv=StringVar(loading,"")
lprg=Label(loading,font=("consolas",15),textvariable=lstv)
lprg.pack()
def load():
    with open("accepted.txt","r") as file:
        try:
            txt=file.read().split("\n")
            for i in txt:
                res=i.split()
                val=int(res[0])
                for i in range(1,len(res)):
                    lstv.set(res[i]+".accepted")
                    accepted[res[i]]=val
        except:
            pass
        file.close()
    with open("acrate.txt","r") as file:
        try:
            txt=file.read().split("\n")
            for i in txt:
                res=i.split()
                val=int(res[0])
                for i in range(1,len(res)):
                    lstv.set(res[i]+".acrate")
                    acrate[res[i]]=val
        except:
            pass
        file.close()
    with open("difficulty.txt","r") as file:
        try:
            txt=file.read().split("\n")
            for i in txt:
                res=i.split()
                val=int(res[0])
                for i in range(1,len(res)):
                    lstv.set(res[i]+".difficulty")
                    difficulty[res[i]]=val
        except:
            pass
        file.close()
    with open("submit.txt","r") as file:
        try:
            txt=file.read().split("\n")
            for i in txt:
                res=i.split()
                val=int(res[0])
                for i in range(1,len(res)):
                    lstv.set(res[i]+".submit")
                    submit[res[i]]=val
        except:
            pass
        file.close()
    with open("tag.txt","r") as file:
        try:
            txt=file.read().split("\n")
            for i in txt:
                res=i.split()
                val=int(res[0])
                for i in range(1,len(res)):
                    lstv.set(res[i]+".tag")
                    if res[i] in tag.keys():
                        tag[res[i]].append(val)
                    else:
                        tag[res[i]]=[val]
        except:
            pass
        file.close()
    with open("translation.txt","r") as file:
        try:
            txt=file.read().split("\n")
            for i in txt:
                res=i.split()
                val=res[0]=="true"
                for i in range(1,len(res)):
                    lstv.set(res[i]+".translation")
                    translation[res[i]]=val
        except:
            pass
        file.close()
    loading.destroy()
loading.after(100,load)
loading.mainloop()
root=Tk()
root.title("Luogu random chooser")
root.geometry("500x500")
stv=StringVar(root,"Please enter the conditions")
ent=Entry(root,textvariable=stv,font=("consolas",15),width=100)
ent.pack()
res=StringVar(root,"Last result:")
result=Label(root,textvariable=res,font=("consolas",15))
def choose():
    match=[]
    try:
        for i in accepted.keys():
            if not i in tag.keys():
                tag[i]=[]
            if not i in acrate.keys():
                acrate[i]=None
            statement=stv.get().replace("accepted",str(accepted[i]))\
                       .replace("acrate",str(acrate[i]))\
                       .replace("difficulty",str(difficulty[i]))\
                       .replace("submit",str(submit[i]))\
                       .replace("tag",str(tag[i]))\
                       .replace("translation",str(translation[i]))
            if eval(statement):
                match.append(i)
    except Exception as e:
        res.set("Last result:ERR")
        return
    if len(match)==0:
        res.set("Last result:None")
        return
    res.set("Last result:"+choice(match))
btn=Button(root,text="Choose",command=choose)
btn.pack()
result.pack()
root.mainloop()
