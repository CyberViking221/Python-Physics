#!/usr/bin/python3.5

#importations des modules#
from math import *
from planete.terre import *
from astuces import *

#définition des fonctions#
carre = lambda x: x*x

def vitesse():
	V = sqrt((K*M)/r)
	return V

def periode():
	T = (2*pi*r)/V
	return T

def go():
	go = (K*M)/carre(R)
	return go

def F():
	F = (K*M*m)/carre(r)
	return F

def isGeostationer():
	if h > 36e6 or h < 30e6:
		return False
	else:
		return True

#recupération des données#
h = float(input("Entrer l'altidude h du satellite : "))
m = float(input("Entrer la masse du satellite : "))

##########calculs#########
r = R + h
F = F()
V = vitesse()
T = periode()
go = go()
geoStat = isGeostationer()

#########résultats########

print("#####################################################################################")
print("### Vitesse v = ", formater_nombre(V, 3), "m/s" )
print("### période T = ", formater_nombre(T, 3), "s")
print("### go = ", formater_nombre(go, 1), "N/Kg")
print("### F = ", formater_nombre(F, 3), "N")

if geoStat:
	print("### Ce satellite est géostationnaire .")
else:
	print("### Ce satellite n'est pas géostationnaire.")
