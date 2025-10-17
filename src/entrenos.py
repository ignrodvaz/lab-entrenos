import csv
from collections import namedtuple
from datetime import datetime

entreno = namedtuple(
    'Entreno',
    'tipo, fechahora, ubicacion, duracion, calorias, distancia, frecuencia, compartido'
)

ruta_csv = './data/entrenos.csv'

def lee_entrenos(ruta_csv):
    with open(ruta_csv, encoding="utf-8") as f:
        lector = csv.reader(f)
        next(lector)
        lista_entrenos = []
        for tipo, fechahora, ubicacion, duracion, calorias, distancia, frecuencia, compartido in lector:
            fechahora = datetime.strptime(fechahora, "%d/%m/%Y %H:%M").date()
            duracion = int(duracion)
            calorias = int(calorias)
            distancia = float(distancia)
            frecuencia = int(frecuencia)
            if compartido == "s":
                True
            else:
                False
            entrenos = entreno(tipo, fechahora, ubicacion, duracion, calorias, distancia, frecuencia, compartido)
            lista_entrenos.append(entrenos)
    
    return lista_entrenos

def tipos_entreno(lista_entrenos):
    tipos = {entreno[0] for entreno in lista_entrenos}
    return sorted(tipos)

def entrenos_duracion_superior(lista_entrenos, d):
    entreno_con_duracion_d = []
    for entreno in lista_entrenos:
        if entreno[3] > d:
            entreno_con_duracion_d.append(entreno)
            
    return print(entreno_con_duracion_d)

def suma_calorias(lista_entrenos, f_inicio, f_fin):
    calorias_quemadas = 0
    for entreno in lista_entrenos:
        if  f_inicio <= entreno[1] <= f_fin:
            calorias_quemadas += entreno[4]
    return print(f"Calorias quemadas entre las fechas introducidas: {calorias_quemadas}")
    
def entrenamiento_mas_kms(lista_entrenos):
    lista_mas_kms = lista_entrenos[0]
    for entreno in lista_entrenos:
        if entreno[5] > lista_mas_kms[5]:
            lista_mas_kms = entreno
        else:
            lista_mas_kms = lista_mas_kms
    return print("El entrenamiento con mayor kilometraje: ", lista_mas_kms)

def duracion_media_entrenos(lista_entrenos, ano, mes):
    duracion_total = 0
    total_entrenamientos = 0
    for entreno in lista_entrenos:
        fecha_entreno = entreno[1]
        if fecha_entreno.year == ano and fecha_entreno.month == mes:
            duracion_total += entreno[3]
            total_entrenamientos += 1
    if total_entrenamientos == 0:
        return None
    
    return duracion_total/total_entrenamientos

# if __name__ == "__main__":
#     datos = lee_entrenos(ruta_csv)
#     print(f"Se han leido {len(datos)} datos.")
#     print("Mostrando los 3 primeros registros:")
#     for dato in datos[:3]:
#         print(dato)
        
#     print("Mostrando los 3 ultimo registros:")
#     for dato in datos[-3:]:
#         print(dato)