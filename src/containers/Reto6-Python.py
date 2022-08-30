def invertir(pal):
    lstPal = []
    for i in range(0,len(pal)):
        lstPal.insert(0, pal[i])    
    pal = ""
    for i in lstPal:
        pal += i
    print(pal)

invertir("Hola mundo")    
