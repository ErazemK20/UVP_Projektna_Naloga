"""#!/usr/bin/env python3""" #Samostojno poganjanje programa


""" Program iz spletnih strani mednarodne sahovske zveze FIDE zajame podatke o
igralcih z identifikacijskimi steviklami med ID1 in ID2. Slovenske igralce s 
koncnim standardnim (pocasnim) rangom razvrsti v urejen seznam, ki ga izpise na
zaslon in v datoteko tako, da poda rang, ime, priimek, letnico rojstva ter 
(morebitni) sahovski naziv. Izracuna in izpise tudi povprecen rang."""

import requests
import re
import sys
from operator import itemgetter

ID1=14627500 # Zaprt interval  obravnavanih
ID2=14629500 # identifikacijskih stevilk
IZHODNA_DATOTEKA="seznam.txt" # Ime izhodne datoteke

ROOT_URL="https://ratings.fide.com/profile/" # URL izhodiscne spletne strani

NE_OBSTAJA_REGEX=r'No record found'  # Potrebni regularni...
DRZAVA_REGEX=r'<div class="profile-top-info__block__row__header">Federation:</div>\n\s+ <div class="profile-top-info__block__row__data">(?P<drzava>[a-zA-Z\s]+)</div>'
IME_PRIIMEK_REGEX=r'<title>(?P<priimek>[a-zA-Z]+), (?P<ime>[a-zA-Z]+)</title>'
LETO_ROJSTVA_REGEX=r'<div class="profile-top-info__block__row__header">B-Year:</div>\n\s+<div class="profile-top-info__block__row__data">(?P<leto>[\d]+)</div>'
SPOL_REGEX=r'<div class="profile-top-info__block__row__header">Sex:</div>\n\s+<div class="profile-top-info__block__row__data">(?P<spol>[a-zA-Z]+)</div>'
NAZIV_REGEX=r' <div class="profile-top-info__block__row__header">FIDE title:</div>\n\s+ <div class="profile-top-info__block__row__data">(?P<naziv>[a-zA-Z\s]+)</div>'
STANDARDNI_REGEX=r'<span class="profile-top-rating-dataDesc">std</span>\n\s+(?P<standardni>\d+)'
POSPESENI_REGEX=r'<span class="profile-top-rating-dataDesc">rapid</span>\n\s+(?P<pospeseni>\d+)'
HITROPOTEZNI_REGEX=r'<span class="profile-top-rating-dataDesc">blitz</span>\n\s+(?P<hitropotezni>\d+)'                     # ...izrazi za iskanje v datotekah tipa html   



seznam=[]  # Seznam (pod)seznamov
for i in range(ID1,ID2+1):
   url=ROOT_URL+str(i) # vsaki identifikacijski stevilki pripada locena spletna stran
   resp=requests.get(url) # zajem ustrezne datoteke html
   m=re.search(NE_OBSTAJA_REGEX,resp.text)
   if not m: # vsak element iz [ID1,ID2] ni identifikacijska stevilka
      print("\rZajemam podatke za FIDE ID: {}".format(i),end='')# Zajem je pocasen...
      sys.stdout.flush()

      n=re.search(DRZAVA_REGEX,resp.text) # Informacija o drzavi
      if n != None:
         drzava=n.group('drzava')
      else: 
         drzava=''

      n=re.search(IME_PRIIMEK_REGEX,resp.text) # Informacija o imenu in priimku
      if n != None:
         ime=n.group('ime')
         priimek=n.group('priimek')
      else: 
         ime=''
         priimek=''

      n=re.search(LETO_ROJSTVA_REGEX,resp.text) # Informacija o letnici rojstva
      if n != None:
         leto=n.group('leto') 
      else: leto=''

      n=re.search(SPOL_REGEX,resp.text) # Informacija o spolu 
      if n != None:
         spol = "Moski" if n.group('spol') == "Male" else "Zenska"
      else: spol=''

      n=re.search(NAZIV_REGEX,resp.text) # Informacija o nazivu FIDE
      if n != None:
         if n.group('naziv') == "FIDE Master":
            naziv="Mojster FIDE"
         elif n.group('naziv') == "International Master":
            naziv="Mednarodni mojster"
         elif n.group('naziv') == "Grandmaster":
            naziv="Velemojster"
         elif n.group('naziv') == "Woman FIDE Master":
            naziv="Mojstrica FIDE"
         elif n.group('naziv') == "Woman International Master":
            naziv="Mednarodna mojstrica"
         elif n.group('naziv') == "Woman Grandmaster":
            naziv="Velemojstrica"
         else:
            naziv=''
      else: naziv='' 

      n=re.search(STANDARDNI_REGEX,resp.text) # Informacija o standardnem rangu
      if n != None:
         standardni=n.group('standardni')
      else: standardni = '' 
      n=re.search(POSPESENI_REGEX,resp.text) # Informacija o pospesenem rangu
      if n != None:
         pospeseni=n.group('pospeseni')
      else: pospeseni = '' 

      n=re.search(HITROPOTEZNI_REGEX,resp.text) # Informacija o hitropoteznem rangu
      if n != None:
         hitropotezni=n.group('hitropotezni')
      else: hitropotezni = '' 
     
      sahist=[i,drzava,ime,priimek,leto,spol,naziv,standardni,pospeseni,hitropotezni]
      if(drzava=="Slovenia" and standardni!=""): # Podseznam za slovenskega sahista
         seznam.append(sahist)                   # uvrstimo v glavni seznam

urejen_seznam=sorted(seznam,key=itemgetter(7),reverse=True) # Seznam uredimo glede na
print ()                                                    # standardni rang

standard_povprecje=0   # Za dolocanje povprecenga standardnega ranga

f=open(IZHODNA_DATOTEKA,'w') # Odpri izhodno datoteko za izpis
for sahist in urejen_seznam:
   print (sahist[7],sahist[2],sahist[3],",","roj.",sahist[4],",",sahist[6])
   standard_povprecje+=int(sahist[7])
   vrstica=str(sahist[7])+" "+str(sahist[2])+" "+str(sahist[3])+" "+str(sahist[4])+" "+str(sahist[6]+"\n")
   f.write(vrstica)

f.close()

standard_povprecje/=len(urejen_seznam)
print ("Povprecen standardni rang: ",int(standard_povprecje))
      
