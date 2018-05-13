from tkinter import*
bgclr="#282828"
fgclr="#cecece"
clr='#004a95'

data  = {}

def getdata():
    data['usuario'] = user_Entry.get()
    data['contraseña'] = password_Entry.get()
    data['destino'] = tuser_Entry.get()
    w.destroy()

w=Tk()
w.title("InstaScrap")
w.geometry("450x350")
w.config(bg=bgclr)

user=Label(w,text="Usuario",font=("blod",15),bg=bgclr,fg=fgclr)
user.place(x=20,y=30)

user_Entry=Entry(w,bg=bgclr,fg="white",relief=GROOVE,highlightcolor="white",highlightthickness=2,highlightbackground=clr,
                 width=40,
                 font=10,
                 bd=5)
user_Entry.place(x=20,y=70)

passwordl=Label(w,text="Contraseña",font=("blod",15),bg=bgclr,fg=fgclr)
passwordl.place(x=20,y=110)

password_Entry=Entry(w,bg=bgclr,fg="white",relief=GROOVE,highlightcolor="white",highlightthickness=2,highlightbackground=clr,
                     width=40,
                     font=10,
                     show="*",
                     bd=5)
password_Entry.place(x=20,y=150)

tuser=Label(w,text="Perfil Destino",font=("blod",15),bg=bgclr,fg=fgclr)
tuser.place(x=20,y=190)

tuser_Entry=Entry(w,bg=bgclr,fg="white",relief=GROOVE,highlightcolor="white",highlightthickness=2,highlightbackground=clr,
                  width=40,
                  font=10,
                  bd=5)
tuser_Entry.place(x=20,y=230)

button=Button(w,text="Login",bg=clr,fg="white",relief=GROOVE,highlightcolor=clr,highlightthickness=4,width=40,font=10,
              command = getdata)
button.place(x=20,y=280)

w.mainloop()





