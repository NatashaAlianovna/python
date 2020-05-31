#Licence: GPL 3.0
# Menu creation
# Lenguage spanish
# NatashaAlianovna
import requests
import sys
from pathlib import Path
from bitcoin import *
import codecs
import os
cmd = "rename.bat"

while True:
    print ("Bienvenido al Menu")
    print ("1 - Buscar un address")
    print ("2 - Borrar un address")
    print ("3 - Ordenar lista")
    print ("4 - Balance")
    print ("5-  Check EXA")
    print ("6 - Exit")

    opcion = input("Ingrese una Opcion:")

    if opcion == ("1"):
        addr = input("Ingrese una direccion:")
        print ("Buscando el Address")
        compare = lambda addr: [x for x in Path("lista.txt").read_text().split("\n") if x == addr]
        if (compare(addr)) != ([]):
            print(addr)
            print ("exito")
        else:
            print ("Address no encontrada")
            opcion1 = input(" Desea agregar dirección? S/N")
            if opcion1 ==("S") or opcion1 == ("s"):
                    f3 = open ('lista.txt','a')
                    f3.write(addr)
                    f3.write("\n")
                    f3.close()
                    print ("Address guardada")
            else:
                break
            if opcion1 == ("N") or opcion1 == ("n"):
                break
    
    if opcion == ("3"):
        print ("Ordenando archivo lista.txt")
        with open ('lista.txt','r') as f:
            linea = [line.strip() for line in f]
            r = sorted(linea)
            r1 = (str(r)+'\n')
            f.close()
            f1 = open ('lista2.txt','a')
            listToStr = ' '.join(r)
            espacio = listToStr.replace(" ", "\n")
            f1.write(espacio)
            f1.write("\n")
            f1.close()
            print ("Borre archivo lista.txt manualmente")
    if opcion == ("4"):
        addr = input("Ingrese una direccion:")
        print ("Buscando balance")
        valid_address = (addr)
        x = (history(valid_address))
        print (x)
    if opcion == ("5"):
        var1 = input("Ingresa HEXADECIMAL ")
        def create_addr():
            priv = codecs.encode(var1).decode()
            pub = privtopub(priv)
            addr = pubtoaddr(pub)
            return addr, priv
        for a in range(1):
            addr,priv = create_addr()
            valid_address = (addr)
            x = (history(valid_address))
        if len(x) == 0:
            print("0")
            print (addr)
        else:
            print (x)
            print (addr, priv)   
        
    if opcion == ("6"):
        break
    if opcion == ("2"):
        addr = input("Ingrese una direccion para borrar:")
        print ("Buscando el Address")
        compare = lambda addr: [x for x in Path("lista.txt").read_text().split("\n") if x == addr]
        if (compare(addr)) != ([]):
            with open ('lista.txt','r') as f:
                linea = [line.strip() for line in f]
                linea.remove(addr)
                r = sorted(linea)
                r1 = (str(r)+'\n')
                f.close()
                f1 = open ('lista2.txt','w')
                listToStr = ' '.join(r)
                espacio = listToStr.replace(" ", "\n")
                f1.write(espacio)
                f1.write("\n")
                f1.close()

            print ("Ordenando archivo lista2.txt")
            with open ('lista2.txt','r') as f:
                linea = [line.strip() for line in f]
                r = sorted(linea)
                r1 = (str(r)+'\n')
                f.close()
                f1 = open ('lista2.txt','w')
                listToStr = ' '.join(r)
                espacio = listToStr.replace(" ", "\n")
                f1.write(espacio)
                f1.write("\n")
                f1.close()
                print(addr)
                print ("Borrada")
                os.system(cmd)        
