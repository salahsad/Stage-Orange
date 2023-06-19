from tkinter import *

fenetre = Tk()
fenetre.geometry("500x500")
fenetre.title("saisi DIS")
fenetre["bg"] ='orange'
label = Label(fenetre,text="SAISI DIS",bg="orange" ,font=("Courier_New",20,"bold")).place(x="180" ,y="20")

var1 = StringVar()
var2 = StringVar()
var3=StringVar()
label = Label(fenetre,text="Saisir equipement",font=("Verdana",12),bg="orange").place(x="30",y="170")
entree1 = Entry(fenetre,textvariable=var1,width=40).place(x="200",y="170")
label1 = Label(fenetre,text="Saisir site",font=("Verdana",12,),bg="orange").place(x="30",y="200")
entree2 = Entry(fenetre,textvariable=var2,width=40).place(x="200",y="200")
label2 = Label(fenetre,text="Saisir topologie",font=("Verdana",12),bg="orange").place(x="30",y="230")
entree3 = Entry(fenetre,textvariable=var3,width=40).place(x="200",y="230")
fenetre.resizable(height=False,width=False)

my_list = []
def function():
    equipement = var1.get()
    site = var2.get()
    topologie= var3.get()
    my_list.append(equipement)
    my_list.append(site)
    my_list.append(topologie)
    var1.set('')
    var2.set('')
    var3.set('')
    print (my_list)

envoyer = Button(fenetre,text="envoyer!",bg="white",font=("Verdana",12,"bold"),command=function
,activebackground="green"
).place(x="200",y="370")

fenetre.mainloop()

print(my_list)

