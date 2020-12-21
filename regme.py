def regme():
    import re
    import io


    #All list being openned for search for paterns
    allwords = list()
    go = io.open("google.txt", "r" , encoding="utf8")
    gof = go.read()
    ya = io.open("yandex.txt" , "r" , encoding="utf8")
    yaf = ya.read()
    us = io.open("usr.txt" , "r" , encoding="utf8")
    usf = us.read()
    # All Reg Ex patterns that i will use
    #facebook
    face1 = '(?:https?:)?\/\/(?:www\.)?(?:facebook|fb)\.com\/(?P<profile>(?![A-z]+\.php)(?!marketplace|gaming|watch|me|messages|help|search|groups)[A-z0-9_\-\.]+)\/?'
    #facebook id
    face2 = '(?:https?:)?\/\/(?:www\.)facebook.com/(?:profile.php\?id=)?(?P<id>[0-9]+)'
    #Instagram
    ig1 = '(?:https?:)?\/\/(?:www\.)?(?:instagram\.com|instagr\.am)\/(?P<username>[A-Za-z0-9_](?:(?:[A-Za-z0-9_]|(?:\.(?!\.))){0,28}(?:[A-Za-z0-9_]))?)'
    #Phone number
    ph1 = '(?:tel|phone|mobile):(?P<number>\+?[0-9. -]+)'
    emaill = '(?P<email>[A-z0-9_.+-]+@[A-z0-9_.-]+\.[A-z]+)'
    #Linkdin
    link = "(?:https?:)?\/\/(?:[\w]+\.)?linkedin\.com\/in\/(?P<permalink>[\w\-\_À-ÿ%]+)\/?"

    finallist = gof.split() + yaf.split() + usf.split()
    ffcomb = open("mixw.txt" , "a" , encoding="utf8")
    finaldocumet = open("fdocument.txt" , "a" , encoding="utf8")
    for i in finallist:

        ffcomb.write(i)

    ffcomb.close()


    for all in finallist:
        if(re.search(face1 , all)):
            allwords.append(all)
            print("The follow info was found:" + all)
        elif(re.search(face2 , all)):
            allwords.append(all)
            print("The follow info was found:" + all)
        elif(re.search(ig1 ,all)):
            allwords.append(all)
            print("The follow info was found:" + all)
        elif(re.search(ph1, all)):
            allwords.append(all)
            print("The follow info was found:" + all)
        elif(re.search(emaill, all)):
            allwords.append(all)
            print("The follow info was found:" + all)
        elif(re.search(link ,all)):
            allwords.append(all)
        else:
            continue

    for i in allwords:
        finaldocumet.write(i)
    finaldocumet.close()

    print("ALL RELEVANT INFO WAS SAVED AT FDOCUMENT.TXT")