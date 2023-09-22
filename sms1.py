from tkinter import *
import time
from tkinter import ttk,messagebox
import pymysql
# functinality part
# parent =add_window this is for the pop up shouls be on top
def search_student():
    def search_data():
        query='select * from student where ID=%s or name=%s or email=%s or mobile no=%s or address=%s or DOB=%s or gender=%s '
        mycursor.execute(query, (idEntry.get(), nameEntry.get(), phoneEntry.get(), emailEntry.get(),
                                 addressEntry.get(), dobEntry.get(), genderEntry.get()))
        studenttable.delete(*studenttable.get_children())
        fetched_data=mycursor.fetchall()
        for data in fetched_data:
            studenttable.insert('',END,values=data)





    search_window = Toplevel()
    search_window.grab_set()
    search_window.title('search student')
    search_window.resizable(False, False)
    idLabel = Label(search_window, text='Id', font=('times new roman', 28, 'bold'))
    idLabel.grid(row=0, column=0, padx=30, pady=15)
    idEntry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    idEntry.grid(row=0, column=1, pady=15, padx=10)

    nameLabel = Label(search_window, text='Name', font=('times new roman', 28, 'bold'))
    nameLabel.grid(row=1, column=0, padx=30, pady=15)
    nameEntry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    nameEntry.grid(row=1, column=1, pady=15, padx=10)

    phoneLabel = Label(search_window, text='Phone', font=('times new roman', 28, 'bold'))
    phoneLabel.grid(row=2, column=0, padx=30, pady=15)
    phoneEntry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    phoneEntry.grid(row=2, column=1, pady=15, padx=10)

    emailLabel = Label(search_window, text='Email', font=('times new roman', 28, 'bold'))
    emailLabel.grid(row=3, column=0, padx=30, pady=15)
    emailEntry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    emailEntry.grid(row=3, column=1, pady=15, padx=10)

    addressLabel = Label(search_window, text='Address', font=('times new roman', 28, 'bold'))
    addressLabel.grid(row=4, column=0, padx=30, pady=15)
    addressEntry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    addressEntry.grid(row=4, column=1, pady=15, padx=10)

    dobLabel = Label(search_window, text='DOB', font=('times new roman', 28, 'bold'))
    dobLabel.grid(row=5, column=0, padx=30, pady=15)
    dobEntry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    dobEntry.grid(row=5, column=1, pady=15, padx=10)

    genderLabel = Label(search_window, text='gender', font=('times new roman', 28, 'bold'))
    genderLabel.grid(row=6, column=0, padx=30, pady=15)
    genderEntry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    genderEntry.grid(row=6, column=1, pady=15, padx=10)

    search_student_button = Button(search_window, text='search', command=search_data)
    search_student_button.grid(row=7, columnspan=2)


