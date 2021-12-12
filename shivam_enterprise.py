# from _typeshed import OpenTextModeReading
from tkinter import *
from tkinter import font
import tkinter.messagebox as tmsg
# from typing import Collection
import time
root = Tk()
# root.geometry("500x500")
root.title("Shivam Enterprise")
# demo func
def Demo_soft():
    tmsg.showinfo("Shivam Enterprise", "This is just a demo software of version 1.0")

def submit_feedback():
    with open("feedback11.txt", "a") as f:
        f.write(f"the feedback is given by {name.get()} and feedback is {str(feedback1)}")
    

def feedback ():
    ask =  tmsg.askquestion("Feedback","Do you want to give the feedback related to this software?")
    if ask == 'yes' :
        feedback11 = Tk()
        feedback11.title("Feedback Clone")
        global feedback1
        feedback1 = Text(feedback11, height=2, width=20)
        feedback1.grid(row=1, column=0)
        Button(feedback11, text="Submit", fg="green",command=submit_feedback).grid(row=2, column=0)
        time.sleep(5)
        tmsg.showinfo("Feedback","thank you for giving the feedback")
        feedback11.mainloop()
    else :
        tmsg.showinfo("Feedback","No worry about it! just Thank to you")


def about_us ():
    tmsg.showinfo("About Us","This is just a demo of our software design with graphics support. As It is just a experiment of Tkinter. I wish to You have like this demo software.")
def submit():
    amt_without_gst = float(rate.get() * weight.get())
    gst_value = ((amt_without_gst*10)/100)
    total_amount = (amt_without_gst+gst_value)
    gstvalue1 = total_amount-amt_without_gst

    gstval.delete("1.0", END)
    gstval.insert(END, gstvalue1)

    withoutgst.delete("1.0", END)
    withoutgst.insert(END, amt_without_gst)

    totalamtval.delete("1.0", END)
    totalamtval.insert(END, total_amount)

    with open("shivamENT.txt","a") as j:
        j.write(f"Name : {name.get()}\n")
        j.write(f"Weight : {weight.get()}\n")
        j.write(f"Metal : {metal.get()}\n")
        j.write(f"GST : {gst_value}\n")
        j.write(f"WithOut Gst : {amt_without_gst}\n")
        j.write(f"ToTal Amount : {total_amount}\n")
    
    
    
# _______________ for menu part _______________

mainmenu = Menu(root)
m1 = Menu(mainmenu, tearoff=0)
m1.add_command(label="New File", command= Demo_soft)
m1.add_command(label="Open File", command= Demo_soft)
m1.add_command(label="Open File From", command= Demo_soft)
m1.add_command(label="New Window", command= Demo_soft)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="File", menu=m1)

m2 = Menu(mainmenu, tearoff=0)
m2.add_command(label="Cut", command= Demo_soft)
m2.add_command(label="Copy", command= Demo_soft)
m2.add_command(label="Paste", command= Demo_soft)
m2.add_command(label="Undo", command= Demo_soft)
m2.add_command(label="Redo", command= Demo_soft)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="Menu", menu=m2)

m3 = Menu(mainmenu, tearoff=0)
m3.add_command(label="Feedback", command= feedback)
m3.add_command(label="About Us ", command= about_us)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="About", menu=m3)

m4 = Menu(mainmenu,tearoff=0)
m4.add_command(label="Exit", command= quit)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="Exit", menu=m4)

#-______________ for label head___________________
Label(root, text="SHIVAM ENTERPRISES", font="comicsans 20 bold", fg="red", relief=SUNKEN, pady=10).grid(row=0, column=2)
Label(root, text="HARDING AND HEAT TREATMENT COMPANY", font="comicsans 10 bold", pady=10).grid(row=1, column=2)

Label(root, text="Name", font= "comicsans 10 bold",pady=10).grid(row=3, column=0)
Label(root, text="Metal", font= "comicsans 10 bold", pady=10).grid(row=4, column=0)
Label(root, text="Weight", font="comicsans 10 bold", pady=10).grid(row=5, column=0)
Label(root, text="Rate", font="comicsans 10 bold", pady=10).grid(row=6, column=0)
Label(root, text="GST", font="comicsans 10 bold", pady=10).grid(row=7, column=0)
Label(root, text="Amt. Without GST", font="comicsans 10 bold", pady=10).grid(row=8, column=0)
Label(root, text="Total Amount", font="comicsans 10 bold", pady=10).grid(row=9, column=0)

# --------------- button ______________________-
Button(root, text="Submit", font="comicsans 10 bold", fg="green", pady=10, command=submit).grid(row=10, column=2)
Button(root, text="Exit", font="comicsans 10 bold", fg="red", pady=10, command=quit).grid(row=10, column=3)

# ------------------ for entering _------------------
name = StringVar()
metal = IntVar()
rate = IntVar()
weight = IntVar()



nameval = Entry(root, textvariable=name).grid(row=3, column=1)
radio = Radiobutton(root, text= "Iron", variable=metal, value=1).grid(row=4, column=1)
radio = Radiobutton(root, text= "Steel", variable=metal, value=2).grid(row=4, column=2)
radio = Radiobutton(root, text= "Copper", variable=metal, value=3).grid(row=4, column=3)
radio = Radiobutton(root, text= "Tin", variable=metal, value=4, padx=10).grid(row=4, column=4)

waitval = Entry(root, textvariable=weight).grid(row=5, column=1)
rateval = Entry(root, textvariable=rate).grid(row=6, column=1)
gstval = Text(root, height=1, width=20)
gstval.grid(row=7, column=1)
withoutgst = Text(root, height=1, width=20)
withoutgst.grid(row=8, column=1)
totalamtval  = Text(root, height=1, width=20)
totalamtval.grid(row=9, column=1)



root.mainloop()