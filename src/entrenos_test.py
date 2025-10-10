from entrenos import *
from datetime import datetime


if __name__ == "__main__":
    datos = lee_entrenos(ruta_csv)
    print(f"Se han leido {len(datos)} datos.")
    print("Mostrando los 3 primeros registros:")
    for dato in datos[:3]:
        print(dato)
        
    print("Mostrando los 3 ultimo registros:")
    for dato in datos[-3:]:
        print(dato)
    
    #EJERCICIO 1
    tipo_entreno = tipos_entreno(datos)
    print(f"Estos son todos los tipos de entreno: {tipo_entreno}")
    
    #EJERCICIO 2
    d = int(input("Entrenos con una duracion superior a: "))
    entrenos_duracion_superior(datos, d)
    
    #EJERCICIO 3
    f_inicio = input("Introduzca una fecha de inicio (dd/mm/YYYY): ")
    f_fin = input("Introduzca una fecha de fin (dd/mm/YYYY): ")
    fecha_inicio = datetime.strptime(f_inicio, "%d/%m/%Y").date()
    fecha_fin = datetime.strptime(f_fin, "%d/%m/%Y").date()
    suma_calorias(datos, fecha_inicio, fecha_fin)
    
    #EJERCICIO 4
    entrenamiento_mas_kms(datos)
    
    #EJERCICIO 5
    ano = int(input("Introduzca un año: "))
    mes = int(input("Introduzca un mes: "))
    media = duracion_media_entrenos(datos, ano, mes)
    print(f"Duracion media del entrenamiento ese mes: {media}")