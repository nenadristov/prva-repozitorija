
try:
    broj = int(input("Vnesete broj: "))
    print(broj)

    lista =[]
    print(lista[5])
except ValueError:
    print("Vnesovte string")
except SyntaxError:
    print("Ima greska vo sintaksata")
except IndexError:
    print("Element so toj index ne postoi")

    

