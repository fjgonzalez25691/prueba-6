import ficheros
import fun_crear_txt
import time

#Ejecutamos verificar_fichero del módulo ficheros para descargar los ficheros Json de la web
#y trabajar local
ficheros.verificar_fichero()


#Mostramos el menú principal por pantalla


salir = False
while not salir:
        print('''
            Listado de clubes por liga
            ==========================
            1) Liga Española.
            2) Liga Alemana.
            3) Liga Italiana.
            4) Liga Austriaca.
            5) Liga Inglesa.
            6) Salir ''')       
                       
        opcion = input('Elija una liga: ')
        if opcion == '1':
                liga = "liga_espanola"
        elif opcion == '2':
             liga = "liga_alemana"
        elif opcion == '3':
                liga = "liga_italiana"
        elif opcion == '4':
                liga = "liga_austriaca"

        elif opcion == '5':
                liga = "liga_inglesa"
        elif opcion == '6':
                
                salir = True
                print("¡Hasta luego!")                
                time.sleep(1)
                break
        else:
               print("Debe elegir una opción entre el 1 y 6")
               time.sleep(2)
#una vez elegida la opción, ejecutamos la función que nos lleva al submenú
        try:
            fun_crear_txt.menu_liga(liga)
        except TypeError:
            print("Debe de elegir un número del 1 al 6")
            time.sleep(2)
        except NameError:
             continue

        
