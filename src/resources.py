# Definir un conjunto de elementos representados por símbolos químicos
arrayp = {'H', 'S', 'Fe', 'Fe'}  # Conjunto de elementos químicos con dos Fe, uno S, y uno H

# Calcular el total de elementos en el conjunto
total_elements = len(arrayp)

# Crear un diccionario para contar cuántas veces aparece cada elemento
element_counts = {}

# Recorrer cada elemento en el conjunto para contar su ocurrencia
for element in arrayp:
    if element in element_counts:
        element_counts[element] += 1  # Si el elemento ya está en el diccionario, incrementar su contador
    else:
        element_counts[element] = 1  # Si es la primera vez que se encuentra el elemento, añadirlo al diccionario

# Calcular el porcentaje de composición de cada elemento y almacenarlo en variables
Fe_percentage = (element_counts.get('Fe', 0) / total_elements) * 100  # Porcentaje de hierro (Fe)
S_percentage = (element_counts.get('S', 0) / total_elements) * 100    # Porcentaje de azufre (S)
H_percentage = (element_counts.get('H', 0) / total_elements) * 100    # Porcentaje de hidrógeno (H)
N_percentage = (element_counts.get('N', 0) / total_elements) * 100    # Porcentaje de nitrógeno (N), aunque no está en el conjunto

# Contar cada elemento individualmente
Fe_count = element_counts.get('Fe', 0)  # Número de átomos de hierro
S_count = element_counts.get('S', 0)    # Número de átomos de azufre
H_count = element_counts.get('H', 0)    # Número de átomos de hidrógeno
C_count = element_counts.get('C', 0)    # Número de átomos de carbono, aunque no está en el conjunto

# Inicializar el pH
ph = 7  # Valor inicial de pH neutro

# Lógica basada en las proporciones de elementos para determinar el pH
if Fe_percentage == 50 and S_percentage == 50:
    ph = 7  # Si hay 50% de hierro y 50% de azufre, el pH se mantiene en 7 (neutro)
elif Fe_percentage < 10 and S_percentage < 10:
    ph = 7  # Si los porcentajes de hierro y azufre son menores al 10%, el pH es 7 (neutro)
    if H_percentage > 50:
        ph = 5  # Si además el porcentaje de hidrógeno es mayor al 50%, el pH baja a 5 (ácido)
else:
    if Fe_percentage > 40:
        ph = 9  # Si el porcentaje de hierro es mayor al 40%, el pH sube a 9 (básico)
        if Fe_percentage > 60:
            ph = 11  # Si el porcentaje de hierro supera el 60%, el pH sube a 11
            if Fe_percentage > 90:
                ph = 14  # Si el porcentaje de hierro es mayor al 90%, el pH alcanza un valor extremo de 14 (muy básico)
    
    if S_percentage > 40:
        ph = 5  # Si el porcentaje de azufre es mayor al 40%, el pH baja a 5 (ácido)
        if S_percentage > 60:
            ph = 3  # Si el porcentaje de azufre supera el 60%, el pH baja a 3
            if S_percentage > 90:
                ph = 1  # Si el porcentaje de azufre es mayor al 90%, el pH llega a 1 (muy ácido, inviable para la vida)

# Bloquear avance de habilidades (probablemente relacionado con algún sistema del juego)

# Importar librerías necesarias
import json
import ast
from collections import Counter

# Cargar combinaciones posibles desde un archivo JSON llamado 'Combinaciones.json'
with open('Combinaciones.json', 'r', encoding='utf-8') as file:
    combinaciones = json.load(file)

# Función para transformar las claves del diccionario (convertir strings en tuplas ordenadas)
def transform_dict(original_dict):
    new_dict = {}
    for key, value in original_dict.items():
        try:
            # Intenta interpretar las claves del diccionario como listas o tuplas
            new_key = ast.literal_eval(key)
            if isinstance(new_key, list):
                new_key = tuple(sorted(Counter(new_key).items()))  # Ordenar y contar los elementos de la lista
            new_dict[new_key] = value  # Asignar el valor con la nueva clave transformada
        except (ValueError, SyntaxError):
            new_dict[key] = value  # Si la clave no es interpretable, dejarla como estaba
    return new_dict

# Función para buscar una combinación específica en el diccionario transformado
def search_key(dict, key):
    # Ordenar la clave buscada y convertirla a una tupla de conteos
    llave_ordenada = tuple(sorted(Counter(key).items()))
    return dict.get(llave_ordenada, "No se encontró la combinación")  # Buscar la combinación en el diccionario

# Transformar el diccionario de combinaciones
nuevo_diccionario = transform_dict(combinaciones)

# Buscar una clave específica (basada en el conjunto 'arrayp') en el nuevo diccionario transformado
search_key(nuevo_diccionario, arrayp)




    