from laptop_busines import Laptop_Business
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import random
class App :
    def __init__(self,root):
        self.root=root
        self.laptops=[]
        self.imagenes=[r"C:\Users\CLEAR MINDS\Desktop\kevin\modulo5\retos\r8\IMG/1.jpeg",
        r"C:\Users\CLEAR MINDS\Desktop\kevin\modulo5\retos\r8\IMG/2.jpg",
        r"C:\Users\CLEAR MINDS\Desktop\kevin\modulo5\retos\r8\IMG/3.jpg",
        r"C:\Users\CLEAR MINDS\Desktop\kevin\modulo5\retos\r8\IMG/4.jpg",
        r"C:\Users\CLEAR MINDS\Desktop\kevin\modulo5\retos\r8\IMG/5.jpeg",]
        root.title("ingresas datos")
        self.setup_ui()
        pass 

       
       

    def setup_ui(self):
        ttk.Label(self.root,text="marca").grid(row=0,column=0)
        self.marca=tk.StringVar()
        ttk.Entry(self.root,textvariable=self.marca).grid(row=0,column=1)
        
        ttk.Label(self.root,text="procesador").grid(row=1,column=0)
        self.procesador=tk.StringVar()
        ttk.Entry(self.root,textvariable=self.procesador).grid(row=1,column=1)
        
        ttk.Label(self.root,text="Memoria").grid(row=2,column=0)
        self.memoria=tk.StringVar()
        ttk.Entry(self.root,textvariable=self.memoria).grid(row=2,column=1)
        
        ttk.Label(self.root,text="disco ").grid(row=3,column=0)
        self.disco=tk.StringVar()
        ttk.Entry(self.root,textvariable=self.disco).grid(row=3,column=1)  
              
        ttk.Label(self.root,text="Duracion Bateria ").grid(row=4,column=0)
        self.bateria=tk.StringVar()
        ttk.Entry(self.root,textvariable=self.bateria).grid(row=4,column=1) 
         
        ttk.Label(self.root,text="precio").grid(row=5,column=0)
        self.precio=tk.StringVar()
        ttk.Entry(self.root,textvariable=self.precio).grid(row=5,column=1)   
        
        ttk.Button(self.root,text="agregar laptop",command=self.agregar).grid(row=5,column=0)

        self.mostrar_Laptop=tk.Text(self.root,height=10,width=50)
        self.mostrar_Laptop.grid(column=0,row=6,columnspan=2)
        self.canva=tk.Canvas(self.root,width=200,height=200)
        self.canva.grid(column=3,row=1,rowspan=6)
    def agregar(self):
        nueva_laptop=Laptop_Business(self.marca.get(),self.procesador.get(),self.memoria.get(),
                                   self.disco.get(),self.bateria.get(),self.precio.get())
        self.laptops.append(nueva_laptop)
        print(self.laptops[0])
        self.mostrar_Laptop.insert(tk.END,f"{nueva_laptop}")
        self.mostrar_img_aleatoria()
        
    def mostrar_img_aleatoria(self):
        imagen_path=random.choice(self.imagenes)
        imagen=Image.open(imagen_path)
        imagen=imagen.resize((200,200),Image.Resampling.LANCZOS)
        photo=ImageTk.PhotoImage(imagen)
        self.canva.create_image(0,0,anchor=tk.NW,image=photo)
        self.canva.image=photo
        pass    
root=tk.Tk()
app=App(root)
root.mainloop()