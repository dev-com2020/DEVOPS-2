osoby = [1, 2, 3, 4, 5, 'tomek']

print("to jest lista", osoby)


if osoby:
    print("lista jest ok")

if not osoby:
    print("lista nie jest ok")

for i in range(5):
    osoby.append(i)
