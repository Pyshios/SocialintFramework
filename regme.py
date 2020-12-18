import re
allwords = list()
go = open("google.txt", "r" , encoding="utf8")
gof = go.read()
ya = open("yandex.txt" , "r" , encoding="utf8")
yaf = ya.read()
us = open("usr.txt" , "r" , encoding="utf8")
usf = us.read()

finallist = gof.split() + yaf.split() + usf.split()
ffcomb = open("mixw.txt" , "a")
finaldocumet =
for i in finallist:

    ffcomb.write(i)
    ffcomb.close()



for all in finallist:
