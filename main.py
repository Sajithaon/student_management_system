from tkinter import *
from tkinter import messagebox

#from PIL import ImageTK
def login1():
    if usernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('Error','Fields cannot be empty')
    elif usernameEntry.get()=='sajitha' and passwordEntry.get()=='1234':
        messagebox.showinfo('sucess','welcome')
        window.destroy()
        import sms1


    else:
        messagebox.showerror('error',"please enter correct details")
window=Tk()
window.geometry('1280x700+0+0')
window.title('login for student managgement system')
window.resizable(False,False)
#backgroundImage=ImageTK.\
backgroundImage=PhotoImage(file='img.png')
bgLabel=Label(window,image=backgroundImage)
bgLabel.place(x=0,y=0)
loginFrame=Frame(window,bg="grey")
loginFrame.place(x=400,y=150)
logoImage=PhotoImage(file='img_1.png')
logoLabel=Label(loginFrame,image=logoImage)
logoLabel.grid(row=0,column=0,columnspan=2,pady=10)
usernameImage=PhotoImage(file='img_2.png')
usernameLabel=Label(loginFrame,image=usernameImage,text='Username ',compound=LEFT,font=('times new roman',20,'bold'),bg="white")
usernameLabel.grid(row=2,column=0,pady=10)
usernameEntry=Entry(loginFrame,font=('times new roman',20,'bold'),fg='royal blue')
usernameEntry.grid(row=2,column=1,pady=10,padx=20)
#fg is for txt colour
passwordImage=PhotoImage(file='img_3.png')
passwordLabel=Label(loginFrame,image=passwordImage,text='Username ',compound=LEFT,font=('times new roman',20,'bold'),bg="white")
passwordLabel.grid(row=3,column=0,pady=10)
passwordEntry=Entry(loginFrame,font=('times new roman',20,'bold'),fg='royal blue')
passwordEntry.grid(row=3,column=1,pady=10,padx=20)
loginButton=Button(loginFrame,text='LOGIN',font=('times new roman',14,'bold'),width=15,fg='white',bg='cornflowerblue',activebackground='cornflowerblue',command=login1)
loginButton.grid(row=4,column=1,pady=10)



window.mainloop()
