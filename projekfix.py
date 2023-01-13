import tkinter
from tkinter import *
from time import strftime
from datetime import *

#Ukuran window
window = Tk()
cnv = Canvas(background="white", width=700, height=600)
cnv.pack()
window.title("To-do List")
window.resizable(False,False)

#List untuk menampung data yang diinputkan to do list
task_list = []

#Function untuk menambahkan data yang masuk ke list taskList
def addTask(): 
    task = entryTask.get()
    entryTask.delete(0, END)  
    if task:
        with open("taskList.txt","a") as taskFile:
            taskFile.write(f"\n{task}")
        task_list.append(task)
        listTask.insert(END, task)
        
#Function untuk menghapus data yang masuk ke list taskList
def deleteTask(): 
    global task_list
    task = str(listTask.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("taskList.txt","w") as taskFFile:
            for task in task_list:
                taskFFile.write(task+"\n")       
        listTask.delete(ANCHOR)
        
#Function untuk Membaca data yang telah masuk ke list taskList
def openFiletask():
    try:
        global task_list
        with open("taskList.txt","r") as tl:
            tasks = tl.readlines()      
        for task in tasks:
            if task !="\n":
                task_list.append(task)
                listTask.insert(END, task)
    except:
        file = open('taskList.txt','w')
        file.close()
        
#Function untuk membuat waktu
def getTime(): 
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, getTime)
    
#Function untuk membuat tanggal
def getDate(): 
    global dateVar
    dateVar.set(datetime.now().date())
    tanggal.after(1000, getDate)
    
#Icon     
imageIcon = PhotoImage(file="task.png") 
window.iconphoto(False,imageIcon)

#Frame Atas
topFrameimage = PhotoImage(file="top ractangle.png") 
Label(window, image=topFrameimage, bg="white").place(x=0, y=0)
dockImage = PhotoImage(file="dock.png")
Label(window, image=dockImage, bg="#F08080").place(x=30, y=25)
dockImage1 = PhotoImage(file="dock1.png")
Label(window, image=dockImage1, bg="#F08080").place(x=640, y=25)
noteImage = PhotoImage(file="task.png")
Label(window, image=noteImage, bg="#F08080").place(x=230, y=18)
header = Label(window, text="TO-DO LIST", font=" arial 20 bold", fg="black", bg="#F08080")
header.place(x=265 ,y=20)
Label(window, text="--- Hallo Guys ---", font="arial 10 bold ", bg="white", fg="#32405b").place(x=300, y=90)
Label(window, text="Yuk Catat Aktivitas Prioritasmu Disini !!", font="arial 10 bold ", bg="white", fg="#32405b").place(x=225, y=110)
Label(window, text="Dan Mulai Lakukan Aktivitasmu 🙌", font="arial 10 bold ", bg="white", fg="#32405b").place(x=237, y=130)
frameDesainSatu = Frame(window, width=275, height=10, bg="#F08080")
frameDesainSatu.place(x=0, y=95)
frameDesainDua = Frame(window, width=275, height=10, bg="#F08080")
frameDesainDua.place(x=429, y=95)

#Frame Tengah
frameTengah = Frame(window, width=700, height=50, bg="white") 
frameTengah.place(x=0, y=165)

#Entry text
task = StringVar() 
entryTask = Entry(frameTengah, width=46, font="arial 15", bd=0)
entryTask.place(x=82, y=10)
entryTask.focus()

#Button untuk menambah list tugas
btn = Button(frameTengah, text="ADD", font="arial 20 bold", width=6, bg="#E6E6FA", fg="black", bd=0, command=addTask) 
btn.place(x=600, y=0)

#Frame List
f1 = Frame(window, bd=3, width=700, height=280, bg="#F08080") 
f1.place(x=0, y=230)
listTask = Listbox(f1, font="arial 12 bold", width=74, height=9, bg="#F08080", fg="black")
listTask.pack(side=LEFT, fill=BOTH, padx=2)

#Scrolling
activationScroolbar = Scrollbar(f1) 
activationScroolbar.pack(side=RIGHT, fill=BOTH)
listTask.config(yscrollcommand=activationScroolbar.set)
activationScroolbar.config(command=listTask.yview)

openFiletask()

#Delete list task
deleteIcon = PhotoImage(file="delete.png") 
Button(window, image=deleteIcon, bd=0, command=deleteTask, bg="white").place(x=3, y=160)

#Frame Bawah
frameBawahSatu = Frame(window, width=340, height=90, bg="#F08080") 
frameBawahSatu.place(x=0, y=439)
Label(frameBawahSatu, text="Tanggal Sekarang :", font="arial 10 bold", bg="#F08080").place(x=106, y=2)
frameBawahDua = Frame(window, width=340, height=90, bg="#F08080")
frameBawahDua.place(x=360, y=439)
frameBawah = Frame(window, width=700, height=40, bg="#F08080")
frameBawah.place(x=0, y=550)
imageCreate = PhotoImage(file="downbar.png")
Label(frameBawah, image=imageCreate, bd=0, bg="#F08080").place(x=0, y=0)

#Label waktu
label = Label(frameBawahDua, font="arial 30", background="#F08080", foreground="black") 
Label(frameBawahDua, text="Waktu Jam Sekarang :", font="arial 10 bold", bg="#F08080").place(x=100, y=2)
label.place(x=55, y=24)

getTime()

#Label Tanggal
dateVar = StringVar()
tanggal = Label(frameBawahSatu, width=10, borderwidth=3,bg="#F08080", font="arial 20 bold", textvariable=dateVar)
tanggal.place(x=80, y=32)

getDate()

#Menampilkan window
window.mainloop() 