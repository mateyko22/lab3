# Zad1
# a = [1-x for x in range(1, 11)]
# print(a)
# b = [4**y for y in range(8)]
# print(b)
# c = [x for x in b if x % 2 == 0]
# print(c)

# Zad2
# lista1 = []
# for x in range(11):
#     los = randint(1, 25)
#     lista1.append(los)
#
# print("lista1:", lista1)
# lista2 = [x for x in lista1 if x % 2 == 0]
# print("Tylko parzyste elementy:", lista2)

# Zad3
# produkty = {"mieso": "kg", "chipsy": "sztuki", "przyprawy": "sztuki", "pieczywo": "sztuki", "napoje": "sztuki",
#             "sery": "kg", "cukierki": "kg", "owoce": "kg", "cukier": "sztuki"}
# print(produkty)
# lista = {key for key, value in produkty.items() if value == "sztuki"}
# print(lista)

# Zad4
# def prostok(a,b,c):
#     if a*a+b*b==c*c or a*a+c*c==b*b or b*b+c*c==a*a:
#         print("Trojkat jest prostokatny")
#     else:
#         print("Trojkat nie jest prostokatny")
#
# prostok(3,4,5)
# prostok(1,2,3)
# prostok(4,3,5)
# prostok(12,23,34)

# Zad5
# def trapez(a=12, b=2, h=12):
#     return (a + b) * h / 2
#
# print(trapez())
# print(trapez(1, 2, 3))
# print(trapez(10, 5, 8))

# Zad6
# def ciag(a1=1, b=4, ile=10):
#     iloczyn = 1
#     for x in range(ile):
#         iloczyn *= a1 * b
#     return iloczyn
#
# print(ciag())
# print(ciag(ile=3))
# print(ciag(2,3,3))

# Zad8
# def zakupy(**produkt):
#     suma = 0
#     for x in produkt:
#         suma += 1
#     print(produkt)
#     print("Suma produktow:", suma)
#     return sum(produkt.values())
#
#
# print(zakupy(czekolada=2.50, mleko=3, chleb=2.7, woda=0.99, piwo=2.89, kielbasa=12.99))
