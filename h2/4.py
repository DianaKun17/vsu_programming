def fun(a):
    ot = a.count('(')
    za = a.count(')')
    if ot > za:
        retunt "Dopishite", ot - za, "zakrivaushih skobok"
    elif ot < za:
        retunt "Dopishite", za - ot, "otkrivaushih skobok"
    return "vse skobki na meste"
    
print(fun(input("Vvedite stroky: ")
