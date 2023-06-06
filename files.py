"""fajl = open("lorem.txt", mode="r")
tekst = fajl.readlines()
print(tekst[1])
fajl.close()"""
# read -> celiot tekst
# readline -> eden red / so sekoe naredno povtoruvanje sleden red
# readlines -> lista od redovi


# w - write -> brise sto imalo vo fajlot i zapisuva novi podatoci
# a - append -> dodava tekst vo vekepostoecki fajl

"""fajl = open("lorem.txt", mode="w")
fajl.write("Nov Tekst - Stariot e izbrisan")
fajl.close()"""

"""fajl = open("lorem.txt", mode="a")
fajl.write("\nNov Tekst - Dodaden na stariot, ne izbrisan tekst")
fajl.close()"""

"""import os

os.remove("lorem.txt")"""

