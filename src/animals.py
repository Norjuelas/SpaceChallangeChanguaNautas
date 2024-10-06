import json
import ast
from collections import Counter
with open('json/Combinaciones.json', 'r', encoding='utf-8') as file:
    combinaciones = json.load(file)


class Animals:
    def __init__(self) -> None:
        self.elements_dict = self.transform_dict(combinaciones)
    
    def transform_dict(self, original_dict):
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

    def search_key(self, dict, key):
        llave_ordenada = tuple(sorted(Counter(key).items()))
        return dict.get(llave_ordenada, "No se encontró la combinación")
    
    def select_animal(self, element_list):
        return self.search_key(self.elements_dict, element_list)
