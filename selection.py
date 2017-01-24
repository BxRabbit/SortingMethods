#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from tkinter import *
import tkSimpleDialog


def select():
	datos = int(entrynumeros.get())
	vector = []

	for i in range(0,datos):
		dialog = tkSimpleDialog.askinteger("","Ingresa el numero")
		vector.append(dialog)

	aux_impresion1 = str(vector)
	Label2.config(text=aux_impresion1)

	for i in range(0,len(vector)-1):
		aux = i
		for j in range(i+1,len(vector)):
			if vector[j] < vector[aux]:
				aux = j

		aux2 = vector[aux]
		vector[aux] = vector[i]
		vector[i] = aux2

	aux_impresion2 = str(vector)
	label3.config(text=aux_impresion2)

app = Tk()
app.title("Selection Sort")
app.configure(bg = 'SkyBlue2')

Label1 = Label(app, text="Cuantos numeros vas a ingresar?",font='Helvetica 12', bg = 'SkyBlue2')
Label1.pack()

datos = 0
entrynumeros = Entry(app, width=8, textvariable=datos)
entrynumeros.pack()

button1 = Button(app, text="Ok!", command=select)
button1.pack(pady=(10,0))

Label2 = Label(app, text="",bg = 'SkyBlue2')
Label2.pack(pady=(10,0))

label3 = Label(app, text="",bg = 'SkyBlue2')
label3.pack(pady=(10,0))

app.mainloop()