def add_student():
    def add_data():
        # phone no is 10 digits only becoz i have mentioned
        if idEntry.get()=='' or nameEntry.get()=='' or phoneEntry.get()==''or emailEntry.get()=='' or addressEntry.get()=='' or dobEntry.get()=='' or genderEntry.get()=='':
            messagebox.showerror('error','all fields are required',parent=add_window)
        else:
            # values are strings so %S
            currentdate = time.strftime('%d/%m/%Y')
            currenttime = time.strftime('%H:%M:%S')
            try:
                query='insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                mycursor.execute(query,(idEntry.get(),nameEntry.get(),phoneEntry.get(),emailEntry.get(),
                                        addressEntry.get(),dobEntry.get(),genderEntry.get(),currentdate,currenttime))
                # adding deleting ..like anyything in the data we need to commit
                # and in below code con as global
                con.commit() # to make again empty
                result=messagebox.askyesno('Confirmed','Data added succesfully. do you want to clean the form?')
                if result: # cleans the form
                    idEntry.delete(0,END)
                    nameEntry.delete(0,END)
                    phoneEntry.delete(0,END)
                    emailEntry.delete(0,END)
                    addressEntry.delete(0,END)
                    dobEntry.delete(0,END)
                    genderEntry.delete(0,END)
                else:
                    pass
            except:
                messagebox.showerror('Error','ID cannot be repeated ',parent=add_window)
                return
            query='select * from student'
            mycursor.execute(query)
            fetched_data=mycursor.fetchall()
            #print(fetched_data)
            # data will be in the form of tuple
            # convert to list so use for lloop
            # to delete the old datas
            studenttable.delete(*studenttable.get_children())
            for data in fetched_data:
                datalist=list(data)
                studenttable.insert('',END,values=datalist)
    add_window=Toplevel()
    add_window.resizable(False,False)
    idLabel = Label(add_window, text='Id', font=('times new roman', 28, 'bold'))
    idLabel.grid(row=0, column=0, padx=30, pady=15)
    idEntry = Entry(add_window, font=('roman',15,'bold'),width=24)
    idEntry.grid(row=0, column=1, pady=15, padx=10)

    nameLabel = Label(add_window, text='Name', font=('times new roman', 28, 'bold'))
    nameLabel.grid(row=1, column=0, padx=30, pady=15)
    nameEntry = Entry(add_window, font=('roman', 15, 'bold'), width=24)
    nameEntry.grid(row=1, column=1, pady=15, padx=10)

    phoneLabel = Label(add_window, text='Phone', font=('times new roman', 28, 'bold'))
    phoneLabel.grid(row=2, column=0, padx=30, pady=15)
    phoneEntry = Entry(add_window, font=('roman', 15, 'bold'), width=24)
    phoneEntry.grid(row=2, column=1, pady=15, padx=10)

    emailLabel = Label(add_window, text='Email', font=('times new roman', 28, 'bold'))
    emailLabel.grid(row=3, column=0, padx=30, pady=15)
    emailEntry = Entry(add_window, font=('roman', 15, 'bold'), width=24)
    emailEntry.grid(row=3, column=1, pady=15, padx=10)

    addressLabel = Label(add_window, text='Address', font=('times new roman', 28, 'bold'))
    addressLabel.grid(row=4, column=0, padx=30, pady=15)
    addressEntry = Entry(add_window, font=('roman', 15, 'bold'), width=24)
    addressEntry.grid(row=4, column=1, pady=15, padx=10)

    dobLabel = Label(add_window, text='DOB', font=('times new roman', 28, 'bold'))
    dobLabel.grid(row=5, column=0, padx=30, pady=15)
    dobEntry = Entry(add_window, font=('roman', 15, 'bold'), width=24)
    dobEntry.grid(row=5, column=1, pady=15, padx=10)

    genderLabel = Label(add_window, text='gender', font=('times new roman', 28, 'bold'))
    genderLabel.grid(row=6, column=0, padx=30, pady=15)
    genderEntry = Entry(add_window, font=('roman', 15, 'bold'), width=24)
    genderEntry.grid(row=6, column=1, pady=15, padx=10)

    add_student_button=Button(add_window,text='submit',command=add_data)
    add_student_button.grid(row=7,columnspan=2)


def connect_database():
    def connect():
        global mycursor,con
        try:
            # host name: hostname
            # username is root
            # pwd is root
            con=pymysql.connect(host=hostEntry.get(),user=userEntry.get(),password=passwordEntry.get())
            mycursor=con.cursor()
           # messagebox.showinfo('Sucess','database connection is sucessful',parent=connectWindow)
        except:
            messagebox.showerror('Error','Invalid Details',parent=connectWindow)
            return 
        try:
            query='create database studentmanagementsystem'
            mycursor.execute(query)
            query='use studentmanagementsystem'
            # mycursor is used to execute the queies
            mycursor.execute(query)
            # after running and clicking  connect database
            # now in command line do show databases; then all the databases will be visible
            query = 'create table student (id int not null primary key, name varchar(30), mobile varchar(10),' \
                    'email varchar(30),address varchar(100), gender varchar (20),' \
                    'dob varchar(20), date varchar(50), time varchar(50))'

            mycursor.execute(query)
        except:
            query='use studentmanagementsystem'
            mycursor.execute(query)
        messagebox.showinfo('sucess','database connection is sucessful',parent=connectWindow)
        # enabling all buttons
        connectWindow.destroy()
        addstudentbutton.config(state=NORMAL)
        searchstudentbutton.config(state=NORMAL)
        updatestudentbutton.config(state=NORMAL)
        showstudentbutton.config(state=NORMAL)
        exportstudentbutton.config(state=NORMAL)
        deletestudentbutton.config(state=NORMAL)

    connectWindow = Toplevel()
    connectWindow.geometry('470x250+830+230')
    connectWindow.title("DatabaseConnection")
    connectWindow.resizable(0,0)
    hostnameLabel = Label(connectWindow, text='Host Name', font=('arial', 15, 'bold'))
    hostnameLabel.grid(row=0, column=0,padx=40,pady=20)
    hostEntry =Entry(connectWindow, font=('roman', 15, 'bold'), bd=2)
    hostEntry.grid(row=0, column=1,padx=40,pady=20)

    usernameLabel = Label(connectWindow, text='user Name', font=('arial', 15, 'bold'))
    usernameLabel.grid(row=1, column=0, padx=40, pady=20)
    userEntry = Entry(connectWindow, font=('roman', 15, 'bold'), bd=2)
    userEntry.grid(row=1, column=1, padx=40, pady=20)

    passwordLabel = Label(connectWindow, text='Password', font=('arial', 15, 'bold'))
    passwordLabel.grid(row=2, column=0, padx=40, pady=20)
    passwordEntry = Entry(connectWindow, font=('roman', 15, 'bold'), bd=2)
    passwordEntry.grid(row=2, column=1, padx=40, pady=20)

    connectButton=Button(connectWindow,text="CONNECT",command=connect)
    connectButton.grid(row=3,columnspan=2)




