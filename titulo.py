# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 09:34:50 2023

@author: Alumno
"""

# Importamos la libreria
import camelcase

nombre = "Pascacio Sanchez Roxana Gadita"

print(nombre.upper())
print(nombre.title())


#Creamos un objeto llamado cam
cam = camelcase.CamelCase()
print("Con camelcase....")

# imprimimos el nombre en formato título
# utilizamos camelcase
print(cam.hump(nombre))

# Para resolver el problema
# creamos otro objeto llamado cam2
# al definir el objeto, incluimos los argumentos
# 'flor' y 'león' 
cam2 = camelcase.CamelCase('Pascacio','Gadita')
print(cam2.hump(nombre))
