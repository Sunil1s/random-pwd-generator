from tkinter import*
import tkinter as tk 
import random
import string

##website title
root=Tk()
root.geometry("800x700")
root.title("random password generator")

##heading at the user interface
title=StringVar()
label=Label(root,textvariable=title,width=90,font=('ALGERIAN',18),bd=5).pack(anchor=W,padx=50,pady=10)
title.set("random secure password generating")


SYMBOLS =   "!§$%&/()=?{[]}*+'#~,;.:-_'<>"
POOR    =    string.ascii_uppercase + string.ascii_lowercase
AVERAGE =    string.ascii_uppercase + string.ascii_lowercase + string.digits
GOOD    =    string.ascii_uppercase + string.ascii_lowercase + string.digits+"@\|/^"
BEST    =    GOOD + SYMBOLS
password = ""


# types of password strengths selection
def selection():
    choice.get()
choice=IntVar()


BUTTON1=Radiobutton(root,text="POOR",variable=choice,value=1,command=selection,bd=20,font=10,width=60,height=1,bg='#ffffff',activebackground='yellow').pack(anchor=CENTER,padx=300,pady=5)


BUTTON2=Radiobutton(root,text="AVERAGE",variable=choice,value=2,command=selection,font=10,width=40,height=2,bg='#ffffff',activebackground='sky blue').pack(anchor=CENTER,padx=180,pady=2)


BUTTON3=Radiobutton(root,text="GOOD",variable=choice,value=3,command=selection,font=10,width=30,height=2,bg='#ffffff',activebackground='red').pack(anchor=CENTER,padx=100,pady=2)


BUTTON4=Radiobutton(root,text="BEST",variable=choice,value=4,command=selection,font=10,width=20,height=2,bg='#ffffff',activebackground='#00ff00').pack(anchor=CENTER,padx=50,pady=3)

def callback():
    DISPLAY.config(text=passwordgeneration())



def passwordgeneration():
    global password
    password = ""
    
    if choice.get() == 1:
        password = password.join(random.sample(POOR, passwordlength.get()))
        return password
    elif choice.get() == 2:
        password = password.join(random.sample(AVERAGE, passwordlength.get()))
        return password
    elif choice.get() == 3:
        password = password.join(random.sample(GOOD, passwordlength.get()))
        return password
    elif choice.get() == 4:
        password = password.join(random.sample(BEST,passwordlength.get()))
        return password
    else:
        print("choose an opion above")    

lengthlabel=StringVar()
lengthlabel.set("Password Length:")
lengthtitle = Label(root, textvariable=lengthlabel).pack(anchor=CENTER,padx=200,pady=30)

passwordlength=IntVar()
spinboxlength = Spinbox(root, from_=8, to_=360, textvariable=passwordlength, width=30).pack(anchor=CENTER,padx=3)

passwordgenerationButton=StringVar()
passwordgenerationButton = Button(root, text="Generate Password",bd=5, height=2, command=passwordgeneration,pady=2,padx=20)
passwordgenerationButton = Button(root, text="Generate Password",bd=5, height=2, command=callback,pady=2,padx=20)
passwordgenerationButton.pack() 
password = str(callback)
  
def copytoclipboard():
    global password
    print(password)
    root.clipboard_clear()
    root.clipboard_append(password)
    root.update()
copyButton = Button(root, text="Copy Password to Clipboard", command=copytoclipboard,bg='#ffffff',activebackground='orange')
copyButton.pack(side=BOTTOM)


DISPLAY = Label(root, text="password is")
DISPLAY.pack(side=BOTTOM)


root.mainloop() 