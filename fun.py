from tkinter import *
from tkinter import messagebox

window = Tk()
window.title('Login Screen')
window.geometry('400x150')

l1=Label(window,text='Username:',font=(10)) 
l2=Label(window,text='Password:',font=(10))
l1.grid(row=0,column=0,padx=5,pady=5)
l2.grid(row=1,column=0,padx=5,pady=5)

username=StringVar()
password=StringVar()
t1=Entry(window,textvariable=username,font=(10))
t2=Entry(window,textvariable=password,font=(10),show='*')
t1.grid(row=0,column=1)
t2.grid(row=1,column=1)

def login():
    if username.get()=='admin' and password.get()=='admin':
        
        status=messagebox.askyesno(title='Login status', message='Are You Dumb.\n have 6 attempt only')
        if status==True:
            messagebox.showinfo(title='befool',message='I knew it! Love you 3000')
        else:
            messagebox.askyesno(title='Login status', message='Are You Dumb.\n have 5 attempt only')

            status=messagebox.askyesno(title='Login status', message='Are You Dumb.\n have 4 attempt only')
        if status==True:
           self.tk.call('destroy', self._w)
        else:
            messagebox.askyesno(title='Login status', message='Are You Dumb.\n have 3 attempt only')
            status=messagebox.askyesno(title='Login status', message='Are You Dumb.\n have 2 attempt only')
        if status==True:
            self.tk.call('destroy', self._w)
        else:
            messagebox.askyesno(title='Login status', message='Are You Dumb.\n have 1 attempt only')
            
            
    else:
        messagebox.showerror(title='Login Error', message='Username/Password is incorrect.')

b1=Button(window,command=login,text='Login',font=(10))

def cancel():
    status=messagebox.askyesno(title='Warning',message='Do you want yo close the window?')
    if status==True:
        window.destroy()
    else:
        messagebox.showwarning(title='Warning',message='Try again!')
b2=Button(window,command=cancel,text='Cancel',font=(10))
b1.grid(row=2,column=1,sticky=W)
b2.grid(row=2,column=1,sticky=E)

window.mainloop()
