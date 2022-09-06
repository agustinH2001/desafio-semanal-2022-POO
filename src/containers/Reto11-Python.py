def check_str(str1, str2):
    out1 = "out1 = "
    out2 = "out2 = "
    for caracter in str1:
        if caracter not in str2:
            out1 += caracter
    for caracter in str2:
        if caracter not in str1:
            out2 += caracter
    print(out1,";", out2)

string1 = "palabra-AEI123"
string2 = "OU456-palabra"
check_str(string1, string2)
