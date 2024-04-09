from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from utilNotas import *
#VARIABLES GLOBALES
estudiantes=[
    "1714616123#Santiago#Mosquera#10#2.6#8.5#0#0",
    "0814616123#Santiago#Ramos#9.5#2.6#8.5#1#15.1",
    "1614616123#Maritza#Ramos#8.3#2.6#7.2#2#23.1"
]


#messagebox.showinfo(title="", message="")
def fnBuscar():
    estudianteEncontrado=buscarEstudiante(txtCedula.get(),estudiantes)
    if estudianteEncontrado == None:
        messagebox.showwarning(title="IMPORTANTE", message="No existe el estudiante")
    else:
        partesEstudiante=estudianteEncontrado.split("#")
        limpiar()
        txtCedula.insert(0,partesEstudiante[0])
        txtNombre.insert(0,partesEstudiante[1])
        txtApellido.insert(0,partesEstudiante[2])
        txtNota1.insert(0,partesEstudiante[3])
        txtNota2.insert(0,partesEstudiante[4])
        txtNota3.insert(0,partesEstudiante[5])
        inasistencias = partesEstudiante[6]
        total = partesEstudiante[7]
        messagebox.showinfo(title="Estudiante Encontrado", message=f"Inasistencias: {inasistencias} Total: {total}")

def fnObtenerEntero(txtInfo, lblError, desde, hasta):
    valorEntero = None
    try:
        valorEntero = int(txtInfo.get())
        if hasta!=None:
            if valorEntero >= desde and valorEntero <= hasta:
                lblError.config(text="")
                return valorEntero
            else:
                lblError.config(text=f"Debe ingresar un valor entre {desde} y {hasta}")
        else:
            if valorEntero >= desde:
                lblError.config(text="")
                return valorEntero
            else:
                lblError.config(text=f"Debe ingresar un valor mayor o igual a {desde}")
    except:
        lblError.config(text="Debe ingresar un número entero")
    return valorEntero

def obtenerCadena(txtInfo,lblError,minimo):
    valor=txtInfo.get()
    if len(valor)>=minimo:
        lblError.config(text="")
        return valor
    else:
        lblError.config(text=f"Debe ingresar al menos {minimo} caracteres")
        return None
    
def fnObtenerFloat(txtInfo,lblError,desde,hasta=None):
    valorFloat=None
    
    try:
        valorFloat=float(txtInfo.get())
        if valorFloat>=desde and valorFloat<=hasta:
            lblError.config(text="")
            return valorFloat
        else:
            lblError.config(text=f"Debe ingresar un valor entre {desde} and {hasta}")
    except:
        lblError.config(text="Debe ingresar un número")
    return valorFloat
#FUNCIONES
def fnGuardar():
    cedula=obtenerCadena(txtCedula,lblErrorCedula,10)
    nombre=obtenerCadena(txtNombre,lblErrorNombre,3)
    apellido=obtenerCadena(txtApellido,lblErrorApellido,3)
    nota1=fnObtenerFloat(txtNota1,lblErrorNota1,0,10)
    nota2=fnObtenerFloat(txtNota2,lblErrorNota2,0,10)
    nota3=fnObtenerFloat(txtNota3,lblErrorNota3,0,10)
    estEncontrado=buscarEstudiante(cedula,estudiantes)
    inasistencias = fnObtenerEntero(txtInasistencias, lblErrorInasistencias, 0,20)

    if cedula!=None and nombre!= None and apellido!=None and nota1!= None and nota2!=None and nota3!= None and inasistencias!=None:
        total = calcularTotal(nota1, nota2, nota3, inasistencias)
        lblTotal.config(text=str(total))
        estEncontrado = buscarEstudiante(cedula, estudiantes)
        datosEstudiante=f"{cedula}#{nombre}#{apellido}#{nota1}#{nota2}#{nota3}#{inasistencias}#{total}"
        if estEncontrado == None: #no existe en la lista
            estudiantes.append(datosEstudiante)
            messagebox.showinfo(title="IMPORTANTE", message="Estudiante Guardado")
        else:
                messagebox.showwarning(title="IMPORTANTE", message=f"Ya existe el estudiante con la cédula {cedula}")
    else:
        messagebox.showwarning(title="ERROR", message="No se pudo guardar. Verifique los datos ingresados.")
    print(estudiantes)
             
    
