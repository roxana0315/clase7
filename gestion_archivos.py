# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 09:54:14 2023

@author: Alumno
"""
import os

def crear_archivo(nombre, contenido):
    contenido = "Línea1 hola amigos comonido a Ñaña."
    nombre="roxana.txt"
    archivo = open(nombre,"wt")
    archivo.write(contenido)
    archivo.close()

def eliminar_archivo(nombre):
    os.remove(nombre)

def agregar_contenido_archivo(nombre, contenido):
    archivo = open(nombre,"at")
    archivo.write("\nroxana pacacio sanchez " + contenido)
    archivo.close()

def leer_archivo(nombre):
    archivo = open(nombre,"rt",encoding='utf8')
    contenido = archivo.read()
    return contenido

