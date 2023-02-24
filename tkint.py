from tkinter import *
  
# Create Object
root = Tk()
  
# Set geometry
root.geometry('600x500')
  
# Information List
datas = []

  
# Add Information
def add():
    global datas
    datas.append([Name.get(),Patronymic.get(),Surname.get(),Phone_number.get()])
    update_book()
  
# View Information
def view():
    Name.set(datas[int(select.curselection()[0])][0])
    Patronymic.set(datas[int(select.curselection()[0])][1])
    Surname.set(datas[int(select.curselection()[0])][2])
    Phone_number.set(datas[int(select.curselection()[0])][3])
  
# Delete Information
def delete():
    del datas[int(select.curselection()[0])]
    update_book()
  
def reset():
    Name.set('')
    Patronymic.set('')
    Surname.set('')
    Phone_number.set('')

  
# Update Information
def update_book():
    select.delete(0,END)
    for n in datas:
        select.insert(END, n)
  
# Add Buttons, Label, ListBox
Name = StringVar()
Patronymic = StringVar()
Surname = StringVar()
Phone_number = StringVar()
  
frame = Frame()
frame.pack(pady=10)
  
frame1 = Frame()
frame1.pack()
  
frame2 = Frame()
frame2.pack(pady=10)

frame3 = Frame()
frame3.pack(pady=10)

  
Label(frame, text = 'Name', font='arial 12 bold').pack(side=LEFT)
Entry(frame, textvariable = Name,width=50).pack()

Label(frame1, text = 'Patronymic', font='arial 12 bold').pack(side=LEFT)
Entry(frame1, textvariable = Patronymic,width=50).pack()

Label(frame2, text = 'Surname', font='arial 12 bold').pack(side=LEFT)
Entry(frame2, textvariable = Surname,width=50).pack()
  
Label(frame3, text = 'Phone_number', font='arial 12 bold').pack(side=LEFT)
Entry(frame3, textvariable = Phone_number,width=50).pack()
  
  
Button(root,text="Add",font="arial 12 bold",command=add).place(x= 100, y=270)
Button(root,text="View",font="arial 12 bold",command=view).place(x= 100, y=310)
Button(root,text="Delete",font="arial 12 bold",command=delete).place(x= 100, y=350)
Button(root,text="Reset",font="arial 12 bold",command=reset).place(x= 100, y=390)
  
scroll_bar = Scrollbar(root, orient=VERTICAL)
select = Listbox(root, width=50, yscrollcommand=scroll_bar.set, height=12)
scroll_bar.config (command=select.yview)
scroll_bar.pack(side=RIGHT, fill=Y)
select.place(x=200,y=260)

  
# Execute Tkinter
root.mainloop() 

