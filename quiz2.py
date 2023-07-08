from tkinter import *  
from PIL import ImageTk,Image  
root = Tk()
root.geometry("1000x600")
canvas = Canvas(root, width = 1000, height = 600)  
canvas.pack()  
img = ImageTk.PhotoImage(Image.open("transparentGradHat.png"))  
canvas.create_image(700, 200, anchor=NW, image=img) 
root.mainloop()
