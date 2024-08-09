# UVP_Projektna_Naloga

Opis
Program pridobi podatke o sahistih iz spletne strani fide. Zajame informacijo o imenu in priimku sahista, drzavi, letnici rojstva, spolu, FIDE nazivu in vseh treh rangih. Program ustvari seznam sahistov, ki vsebuje te informacije in ga uredi glede na padajoci standardni rang. Izracunajo in izpisejo se tudi povprecen standardni, pospeseni in hitropotezni rang. Informacije so prikazane  tudi s tremi histograme, ki prikazejo razpored igralcev po vseh treh fide rangih. Prikaze tudi raztreseni diagram korelacije med standardnim rangom in letnico rojstva.

Izvedba
Program je napisan v programskem jeziku Python. Na njem so nalozeni moduli: requests, re, sys in operator.itemgetter.

Navodila za uporabo
Razpon sahistov, ki jih obravnavamo lahko spreminjamo tako, da spreminjamo identifikacijski stevilki ID1 in ID2, med katerima so identifikacijske stevilke sahistov, ki jih analiziramo. Poleg tega lahko spreminjamo tudi ime izhodne datoteke shranjeno v spremenljivki IZHODNA_DATOTEKA. Program najbolje deluje, ce ga zazenemo v okolju jupyter lab. Glavni program, ki pobere podatke in naredi tabelo pozenemo tako, da uvozimo modul fide: import fide. Med izvajanjem program izpise identifikacijsko stevilko sahista, ki ga trenutno obdeluje. Za graficni prikaz podatkov moramo uvoziti modul fide_graf. V tem modulu se nahaja funkcija, ki jo pozenemo tako, da napisemo fide_graf.graf("ime izhodne datoteke").
Program se da zagnati tudi iz ukazne lupine v okolju Linux. Pozenemo ga tako, da napisemo python3 fide.py. Graficno funkcijo pa pozenemo preko nekega drugega programa, ki mora vsebovati import fide_graf in fide_graf.graf("ime izhodne datoteke"). Opomba: V tem primeru je graficen zapis odvisen od konfiguracije sistema.
