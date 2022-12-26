menu = """""
Bienvenido al conversor de monedas 

1- micas
2- kennets
3- chungaletas
4- ahabs

Elige una opcion: """

opcion = input (menu)

if opcion == "1":
    micas = float(input ("cuantas Micas tienes: "))
    valor_de_galletas = 7500
    valor_de_galletas = micas / valor_de_galletas
    valor_de_galletas = round (valor_de_galletas, 2 )
    valor_de_galletas= str (valor_de_galletas)
    print( "tienes: " + valor_de_galletas + " galletas ")

elif  opcion == "2":
    kennets = float(input ("cuantas kennets tienes: "))
    valor_de_galletas = 7500
    valor_de_galletas = kennets / valor_de_galletas
    valor_de_galletas = round (valor_de_galletas,2 )
    valor_de_galletas =str (valor_de_galletas)
    print ( "tienes: " + valor_de_galletas + " galletas " )
elif opcion == "3":
    chungaletas = float(input ("cuantas chungaletas tienes: "))
    valor_de_galletas = 7500
    valor_de_galletas = chungaletas / valor_de_galletas
    valor_de_galletas = round ( valor_de_galletas,2 )
    valor_de_galletas = str (valor_de_galletas)
    print( "tienes: " +  valor_de_galletas + " galletas " )    
elif opcion == "4":
    ahabs = float(input ("cuantas ahabs tienes: "))
    valor_de_galletas = 7500
    valor_de_galletas = ahabs / valor_de_galletas
    valor_de_galletas = round (valor_de_galletas,2 )
    valor_de_galletas = str ( valor_de_galletas)
    print( "tienes: " + valor_de_galletas + " galletas " )
else:
    print ("ingresa una opcion correcta por favor: ")




