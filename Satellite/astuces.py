#!/usr/bin/python3.5
""" Fonction qui reçoit un flottant en argument et qui renvoit 
un nombre formater (avec un point à devant chaque triplé et une 
virgule séparant partie décimale et partie entière) """

def formater_nombre(nombre, apres_virgule):
    nombre = str(nombre)
    partie_entiere, partie_decimale = nombre.split(".")
        
    if len(partie_entiere) > 3:    
        new_nombre = ""
        nombre = ""
        i = len(partie_entiere) - 1
        
        while i >= 0:
            new_nombre += partie_entiere[i]
            i -= 1
                
        i += 1

        while i <= len(partie_entiere) - 1 :

            if (i%3) == 0 and i != 0:
                nombre = new_nombre[i] + "." + nombre   
                i += 1 
            else:
                nombre = new_nombre[i] + nombre
                i += 1       
            
        nombre += "," + partie_decimale[:apres_virgule]
    else:
        nombre = partie_entiere + "," + partie_decimale[:apres_virgule]

    return nombre 