from turtle import *
import tkinter as tk
from PIL import Image, ImageTk
from random import *
import numpy as np

default=150
class dice(tk.Frame):
    
    def __init__(self, master = None):
        super().__init__(master)
        self.pack()
        self.buildWindow()
    
        
        
        self.one=Image.open("diceimg1.jpg")
        self.two=Image.open("diceimg2.jpg")
        self.three=Image.open("diceimg3.jpg")
        self.four=Image.open("diceimg4.jpg")
        self.five=Image.open("diceimg5.jpg")
        self.six=Image.open("diceimg6.jpg")
        
        self.dindx = [self.one,self.two,self.three,self.four,self.five,self.six]    
    
    def buildWindow(self):
        cv = ScrolledCanvas(self, 400,400,400,400)
        cv.pack(side=tk.LEFT)
        
        turtle = RawTurtle(cv)
        turtle.ht()
        turtle.pu()
        turtle.goto(-100,150)        
        turtle.right(90)
        frame = tk.Frame(self)
        frame.pack(side=tk.RIGHT, fill=tk.BOTH)
        text = tk.StringVar(self, value='How many dice?')
        text2 = tk.StringVar(self,value='How many times?')
        d2r = tk.Entry(frame,textvariable=text)
        d2r.pack()
        NoR = tk.Entry(frame,textvariable=text2)
        NoR.pack()
        
        
        def quitHandler():
            self.master.quit()
        quitButton = tk.Button(frame, text = "Quit", command=quitHandler)
        quitButton.pack()        
        ''' I'll figure out how to show dice some other time in the future...'''
        
        def diceHandler():
            top = tk.Toplevel()
            try:
                dice = int(d2r.get())
            except ValueError:
                msg = tk.Button(top,text='Please enter a number!',command=top.destroy)
                msg.pack()
                return            
            pass

        diceButton = tk.Button(frame,text="Show dice",command=diceHandler)
        diceButton.pack()
        
        def rollhandler():
            top = tk.Toplevel()
            try:
                dice = int(d2r.get())
                times = int(NoR.get())
            except ValueError:
                msg = tk.Button(top,text='Please enter a number!',command=top.destroy)
                msg.pack()
                return
            
            if dice==0 or times==0:
                msg = tk.Button(top, text='No roll!', command=top.destroy)
                msg.pack()
            else:
                while times>0:
                    turtle.write(np.random.randint(1,7,dice), font=("Arial",30,"normal"))
                    turtle.fd(50)
                    times-=1
        rollButton = tk.Button(frame, text = 'Roll!', command=rollhandler)
        rollButton.pack()
        
        def resetHandler():
            cv.delete("all")
            turtle.goto(-100,150)
        clearButton = tk.Button(frame,text='Clear!',command=resetHandler)
        clearButton.pack()
def main():
    root = tk.Tk()
    root.title("Dice!")
    app = dice(root)
    app.mainloop()
    
if __name__ == "__main__":
    main()