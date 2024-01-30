#matura2014
#A
# def czy_pierwsza(n):
#     if n == 2:
#         return True
#     if n % 2 == 0 or n <= 1:
#         return False
#
#     pierw = int(n**0.5) + 1
#     for dzielnik in range(3, pierw, 2):
#         if n % dzielnik == 0:
#             return False
#     return True
# licznik_pierwszych=0
# liczabaTymczasowa=0
# liczbaASCII=0
wiersze=open('przyklad.txt','r')
tablica=[]
# tablicaASCII=[]
for wiersz in wiersze:
    wiersz=wiersz.strip()
    tablica.append(wiersz)
# for tab in tablica:
#     for litera in tab:
#         liczbaASCII+=ord(litera)
#     tablicaASCII.append(liczbaASCII)
#     liczabaASCII=0
#
#
# for liczby in tablicaASCII:
#     if czy_pierwsza(liczby):
#         licznik_pierwszych=licznik_pierwszych+1
#
# print(licznik_pierwszych)
#B
# licznik=0
# for tab in tablica:
#     for i in range(len(tab)-1):
#         if ord(tab[i])<ord(tab[i+1]):
#             licznik=licznik+1
#             if licznik==len(tab)-2:
#                 print(tab)
#     licznik=0
#C
slownik={}
for tab in tablica:
    slownik[tab]=0

for tab in  tablica:
    if tab:
        slownik[tab]+=1

for i in range(len(slownik.values())):
        print(slownik.keys())


