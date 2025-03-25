cislo_jedna= int (input("zadejte prvni cislo"))
cislo_dva= int (input("zadejte druhé číslo"))

opakovat = "ano"
while opakovat == "ano":
    operace = input ("zadejte cislo co chcete opakovat")

if operace == "sčítání":
    výsledek = cislo_jedna + cislo_dva
    print (výsledek)
elif operace == "odčítání":
    výsledek = cislo_jedna - cislo_dva
    print (výsledek)
elif operace == "násobení":
    výsledek = cislo_jedna * cislo_dva
    print (výsledek)
elif operace == "dělení":
    výsledek = cislo_jedna / cislo_dva
    print (výsledek)
else:
    print ("tahle možnost neexistuje")

opakovat = input ("chceš program opakovat?")