def limpiar():
    txtCedula.delete(0,END)
    txtNombre.delete(0,END)
    txtApellido.delete(0,END)
    txtNota1.delete(0,END)
    txtNota2.delete(0,END)
    txtNota3.delete(0,END)
    txtInasistencias.delete(0, END)
    lblTotal.config(text="0.00")

def fnNuevo():
    limpiar()

#GRAFICA
ventana=Tk()
ventana.title("NOTAS")
ventana.geometry("600x400")
tabControl=ttk.Notebook(ventana)
tab1=ttk.Frame(tabControl)
tab2=ttk.Frame(tabControl)
tab3=ttk.Frame(tabControl)
tabControl.add(tab1,text="REGISTRO")
tabControl.add(tab2,text="LISTA")
tabControl.add(tab3,text="BUSQUEDA")
tabControl.pack(expand = 1, fill ="both") 
#TAB REGISTRO
frRegistro= Frame(tab1)
frRegistro.place(x=100,y=100)
lblCedula=ttk.Label(frRegistro,text="CEDULA:")
lblNombre=ttk.Label(frRegistro,text="NOMBRE:")
lblApellido=ttk.Label(frRegistro,text="APELLIDO:")
lblNota1=ttk.Label(frRegistro,text="NOTA 1:")
lblNota2=ttk.Label(frRegistro,text="NOTA 2:")
lblNota3=ttk.Label(frRegistro,text="NOTA 3:")
lblInsasistencias=ttk.Label(frRegistro,text="INASISTENCIAS:")
lblTituloPromedio=ttk.Label(frRegistro,text="PROMEDIO:")
lblTotal=ttk.Label(frRegistro,text="0.00",foreground="blue")

txtCedula=ttk.Entry(frRegistro)
txtNombre=ttk.Entry(frRegistro)
txtApellido=ttk.Entry(frRegistro)
txtNota1=ttk.Entry(frRegistro)
txtNota2=ttk.Entry(frRegistro)
txtNota3=ttk.Entry(frRegistro)
txtInasistencias=ttk.Entry(frRegistro)
lblErrorCedula=ttk.Label(frRegistro,text="",foreground="red")
lblErrorNombre=ttk.Label(frRegistro,text="",foreground="red")
lblErrorApellido=ttk.Label(frRegistro,text="",foreground="red")
lblErrorNota1=ttk.Label(frRegistro,text="",foreground="red")
lblErrorNota2=ttk.Label(frRegistro,text="",foreground="red")
lblErrorNota3=ttk.Label(frRegistro,text="",foreground="red")
lblErrorInasistencias=ttk.Label(frRegistro,text="",foreground="red")
frBotones=Frame(frRegistro)
btnGuardar=ttk.Button(frBotones,text="GUARDAR",width=20,command=fnGuardar)
btnNuevo=ttk.Button(frBotones,text="NUEVO",width=20,command=fnNuevo)
btnBuscar=ttk.Button(frBotones,text="BUSCAR",width=20,command=fnBuscar)
btnGuardar.grid(row=0,column=0,padx=10)
btnNuevo.grid(row=0,column=1,padx=10)
btnBuscar.grid(row=0,column=2,padx=10)

lblCedula.grid(row=2,column=1,padx=30)
txtCedula.grid(row=2,column=2,pady=2)
lblErrorCedula.grid(row=2,column=3)
lblNombre.grid(row=3,column=1,pady=2)
txtNombre.grid(row=3,column=2)
lblErrorNombre.grid(row=3,column=3)
lblApellido.grid(row=4,column=1,pady=2)
txtApellido.grid(row=4,column=2)
lblErrorApellido.grid(row=4,column=3)
lblNota1.grid(row=5,column=1,pady=2)
lblErrorApellido.grid(row=4,column=3)
txtNota1.grid(row=5,column=2)
lblErrorNota1.grid(row=5,column=3)
lblNota2.grid(row=6,column=1,pady=2)
txtNota2.grid(row=6,column=2)
lblErrorNota2.grid(row=6,column=3)
lblNota3.grid(row=7,column=1,pady=2)
txtNota3.grid(row=7,column=2)
lblErrorNota3.grid(row=7,column=3)
lblInsasistencias.grid(row=8,column=1)
txtInasistencias.grid(row=8,column=2)
lblErrorInasistencias.grid(row=8,column=3)
lblTituloPromedio.grid(row=9,column=1)
lblTotal.grid(row=9,column=2)
frBotones.grid(row=10,column=0,columnspan=4,pady=10)

ventana.mainloop()


