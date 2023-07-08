import pygame
import random
from pygame import*


from tkinter import*
from PIL import ImageTk,Image
from tkinter import messagebox as mb
import json

pygame.init()

screen_width=1020
screen_height=746
screen=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('platformer')


#images
ocean=pygame.image.load('ocean.jpg')
nemo=pygame.image.load('nemo1.jpg')


pygame.mixer.music.load("ocean-wave.mp3")
pygame.mixer.music.play(-1,2)


#bird
nemo_x=340
nemo_y=200
nemo_y_change=0

shark_x=1000
shark_y=700
i=0


def display_nemo(x,y):
    screen.blit(nemo,(x,y))

def display_shark(x):
    if i==1:
        shark=pygame.image.load('1.png')
        screen.blit(shark,(x,300))
    elif i==2:
        shark=pygame.image.load('2.png')
        screen.blit(shark,(x,300))
    elif i==3:
        shark=pygame.image.load('3.png')
        screen.blit(shark,(x,300))
    elif i==4:
        shark=pygame.image.load('4.png')
        screen.blit(shark,(x,300))
    elif i==5:
        shark=pygame.image.load('5.png')
        screen.blit(shark,(x,300))


score=0
SCORE_FONT=pygame.font.Font('freesansbold.ttf',32)
def score_display(score):
    display=SCORE_FONT.render(f"Score: {score}",True,(255,255,255))
    screen.blit(display,(10,10))
                                                            
count=0
class Quiz:
    def __init__(self):
        self.qn=0
        self.ques=self.question(self.qn)
        self.opt_selected=IntVar()
        self.opts=self.radiobtns()
        self.display_options(self.qn)
        self.buttons()
        self.correct=0
        
    def question(self,qn):
        t=Label(root,text="UNDERWATER PREDATOR QUIZ",width=60,bg="blue",fg="white",font=("Cooper",20,"bold"))
        t.place(x=0,y=2)        
        qn=Label(root,text=q[qn],width=60,font=("Cooper",16,"bold"),anchor="w")
        qn.place(x=70,y=100)
        return qn
    
    def radiobtns(self):
        val=0
        b=[]
        yp=150
        while val<4:
            btn=Radiobutton(root,text=" ",variable=self.opt_selected,value=val+1,font=("times",14))
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
        nbutton=Button(root,text="Next",command=self.nextbtn,width=10,bg="green",fg="white",font=("times",16,"bold"))
        nbutton.place(x=200,y=380)
        quitbutton=Button(root,text="Quit",command=root.destroy,width=10,bg="red",fg="white",font=("times",16,"bold"))
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
        if (i==1):
            info="\nThe correct answers are:"
            info1="\n1.What is the name of the predator?\nA:Muskellunge"
            info2="\n2.What is the weight(kg) of this predator?\nA:32"
            info3="\n3.What is the length(ft) of this predator?\nA:8"
            info4="\n4.What type of specie is this predator?\nA:Esox masquinongy"
        
            mb.showinfo("Result","\n".join([result,correct,wrong,info,info1,info2,info3,info4]))
        elif (i==2):
            info="\nThe correct answers are:"
            info1="\n1.What is the name of the predator?\nA:Great White Shark"
            info2="\n2.What is the lifespan(years) of this predator?\nA:70"
            info3="\n3.What is the length(ft) of this predator?\nA:20"
            info4="\n4.What type of specie is this predator?\nA:Carcharias"

            mb.showinfo("Result","\n".join([result,correct,wrong,info,info1,info2,info3,info4]))
        elif (i==3):
            info="\nThe correct answers are:"
            info1="\n1.What is the name of the predator?\nA:Tiger Shark"
            info2="\n2.What is the weight(kg) of this predator?\nA:635"
            info3="\n3.What is the length(ft) of this predator?\nA:16"
            info4="\n4.What type of specie is this predator?\nA:cuvier"

            mb.showinfo("Result","\n".join([result,correct,wrong,info,info1,info2,info3,info4]))
        elif (i==4):
            info="\nThe correct answers are:"
            info1="\n1.What is the name of the predator?\nA:Basking shark"
            info2="\n2.What is the weight(kg) of this predator?\nA:16"
            info3="\n3.What is the length(ft) of this predator?\nA:26"
            info4="\n4.What type of specie is this predator?\nA:maximus"

            mb.showinfo("Result","\n".join([result,correct,wrong,info,info1,info2,info3,info4]))

run=True
while run:
    
    screen.blit(ocean,(0,0))
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                nemo_y_change=-0.85
            
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_SPACE:
                nemo_y_change=0.45

    nemo_y+=nemo_y_change
    if nemo_y>=400:
        nemo_y=400
    if nemo_y<=0:
        nemo_y=0
        
    display_nemo(nemo_x,nemo_y)

    shark_x-=2
    if shark_x==-600.0:
        shark_x=1000

        #*****
        i=random.randint(1,4)
        #*****

    if shark_x==40:
        score+=1
    
    if (i==1):
        display_shark(shark_x)
    elif (i==2):
        display_shark(shark_x)
    elif (i==3):
        display_shark(shark_x)
    elif (i==4):
        display_shark(shark_x)

    if (200 < shark_x <480) & (290 < (nemo_y+65)< 375):
        run=False
        pygame.quit()
        root=Tk()
        root.geometry("1000x600")
        root.title("Quiz")
        if(i==1):
            with open("json1.json") as f:
                obj=json.load(f)
            canvas = Canvas(root, width = 1000, height = 600)  
            canvas.pack()  
            img = ImageTk.PhotoImage(Image.open("1.png"))  
            canvas.create_image(600, 140, anchor=NW, image=img)
        elif(i==2):
            with open("json2.json") as f:
                obj=json.load(f)
            canvas = Canvas(root, width = 1000, height = 600)  
            canvas.pack()  
            img = ImageTk.PhotoImage(Image.open("2.png"))  
            canvas.create_image(600, 140, anchor=NW, image=img)
        elif(i==3):
            with open("json3.json") as f:
                obj=json.load(f)
            canvas = Canvas(root, width = 1000, height = 600)  
            canvas.pack()  
            img = ImageTk.PhotoImage(Image.open("3.png"))  
            canvas.create_image(600, 140, anchor=NW, image=img)
        elif(i==4):
            with open("json4.json") as f:
                obj=json.load(f)
            canvas = Canvas(root, width = 1000, height = 600)  
            canvas.pack()  
            img = ImageTk.PhotoImage(Image.open("4.png"))  
            canvas.create_image(600, 140, anchor=NW, image=img)
            
        q=(obj['ques'])
        options=(obj['options'])
        a=(obj['ans']) 
        quiz=Quiz()
        root.mainloop()

        
    score_display(score)
    
    pygame.display.update()
pygame.quit()
