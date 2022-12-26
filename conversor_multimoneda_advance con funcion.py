def conversor(tipo_nemo, valor_de_galletas):
    micas = float(input ("cuantas " + tipo_nemo + "tienes?: "))
    valor_de_galletas = micas/ valor_de_galletas
    valor_de_galletas = round (valor_de_galletas, 2 )
    valor_de_galletas= str (valor_de_galletas)
    print( "tienes: " + valor_de_galletas + " galletas ")


menu = """""
Bienvenido al conversor de monedas 

1- micas
2- kennets
3- chungaletas
4- ahabs

Elige una opcion: """

opcion = input (menu)

if opcion == "1":
    conversor("micas ", 7500)

elif  opcion == "2":
    conversor("kennets ", 9500)
elif opcion == "3":
    conversor("chungaletas ", 5500)
elif opcion == "4":
    conversor("ahabs ", 10500)
else:
    print ("ingresa una opcion correcta por favor: ")




