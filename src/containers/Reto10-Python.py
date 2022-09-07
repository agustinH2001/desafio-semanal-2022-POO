import re

def morse(texto):
    texto = str(texto)
    texto = texto.upper()
    es_morse = True
    cifrado = ""
    citext = ""
    codigo_morse = { 'A':'.-', 'B':'-...','C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....','I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.','O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-','U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..','1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....','7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-','?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}
    for i in texto:
        if i != "." and i != "-" and i != " ":
            es_morse = False
    if es_morse:
        texto += " "
        for x in texto:
            if (x != " "):
                i = 0
                citext += x
            else:
                i += 1
                if i == 2 :
                    cifrado += " "
                else:
                    cifrado += list(codigo_morse.keys())[list(codigo_morse.values()).index(citext)]
                    citext = ""
    else:
        for i in texto:
                if i != " ":
                    cifrado += codigo_morse[i] + " "
                else:
                    cifrado += " "
    print(cifrado)

morse("Buenas noches")
morse("-... ..- . -. .- ...  - .- .-. -.. . ...") #buenas tardes
    