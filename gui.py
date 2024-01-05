#=================Module============================
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from data import Database

db = Database('d:/stuff.db')
#==================GUI=============================
win = Tk()
win.geometry('780x450+440+250')
win.resizable(0,0)
win.title('مدیریت کتابخانه')
win.config(bg ='light green')

#================Functions=======================

def populate_list():
    
    list_box.delete(0,END)
    rec = db.select_record()
    # print(rec)
    for row in rec :
        list_box.insert(END, row)
        
def add ():
    # db.insert_table(ent_fname.get() , ent_lname.get() , ent_address.get() , ent_phone.get())
    # clear()
    
    # if name_label.get() == '' or buy_label.get() == '':
    #     messagebox.showinfo('هشدار' , 'لطفا همه فیلدها را پر کنید')
    # else:
        
    db.insert_table(name_entry.get() , buy_entry.get() , sale_entry.get() , num_entry.get())
    clear()
    populate_list()
    
def clear ():
    name_entry.delete(0,END)
    buy_entry.delete(0,END)
    sale_entry.delete(0,END)
    num_entry.delete(0,END)
    
    name_entry.focus_set()

def select_item(event):
    # try:
    global selected_item
    # global index
    index = list_box.curselection()
    selected_item = list_box.get(index)
        # item = lst.split()
    name_entry.delete(0,END)
    name_entry.insert(0 , selected_item[1])
        
    buy_entry.delete(0,END)
    buy_entry.insert(0, selected_item[2])
        
    sale_entry.delete(0,END)
    sale_entry.insert(0 , selected_item[3])
        
    num_entry.delete(0,END)
    num_entry.insert(0 , selected_item[4])
    # except IndexError:
    #     pass

def remove_item():
    
    global selected_item
    index = list_box.curselection()
    selected_item = list_box.get(index)
    x = messagebox.askquestion('هشدار' , 'مورد موردنظر حذف شود؟')
    if x == 'yes':
        db.delete_record(int(selected_item[0]))
        clear()
        populate_list()

def update_item():
    global selected_item
    db.update_records(selected_item[0], name_entry.get() , buy_entry.get() , sale_entry.get() , num_entry.get())
    
    populate_list()
    
    
def search_item():
    
    row = db.search_records(name_entry.get())
    # print(row)
    
    # name_entry.insert(0 , row[1])
    buy_entry.insert(0 ,row[2])
    sale_entry.insert(0 ,row[3])
    num_entry.insert(0 ,row[4])

def close():
    c = messagebox.askquestion('هشدار' , 'آیا برای خروج مطمین هستید ؟')
    if c == 'yes':
        win.destroy()


#==================Widget=======================

#نام کالا
name_label = Label(win , text = 'نام کالا : ' , font= 'arial 15' , bg ='light green' , fg='black')
name_label.place(x=40 , y=10)

name_entry = Entry(win , width=40 )
name_entry.place(x=120 , y=15)

#قیمت خرید
buy_label = Label(win , text='قیمت خرید : ' , font='arial 15' , bg ='light green' , fg='black')
buy_label.place(x=400, y=10)

buy_entry = Entry(win , width=40 ) 
buy_entry.place(x=500 , y=10)

#قیمت فروش
sale_label = Label(win , text='قیمت فروش : ' , font='arial 15' , bg ='light green' , fg='black')
sale_label.place(x=25, y=60)

sale_entry = Entry(win , width=40 ) 
sale_entry.place(x=120 , y=65)


#تعداد
num_label = Label(win , text= 'تعداد : ' , font='arial 15' , bg ='light green' , fg='black')
num_label.place(x=450, y=60)

num_entry = Entry(win , width=40 ) 
num_entry.place(x=500 , y=65)


#BUTTON
add_btn = ttk.Button(win , width=20 , text='اضافه کردن' , command=add )
add_btn.place(x=615, y=150) 

search_btn = ttk.Button(win , width=20 , text='جستجوی کالا' , command=search_item)
search_btn.place(x=615, y=190)

delete_btn = ttk.Button(win , width=20 , text= 'حذف کالا' , command=remove_item)
delete_btn.place(x=615, y=230)

edit_btn = ttk.Button(win , width=20 , text= 'ویرایش' , command=update_item)
edit_btn.place(x=615, y=270)

close_btn = ttk.Button(win , width=20 , text= 'بستن' , command=close)
close_btn.place(x=615, y=310)


#ListBox
list_box = Listbox(win , width=90 , height=18)
list_box.place(x=25 , y=110)

scroll = Scrollbar(win)
scroll.place(x=570 , y=110 , height=292)

list_box.bind('<<ListboxSelect>>' , select_item)

win.mainloop()