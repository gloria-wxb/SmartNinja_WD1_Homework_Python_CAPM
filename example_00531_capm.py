import math

#coding=utf-8
#Implementiere einen Rentenrechner
#Anfangskapital: 100
#Zinsen: 6%
#Laufzeit: Jahre
#Formel für die Zinseszinsrechnung: Anfangskapital * ((1+(Zinsatz/100)) ^ jeweiligen Jahre)
#Anfangskapital*math.pow(Zinsen,1)

anfangskapital = 100
zins = 6.0
laufzeit = 5

for jahr in range(1, laufzeit + 1):
    print('Kapital im Jahr', jahr, ':', anfangskapital * math.pow((1+(zins/100)), jahr))

"""
Ergebnis:
Anfangskapital:  100
Zinssatz:  6.0
Veranlagungszeitraum:  5
Kapital im Jahr 1 : 106.0
Kapital im Jahr 2 : 112.36
Kapital im Jahr 3 : 119.1016
Kapital im Jahr 4 : 126.247696
Kapital im Jahr 5 : 133.82255776
"""


