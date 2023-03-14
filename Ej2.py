from tkinter import *
from tkinter import ttk
import tkinter as ttk

raiz=Tk()
raiz.title("Ejercicio 2")
raiz.geometry("700x600")

#---------------Variables---------------

IDprod = int()
Name = StringVar()
Desc = StringVar()
Quant = int()
Price = int()

#---------------Frame principal---------------
principal=ttk.Frame(raiz,width=600, height=200, bg="black")
principal.grid()

#---------------Frame imagen---------------
Fimg=ttk.Frame(principal,bg="gray40")
Fimg.grid(column=0,row=0)

img = PhotoImage(file="car.png")
etqImagen = ttk.Label(Fimg,bg="gray40")
etqImagen.grid(column=0,row=0,sticky=(W))
etqImagen['image'] = img

#Texto

Timg=ttk.Label(Fimg,text="Product management    ", font=("Arial", 30 , "bold"),foreground="white",bg="gray40").grid(column=1,row=0,sticky=(W))
ttk.Label(Fimg,text="                               ",bg="gray40").grid(column=2,row=0)

#---------------Frame Contenido---------------
contF=ttk.Frame(principal,width=50,height=40,bg="#482525")
contF.grid(column=0,row=2, pady=5, padx=10)

ttk.Label(contF,text="________________", font="Arial", foreground="white",background="#482525").grid(column=1,row=1,sticky=(S),padx=10)
IDprodlbl=ttk.Label(contF,text="Id Product:",font=("Arial",10,"bold"),foreground="white" ,bg="#482525").grid(column=0,row=1,sticky=(W),padx=5)
IDprodEnt=ttk.Entry(contF,width= 20,textvariable=IDprod,bg="#482525",foreground="white", font="Italica",justify=CENTER)
IDprodEnt.grid(column=1,row=1,padx=50,sticky=(N,W))
IDprodEnt.config(borderwidth=0)

ttk.Label(contF,text="________________", font="Arial", foreground="white",background="#482525").grid(column=1,row=2,sticky=(S),padx=10)
Namlbl=ttk.Label(contF,text="Name:",font=("Arial",10,"bold"),foreground="white" ,bg="#482525").grid(column=0,row=2,sticky=(W),padx=5)
NamEnt=ttk.Entry(contF,width= 20,textvariable=IDprod,bg="#482525",foreground="white",font="Italica",justify=CENTER)
NamEnt.grid(column=1,row=2,padx=50,sticky=(N,W))
NamEnt.config(borderwidth=0)

ttk.Label(contF,text="________________", font="Arial", foreground="white",background="#482525").grid(column=1,row=3,sticky=(S),padx=10)
Desclbl=ttk.Label(contF,text="Description:",font=("Arial",10,"bold"),foreground="white" ,bg="#482525").grid(column=0,row=3,sticky=(W),padx=5)
DescEnt=ttk.Entry(contF,width= 20,textvariable=IDprod,bg="#482525",foreground="white",font="Italica",justify=CENTER)
DescEnt.grid(column=1,row=3,padx=50,sticky=(N,W))
DescEnt.config(borderwidth=0)

ttk.Label(contF,text="________________", font="Arial", foreground="white",background="#482525").grid(column=1,row=4,sticky=(S),padx=10)
Quantlbl=ttk.Label(contF,text="Quantity:",font=("Arial",10,"bold"),foreground="white" ,bg="#482525").grid(column=0,row=4,sticky=(W),padx=5)
QuantEnt=ttk.Entry(contF,width= 20,textvariable=IDprod,bg="#482525",foreground="white",font="Italica",justify=CENTER)
QuantEnt.grid(column=1,row=4,padx=50,sticky=(N,W))
QuantEnt.config(borderwidth=0)

ttk.Label(contF,text="________________", font="Arial", foreground="white",background="#482525").grid(column=1,row=5,sticky=(S),padx=10)
Pricelbl=ttk.Label(contF,text="Price:",font=("Arial",10,"bold"),foreground="white" ,bg="#482525").grid(column=0,row=5,sticky=(W),padx=5)
PriceEnt=ttk.Entry(contF,width= 20,textvariable=IDprod,bg="#482525",foreground="white",font="Italica",justify=CENTER)
PriceEnt.grid(column=1,row=5,padx=50,sticky=(N,W))
PriceEnt.config(borderwidth=0)

#Botones

espacio=ttk.Label(contF,text="      ",background="#482525").grid(column=2,row=0)
imglupa = PhotoImage(file="lup.png",width=30,height=30)

btnlupa=ttk.Button(contF,background="#482525",activebackground="#482525")
btnlupa.grid(column=2,row=0,pady=5)
btnlupa.config(borderwidth=0)
btnlupa['image'] = imglupa

imgbroch = PhotoImage(file="Limpiar.png",width=30,height=30)
btnbroc=ttk.Button(contF,background="#482525",activebackground="#482525")
btnbroc.grid(column=3,row=0,sticky=(W),padx=5,pady=5)
btnbroc.config(borderwidth=0)
btnbroc['image'] = imgbroch

btnBack = ttk.Button(contF,text="Back",font=("Arial",10,"bold"),background="#482525",activebackground="#482525",foreground="SlateBlue2")
btnBack.grid(column=3,row=0,padx=80)
btnBack.config(borderwidth=0)
btnSave = ttk.Button(contF,text="Save",background="green3",width=15,foreground="white",font=("Arial",10,"bold"),activebackground="green4",anchor="center").grid(column=3,row=2,sticky=(W)) 
btnDel = ttk.Button(contF,text="Delete",background="red2",width=15,foreground="white",font=("Arial",10,"bold"),activebackground="red3").grid(column=3,row=3,sticky=(W))
btnUpd = ttk.Button(contF,text="Update",background="chocolate2",width=15,foreground="white",font=("Arial",10,"bold"),activebackground="chocolate3").grid(column=3,row=4,sticky=(W))

#---------------Frame Tabla---------------
TablaF = ttk.Frame(contF,width=20,height=20)
TablaF.grid(column=0,row=6,columnspan=5,pady=30)


# Crear encabezado de la tabla
ttk.Label(TablaF, text="ID", width=10, bg="gray", fg="white").grid(row=0, column=0)
ttk.Label(TablaF, text="Nombre", width=20, bg="gray", fg="white").grid(row=0, column=1)
ttk.Label(TablaF, text="Descripción", width=30, bg="gray", fg="white").grid(row=0, column=2)
ttk.Label(TablaF, text="Cantidad", width=10, bg="gray", fg="white").grid(row=0, column=3)
ttk.Label(TablaF, text="Precio", width=10, bg="gray", fg="white").grid(row=0, column=4)

# Crear datos de la tabla
data = [
    ("1", "Producto 1", "Descripción del producto 1", "10", "$100"),
    ("2", "Producto 2", "Descripción del producto 2", "5", "$50"),
    ("3", "Producto 3", "Descripción del producto 3", "20", "$200")
]

# Mostrar datos en la tabla
for i, row in enumerate(data):
    for j, item in enumerate(row):
        ttk.Label(TablaF, text=item, width=10 if j == 0 else 20 if j == 1 else 30 if j == 2 else 10 if j == 3 else 10, bg="white").grid(row=i+1, column=j)




raiz.mainloop()