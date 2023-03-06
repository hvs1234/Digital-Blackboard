#Libraries
from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter import ttk

#Application Setup
root = Tk()
root.geometry("1050x600+100+80")
root.title("Digital Blackboard")
root.resizable(False,False)

current_x = 0
current_y = 0
value = DoubleVar()
color = 'white'

#Functions
def display():
    global colors
    id = colors.create_rectangle((10,10,30,30),fill="black")
    colors.tag_bind(id, '<Button-1>',lambda x: show_color('black'))
    id = colors.create_rectangle((10,40,30,60),fill="dark blue")
    colors.tag_bind(id, '<Button-1>',lambda x: show_color('dark blue'))
    id = colors.create_rectangle((10,70,30,90),fill="red")
    colors.tag_bind(id, '<Button-1>',lambda x: show_color('red'))
    id = colors.create_rectangle((10,100,30,120),fill="lime")
    colors.tag_bind(id, '<Button-1>',lambda x: show_color('lime'))
    id = colors.create_rectangle((10,130,30,150),fill="indigo")
    colors.tag_bind(id, '<Button-1>',lambda x: show_color('indigo'))
    id = colors.create_rectangle((10,160,30,180),fill="white")
    colors.tag_bind(id, '<Button-1>',lambda x: show_color('white'))
    id = colors.create_rectangle((10,190,30,210),fill="dark green")
    colors.tag_bind(id, '<Button-1>',lambda x: show_color('dark green'))
    id = colors.create_rectangle((10,220,30,240),fill="yellow")
    colors.tag_bind(id, '<Button-1>',lambda x: show_color('yellow'))
    id = colors.create_rectangle((10,250,30,270),fill="orange")
    colors.tag_bind(id, '<Button-1>',lambda x: show_color('orange'))
    id = colors.create_rectangle((10,280,30,300),fill="cyan")
    colors.tag_bind(id, '<Button-1>',lambda x: show_color('cyan'))
    id = colors.create_rectangle((10,310,30,330),fill="slate gray")
    colors.tag_bind(id, '<Button-1>',lambda x: show_color('slate gray'))
    id = colors.create_rectangle((10,340,30,360),fill="brown4")
    colors.tag_bind(id, '<Button-1>',lambda x: show_color('brown4'))

def locate_xy(work):
    global current_x,current_y
    current_x = work.x
    current_y = work.y

def addLine(work):
    global current_x,current_y
    board.create_line((current_x,current_y,work.x,work.y),width=get_current_value(),
                      fill=color,capstyle=ROUND,smooth=TRUE)
    current_x = work.x
    current_y = work.y

def show_color(new_color):
    global color
    color = new_color
    
def erase():
    board.delete('all')
    display()

def change_width():
    pass

def get_current_value():
    global value
    return '{: .2f}'.format(value.get())

def change_width(event):
    global value_label
    value_label.configure(text=get_current_value())

#Application Creation
img1 = PhotoImage(file="E:\\pyImages\\whiteboard logo.png")
img2 = PhotoImage(file="E:\\pyImages\\color section.png")
img3 = PhotoImage(file="E:\\pyImages\\eraser.png")
root.iconphoto(False,img1)
color_label = Label(root,image=img2,bg="#f2f3f5")
color_label.place(x=10,y=20)
eraser = Button(root,image=img3,bg="slate grey",width=37,bd=0,
                activebackground="slate grey",command=lambda: erase())
eraser.place(x=30,y=450)
colors = Canvas(root,bg="slate grey",width=37,height=380,bd=0)
colors.place(x=30,y=60)
board = Canvas(root,bg="black",width=925,height=530,cursor="hand2")
board.place(x=100,y=10)
board.bind('<Button-1>',locate_xy)
board.bind('<B1-Motion>',addLine)
slider = Scale(root,from_=0, to=100,orient='horizontal',variable=value,command=change_width)
slider.place(x=30,y=545)

value_label = Label(root,text=get_current_value())
value_label.place(x=27,y=565)

display()
root.mainloop()