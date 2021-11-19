from tkinter import *

resolution = '420x340+800+400'
title = 'Binary to Hex converter'
author = 'itsvishbear'
font = 'Helvetica 9 italic bold'

resolution = str(resolution)
title = str(title)
author = str(author)
font = str(font)

class Windows:
    def __init__(self, win):
        #For Text Labels
        self.lbl1=Label(win, text='Number', font=font)
        self.lbl2=Label(win, text='Result', font=font)
        self.lbl3=Label(win, text=author, font=font, bg='#B45', fg='#000000')

        #Text boxes
        self.t1=Entry(bd=5)
        self.t2=Entry(bd=5)

        #Buttons
        self.btn1 = Button(win, text='Binary', font=font, bg='#B45', fg='#008')
        self.btn2=Button(win, text='Hexadecimal', font=font, bg='#B45', fg='#008')
        self.lbl1.place(x=100, y=100)
        self.t1.place(x=200, y=100)
        self.b1=Button(win, text='Binary', font=font , command=self.bin, bg='#B45', fg='#008')
        self.b2=Button(win, text='Hexadecimal', font=font, bg='#B45', fg='#008')
        self.b2.bind('<Button-1>', self.hex)

        #Coordinates for Buttons, Labels and Textboxes more above aswell
        self.b1.place(x=100, y=150)
        self.b2.place(x=200, y=150)
        self.lbl2.place(x=100, y=200)
        self.t2.place(x=200, y=200)
        self.lbl3.place(x=300, y=320)

        #Results Code
    def bin(self):
        self.t2.delete(0, 'end')
        num1=int(self.t1.get())
        result=bin(num1)
        self.t2.insert(END, str(result))
        
    def hex(self, event):
        self.t2.delete(0, 'end')
        num1=int(self.t1.get())
        result=hex(num1)
        self.t2.insert(END, str(result))

#Gui/Window Code
window=Tk()
mywin=Windows(window)
window.title(title)
window.geometry(resolution)
window['background']='#576675'
window.mainloop()
