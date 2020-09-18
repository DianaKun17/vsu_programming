k = int(input("Vvedite nomer elementa chislovoi posledovatel'nocti Finobachchci ")
a = [0,1]
for i in range(k - 2):
    a.append(a[-1] + a[-2])
print(a)
