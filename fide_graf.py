""" Vhodni parameter je datoteka, ustvarjena z glavnim programom fide.py iz katere se 
zajamejo podatki o standardnih rangih in letnicah sahistov. Porazdelitev po rangih se
graficno prikaze s histogramom, korelacija med letnico rojstva in rangom pa z raztresenim
diagramom"""

import re
import matplotlib.pyplot as plt
import numpy as np

N=10 #Stevilo stolpcev

seznam=[]
letnice=[]
def graf(datoteka):
   try:                                   #Odpiranje datoteke, ustvarjene s fide.py
      f=open(datoteka,'r')
   except FileNotFoundError: 
      print("Datoteka {}  ne obstaja".format(datoteka))
      return None
       
   podatki=f.readlines()                  #Branje iz datoteke
   for vrstica in podatki:
      m=re.search("(?P<rang>\d+)[a-zA-Z\s]+(?P<leto>\d+)",vrstica)
      if m != None:                       #Podatki vsebujejo rang in letnico rojstva
         rang=m.group('rang')
         leto=m.group('leto')
         seznam.append(int(rang))
         letnice.append(int(leto))
   f.close()                              #Zapiranje datoteke

   urejen_seznam=sorted(seznam)           #Narascajoci rangi

   sp=min(urejen_seznam)
   zg=max(urejen_seznam)

   plt.title("Porazdelitev standardnih rangov")                       #Risanje histograma
   plt.xlabel("Rang")
   plt.ylabel("Stevilo igralcev")
   plt.hist(urejen_seznam,bins=N,color='skyblue',edgecolor='black')
   plt.xticks(np.arange(sp,zg+1,int((zg-sp)/N)))
   plt.show()

   plt.title("Korelacija med standardnim rangom in letnico rojstva")  #Risanje raztresenega diagrama
   plt.xlabel("Letnica rojstva")
   plt.ylabel("Rang")
   plt.scatter(letnice,seznam)
   plt.show()
