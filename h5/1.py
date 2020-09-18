from collections impotr deque
name = {
    "Akim" : ["Lida", "Sasha"],
    "Lida" : ["Masha", "Daniil"],
    "Masha" : ["Kolya", "Dima", "Vadim"]
}
def doter(x):
    return not len(x) % 2 and x[0] == "D"

a = deque(name["Akim"])
b = []
while name:
    person = a.popleft()
    if person not in b:
        if doter(person):
            print(person)
            break
        else:
            a += name.get(person, [])
        b.append(person)
