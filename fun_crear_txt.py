import json, os, time


def menu_liga(liga):
    fichero = open (liga+".json", "r", encoding="utf-8")
    data = json.load(fichero)
    nom_liga =liga.replace("_", " ")
    print("La {} tiene {} equipos".format(nom_liga, len(data["clubs"])))
    time.sleep(1)
    salir = False
    while not salir:
        print('''¿Qué desea hacer?
                1) Crear fichero con los equipos de la liga.
                2) Mostrar los equipos por pantalla.
                3) Salir.''')
        opcion= input("Eliga una opción del menú anterior:")
        try:
            if opcion == "1":
                crear_txt(liga)
            elif opcion == "2":
                mostrar_pantalla(liga)
            elif opcion == "3":
                salir == True
                ("Volvemos al menú principal")
                break
            else:
                print("Debe de elegir una opción entre el 1 y el 3")
                time.sleep(1)
        except TypeError:
            print("Debe de elegir un número del 1 al 3")
            time.sleep(1)
        except NameError:
            continue

    fichero.close()


def crear_txt(liga):

    fichero_txt = open(liga+".txt", "w", encoding="utf-8")
    with open(liga+".json", encoding="utf-8") as fichero:
            data = json.load(fichero)
            fichero_txt.writelines("         {}\n".format(data["name"]))
            fichero_txt.writelines("="*35 + "\n")
            for equipo in data["clubs"]:
                fichero_txt.writelines("{:<25} {:<5}{} \n".format(equipo["name"],  str(equipo["code"]),  equipo["country"]))
    
    fichero_txt.close()    
    if os.path.isfile(liga+".txt"):
        print("El fichero {}.txt se ha creado correctamente".format(liga))
    else:
        print("Error al crear el fichero")


def mostrar_pantalla(liga):
    with open(liga+".json", encoding="utf-8") as fichero:
        data = json.load(fichero)
        print("\n LIGA: {}\n".format(data["name"]))
        print("="*40 + "\n")
        for equipo in data["clubs"]:     
            print("{:<25} {:<7}{:.5} \n".format(equipo["name"],  str(equipo["code"]),  equipo["country"]))   
    time.sleep(2)
