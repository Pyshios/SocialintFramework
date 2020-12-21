def getget():
    import wget
    file = open("rnames.txt","r")
    r = file.readlines()
    tlist = list()
    for i in r:
        tlist.append(i)

    for i in tlist:

        image_filename = wget.download(i)
        print('Image Successfully Downloaded: ', image_filename)