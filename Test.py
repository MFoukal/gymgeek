nakup = []

for i in range(10):
    nakup.append(input("prvek "+str(i)+": "))

print("Běž na nákup")

print(">>>OBCHOD<<<")

for i in range(len(nakup)):
    zbozi = input("> ")

    if zbozi in nakup:
        print("OK")
        nakup.remove(zbozi)

    else:
        print("neee")

if len(nakup) > 0:
    print("nekoupil jsi: "),
for nekoupene_zbozi in nakup:
    print(str(nekoupene_zbozi))