count=0
text=''

def slider():
    global text,count
    if count==len(s):
        count=0
        text=''
    text=text+s[count]
    sliderlabel.config(text=text)
    sliderlabel.after(500,slider)
    count+=1

def clock():
    date=time.strftime('%d/%m/%Y')
    currenttime=time.strftime('%H:%M:%S')
    datetimeLabel.config(text=f'  Date: {date}\nTime: {currenttime}')
    datetimeLabel.after(1000,clock)#for updating seconds part
root=Tk()


root.geometry('1174x680+50+0')
root.resizable(0,0)
root.title("student management system")
datetimeLabel=Label(root,text='hello',font=("times new roman",18,'bold'))
datetimeLabel.place(x=5,y=5)
clock()
s='Student Management System'
sliderlabel=Label(root,text=s,width=30,font=("times new roman",18,'italic bold'))
sliderlabel.place(x=200,y=0)
slider()
connectButton=Button(root,text="connect database",font=('times new roman',15,'bold'),bg="red",command=connect_database)
connectButton.place(x=980,y=0)

leftFrame=Frame(root,bg="grey")
leftFrame.place(x=50,y=80,width=300,height=500)
logo_image=PhotoImage(file='img_4.png')
logo_label=Label(leftFrame,image=logo_image)
logo_label.grid(row=0,column=0)

addstudentbutton=Button(leftFrame,text='Add Student',width=25,state=DISABLED,command=add_student)
addstudentbutton.grid(row=1,column=0,pady=20)

searchstudentbutton=Button(leftFrame,text='Search Student',width=25,command=search_student)
searchstudentbutton.grid(row=2,column=0,pady=20)

deletestudentbutton=Button(leftFrame,text='delete Student',width=25)
deletestudentbutton.grid(row=3,column=0,pady=20)

updatestudentbutton=Button(leftFrame,text='update Student',width=25)
updatestudentbutton.grid(row=4,column=0,pady=20)

showstudentbutton=Button(leftFrame,text='Show student',width=25)
showstudentbutton.grid(row=5,column=0,pady=20)

exportstudentbutton=Button(leftFrame,text='Export Data',width=25)
exportstudentbutton.grid(row=6,column=0,pady=20)
#right frame
rightFrame=Frame(root)
rightFrame.place(x=350,y=90,width=820,height=600)
scrollBarX=Scrollbar(rightFrame,orient=HORIZONTAL)
scrollBarY=Scrollbar(rightFrame,orient=VERTICAL)

studenttable=ttk.Treeview(rightFrame,columns=('ID','Name',"mobile No",
                                              'Email','address','DOB','Gender','Added date','added time'),xscrollcommand=scrollBarX.set,yscrollcommand=scrollBarY.set)
scrollBarX.config(command=studenttable.xview)
scrollBarY.config(command=studenttable.yview)


studenttable.pack(fill=BOTH,expand=1)
scrollBarX.pack(side=BOTTOM,fill=X)
scrollBarY.pack(side=RIGHT,fill=Y)
studenttable.heading('ID',text='ID')
studenttable.heading('Name',text='NAME')
studenttable.heading('mobile No',text='MOBILE NO')
studenttable.heading('Email',text='E mail')
studenttable.heading('address',text='ADDRESS')
studenttable.heading('Gender',text='GENDER')
studenttable.heading('DOB',text='DOB')
studenttable.heading('Added date',text='added date')
studenttable.heading('added time',text='added time')


studenttable.config(show="headings")








root.mainloop()