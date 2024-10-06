arrayp = {'H', 'S', 'Fe', 'Fe'} 

total_elements = len(arrayp)
element_counts = {}
for element in arrayp:
    if element in element_counts:
        element_counts[element] += 1
    else:
        element_counts[element] = 1

# Calculate the percentage composition and store them in variables
Fe_percentage = (element_counts.get('Fe', 0) / total_elements) * 100
S_percentage = (element_counts.get('S', 0) / total_elements) * 100
H_percentage = (element_counts.get('H', 0) / total_elements) * 100
N_percentage = (element_counts.get('N', 0) / total_elements) * 100
#Count each element
Fe_count = element_counts.get('Fe', 0)
S_count = element_counts.get('S', 0)
H_count = element_counts.get('H', 0)
C_count = element_counts.get('C', 0)
#ph
ph = 7

#logica 
if Fe_percentage==50 & S_percentage==50:
    ph = 7 #mueren todos
elif Fe_percentage<10 & S_percentage<10:
    ph = 7 
    if H_percentage > 50:
        ph = 5
else:
    if Fe_percentage > 40:
        ph = 9
        if Fe_percentage > 60:
            ph = 11
            if Fe_percentage > 90:
                ph = 14


    if S_percentage > 40:
        ph = 5
        if S_percentage > 60:
            ph = 3
            if S_percentage > 90:
                ph = 1 #inviable


#Desactivar avances de las habilidades
import json
import ast
from collections import Counter
with open('Combinaciones.json', 'r', encoding='utf-8') as file:
    combinaciones = json.load(file)

def transform_dict(original_dict):
    new_dict = {}
    for key, value in original_dict.items():
        try:
            new_key = ast.literal_eval(key)
            if isinstance(new_key, list):
                new_key = tuple(sorted(Counter(new_key).items())) 
            new_dict[new_key] = value
        except (ValueError, SyntaxError):
            new_dict[key] = value
    return new_dict

def search_key(dict,key):
    llave_ordenada = tuple(sorted(Counter(key).items()))
    return dict.get(llave_ordenada, "No se encontró la combinación")

nuevo_diccionario = transform_dict(combinaciones)
search_key(nuevo_diccionario, arrayp)




    