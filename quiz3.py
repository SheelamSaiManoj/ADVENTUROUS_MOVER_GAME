import pygame
import random
from pygame import*

from tkinter import*
from tkinter import messagebox as mb
import json

class A():     
    def __init__(self):
        self.root=Tk()
        self.root.geometry("1000x600")
        self.root.title("Quiz")
        with open("json1.json") as f:
            self.obj=json.load(f)    
        self.q=(self.obj['ques'])
        self.options=(self.obj['options'])
        self.a=(self.obj['ans'])

        self.root.mainloop()

class Quiz(A):
    def __init__(self):
        A.__init__(self)
        self.qn=0
        self.ques=self.question(self.qn)
        self.opt_selected=IntVar()
        self.opts=self.radiobtns()
        self.display_options(self.qn)
        self.buttons()
        self.correct=0
        
    def question(self,qn):
        t=Label(self.root,text="Quiz in python programming",width=70,bg="blue",fg="white",font=("Cooper",20,"bold"))
        t.place(x=0,y=2)
        qn=Label(self.root,text=q[qn],width=60,font=("Cooper",16,"bold"),anchor="w")
        qn.place(x=70,y=100)
        return qn
    
    def radiobtns(self):
        val=0
        b=[]
        yp=150
        while val<4:
            btn=Radiobutton(self.root,text=" ",variable=self.opt_selected,value=val+1,font=("times",14))
            b.append(btn)
            btn.place(x=100,y=yp)
            val+=1
            yp+=40
        return b
    
    def display_options(self, qn):
        val=0
        self.opt_selected.set(0)
        self.ques['text']=q[qn]
        for op in options[qn]:
            self.opts[val]['text']=op
            val+=1

    def buttons(self):
        nbutton=Button(self.root,text="Next",command=self.nextbtn,width=10,bg="green",fg="white",font=("times",16,"bold"))
        nbutton.place(x=200,y=380)
        quitbutton=Button(self.root,text="Quit",command=root.destroy,width=10,bg="red",fg="white",font=("times",16,"bold"))
        quitbutton.place(x=380,y=380)   

    def checkans(self,qn):
        if self.opt_selected.get()==a[qn]:
            return True

    def nextbtn(self):
        if self.checkans(self.qn):
            self.correct+=1
        self.qn+=1
        if self.qn==len(q):
            self.display_result()
        else:
            self.display_options(self.qn)

    def display_result(self):
        score=int(self.correct/len(q)*100)
        result="Score: "+str(score)+"%"
        wc=len(q)-self.correct
        correct="No.of correct answers :"+str(self.correct)
        wrong="No.of wrong answers: "+str(wc)
        mb.showinfo("Result","\n".join([result,correct,wrong]))


class BP(Quiz):
    def __init__(self):
        top = Tk()  

        top.geometry("1000x600")
        top.title("Quiz1")

        t1=Label(top,text="YOU WERE KILLED BY..",width=60,font=("Cooper",21,"bold"),anchor="w").place(x=70,y=70)
        t1=Label(top,text="hello",width=60,font=("Cooper",16),anchor="w").place(x=70,y=100)
        t1=Label(top,text="welcome",width=60,font=("Cooper",16),anchor="w").place(x=70,y=130)
        t1=Label(top,text="here",width=60,font=("Cooper",16),anchor="w").place(x=70,y=160)
        nbutton1=Button(top,text="Next",command=Quiz(),width=10,bg="green",fg="white",font=("times",16,"bold"))
        nbutton1.place(x=200,y=380)


        top.mainloop()

ob=BP()
