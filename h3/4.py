spis = []
a = input("Vvedite elementi")
while a:
    spis.append(a)
    a = input()
for i in set(spis):
    print(i, "|", spis.count(i))
