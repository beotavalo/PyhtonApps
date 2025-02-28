# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 09:10:20 2023

@author: braul
"""
# Importamos toda la libreria Tkinter y Math
from tkinter import *
from math import *

#Funciones
#Para visualizar pantalla
def btnClick(num):
    global operador
    operador = operador + str(num)
    input_text.set(operador)
 
#CÁLCULO Y MUESTRA DE RESULTADOS.
def resultado():
    global operador
    try:
        opera =str (eval(operador))
        input_text.set(opera)
    except:
        input_text.set("ERROR")
    operador = ""
 
#LIMPIEZA DE PANTALLA.
def clear():
    global operador
    operador=("")
    input_text.set("0")
    


#Variables para las dimensiones de los botones

ab = 11 
hb = 3

#Creamos la raiz de nuestra app
root = Tk()

#Titulo de la ventana 

root.title("MY CALC")

#Asignamos un icono para la app
root.iconbitmap('python_logo_icon.ico')

#Activamos remidens=cionamento de ventana
root.resizable(0,0)

#Define size of the window
root.geometry('392x560')

#Definimos color de fondo y botones
root.configure(background = 'SkyBlue4')
color_boton = ('gray77')



#Variables para la funcion de entrada btnClick    
input_text=StringVar()   
operador = "" 

    
#Defino el display de salida de datos de la calculadora
salida = Entry(root, font = ('arial',20,'bold'), width = 22, textvariable=input_text, bd = 20, insertwidth = 4, bg= 'powder blue', justify = 'right').place(x=10, y = 60)


#Definimos los botones de los digitos
Button(root, text = 'C', bg = color_boton, width = ab, height = hb, command = clear).place(x = 17, y = 180)
Button(root, text = 'ln', bg = color_boton, width = ab, height = hb, command = lambda:btnClick('log')).place(x = 107, y = 180)
Button(root, text = 'Exp', bg = color_boton, width = ab, height = hb, command = lambda:btnClick('**')).place(x = 197, y = 180)
Button(root, text = '=', bg = color_boton, width = ab, height = hb, command=resultado).place(x = 287, y = 180)
#segunda fila
Button(root, text = '7', bg = color_boton, width = ab, height = hb, command = lambda:btnClick(7)).place(x = 17, y = 240)
Button(root, text = '8', bg = color_boton, width = ab, height = hb, command = lambda:btnClick(8)).place(x = 107, y = 240)
Button(root, text = '9', bg = color_boton, width = ab, height = hb, command = lambda:btnClick(9)).place(x = 197, y = 240)
Button(root, text = '+', bg = color_boton,  width = ab, height = hb, command = lambda:btnClick('+')).place(x =287, y = 240)
#tercera fila
Button(root, text = '4', bg = color_boton, width = ab, height = hb, command = lambda:btnClick(4)).place(x = 17, y = 300)
Button(root, text = '5', bg = color_boton, width = ab, height = hb, command = lambda:btnClick(5)).place(x = 107, y = 300)
Button(root, text = '6', bg = color_boton, width = ab, height = hb, command = lambda:btnClick(6)).place(x = 197, y = 300)
Button(root, text = '-', bg = color_boton, width = ab, height = hb, command = lambda:btnClick('-')).place(x = 287, y = 300)
#cuarta fila
Button(root, text = '1', bg = color_boton, width = ab, height = hb, command = lambda:btnClick(1)).place(x = 17, y = 360) 
Button(root, text = '2', bg = color_boton, width = ab, height = hb, command = lambda:btnClick(2)).place(x = 107, y = 360)
Button(root, text = '3', bg = color_boton, width = ab, height = hb, command = lambda:btnClick(3)).place(x = 197, y = 360)
Button(root, text = 'x', bg = color_boton, width = ab, height = hb, command = lambda:btnClick('*')).place(x = 287, y = 360)
#quinta fila
Button(root, text = 'π', bg = color_boton, width = ab, height = hb, command = lambda:btnClick('pi')).place(x = 17, y = 420)
Button(root, text = '0', bg = color_boton, width = ab, height = hb, command = lambda:btnClick(0)).place(x = 107, y = 420)
Button(root, text = '.', bg = color_boton, width = ab, height = hb, command = lambda:btnClick('.')).place(x = 197, y = 420)
Button(root, text = '/', bg = color_boton, width = ab, height = hb, command = lambda:btnClick('/')).place(x = 287, y = 420)
#sexta fila
Button(root, text = '(', bg = color_boton, width = ab, height = hb, command = lambda:btnClick('(')).place(x = 17, y = 480)
Button(root, text = ')', bg = color_boton, width = ab, height = hb, command = lambda:btnClick(')')).place(x = 107, y = 480)
Button(root, text = 'sqrt', bg = color_boton, width = ab, height = hb, command = lambda:btnClick('sqrt')).place(x = 197, y = 480)
Button(root, text = '%', bg = color_boton, width = ab, height = hb, command = lambda:btnClick('%')).place(x = 287, y = 480)


clear()

#Ejecutamos un bucle infinito
root.mainloop()