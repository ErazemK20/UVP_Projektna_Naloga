""" Vhodni parameter je datoteka, ustvarjena z glavnim programom fide.py iz katere se 
zajamejo podatki o standardnih rangih in letnicah sahistov. Porazdelitev po rangih se
graficno prikaze s histogramom, korelacija med letnico rojstva in rangom pa z raztresenim
diagramom"""

import re
import matplotlib.pyplot as plt
import numpy as np

N = 10 #Stevilo stolpcev

seznam = []
seznamp = []
seznamh = []
letnice = []
def graf(datoteka):
   try:                                   #Odpiranje datoteke, ustvarjene s fide.py
      f = open(datoteka, 'r')
   except FileNotFoundError: 
      print("Datoteka {}  ne obstaja".format(datoteka))
      return None
       
   podatki = f.readlines()                  #Branje iz datoteke
   for vrstica in podatki:
      m = re.search("(?P<rang>\d+)\s+(?P<rangp>\d+)\s+(?P<rangh>\d+)\s+[a-zA-Z\s]+(?P<leto>\d+)", vrstica)
      if m != None:                       #Podatki vsebujejo rang, pospeseni rang, hitropotezni rang in letnico rojstva
         rang = m.group('rang')
         rangp = m.group('rangp')
         rangh = m.group('rangh')
         leto = m.group('leto')
         seznam.append(int(rang))
         seznamp.append(int(rangp))
         seznamh.append(int(rangh))
         letnice.append(int(leto))
   f.close()                              #Zapiranje datoteke

   urejen_seznam = sorted(seznam)           #Narascajoci rangi
   urejen_seznamp = sorted(seznamp)
   urejen_seznamh = sorted(seznamh)

   sp = min(urejen_seznam)
   zg = max(urejen_seznam)
    
   spp = min(urejen_seznamp)
   zgp = max(urejen_seznamp)

   sph = min(urejen_seznamh)
   zgh = max(urejen_seznamh)

   plt.title("Porazdelitev standardnih rangov")                       #Risanje histogramov
   plt.xlabel("Rang")
   plt.ylabel("Stevilo igralcev")
   plt.hist(urejen_seznam, bins = N, color = 'skyblue', edgecolor = 'black')
   plt.xticks(np.arange(sp, zg + 1, int((zg - sp) / N)))
   plt.show()

   plt.title("Porazdelitev pospesenih rangov")
   plt.xlabel("Rang")
   plt.ylabel("Stevilo igralcev")
   plt.hist(urejen_seznamp, bins = N, color = 'skyblue', edgecolor = 'black')
   plt.xticks(np.arange(spp, zgp + 1, int((zgp - spp) / N)))
   plt.show()

   plt.title("Porazdelitev hitropoteznih rangov")
   plt.xlabel("Rang")
   plt.ylabel("Stevilo igralcev")
   plt.hist(urejen_seznamh, bins = N, color = 'skyblue', edgecolor = 'black')
   plt.xticks(np.arange(sph, zgh + 1, int((zgh - sph) / N)))
   plt.show()

   plt.title("Korelacija med standardnim rangom in letnico rojstva")  #Risanje raztresenega diagrama
   plt.xlabel("Letnica rojstva")
   plt.ylabel("Rang")
   plt.scatter(letnice, seznam)
   plt.show() 
