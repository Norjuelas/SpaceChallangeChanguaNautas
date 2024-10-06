import pygame
import random

# Clase base Organismo
class Organismo(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, tamaño, color):
        super().__init__()
        # Creación de la imagen y su rectángulo de posición
        self.image = pygame.Surface((tamaño, tamaño))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (pos_x, pos_y)

        # Atributos de características
        self.fuerza = 0
        self.resistencia = 0
        self.regeneracion = 0
        self.crecimiento_adaptabilidad = 0
        self.detoxificacion_defensa = 0
        self.recuperacion = 0

        # Atributos de comportamiento y descripción
        self.behavior = ""
        self.description = ""

    # Método para mostrar la descripción del organismo en pantalla
    def mostrar_descripcion(self, pantalla, fuente, color=(255, 255, 255)):
        texto_descripcion = fuente.render(self.description, True, color)
        pantalla.blit(texto_descripcion, (self.rect.x, self.rect.y - 20))

    # Método para intentar ganar una cuadrícula adyacente vacía
    def intentar_expansion(self, grid, row, col):
        """Intenta expandirse a una celda vacía adyacente según su capacidad de crecimiento."""
        if random.random() < (self.crecimiento_adaptabilidad / 10):  # Probabilidad basada en el crecimiento
            empty_neighbors = grid.get_empty_neighbors(row, col)
            if empty_neighbors:
                new_row, new_col = random.choice(empty_neighbors)  # Selecciona un vecino vacío al azar
                new_organism = self.__class__(new_col * (WIDTH + MARGIN) + MARGIN, 
                                              new_row * (HEIGHT + MARGIN) + MARGIN, WIDTH)
                return (new_row, new_col, new_organism)  # Expansión exitosa
        return None

    # Método para competir por una celda ocupada con otro organismo
    def competir_por_territorio(self, otro_organismo):
        """Compite con otro organismo en función de atributos como fuerza y resistencia."""
        # Calcular el "poder" de ambos organismos
        mi_poder = self.fuerza + self.resistencia + (random.random() * 5)  # Incluye un factor de azar
        poder_otro = otro_organismo.fuerza + otro_organismo.resistencia + (random.random() * 5)
        
        if mi_poder > poder_otro:
            # Este organismo gana la batalla
            return True
        else:
            # Este organismo pierde la batalla
            return False

    # Método para regenerar fuerzas o territorio
    def regenerar(self):
        """Regenera el organismo en función de su capacidad de regeneración."""
        if random.random() < (self.regeneracion / 10):
            # La regeneración podría restaurar atributos o permitir expansión adicional
            return True
        return False

# Clases Hijas
# No necesitan cambios directos, ya que los métodos de interacción están en la clase base

class Azufre(Organismo):
    def __init__(self, pos_x, pos_y, tamaño):
        super().__init__(pos_x, pos_y, tamaño, (255, 255, 0))  # Color amarillo
        self.fuerza = 2
        self.resistencia = 4
        self.regeneracion = 3
        self.crecimiento_adaptabilidad = 3
        self.detoxificacion_defensa = 4
        self.recuperacion = 2
        self.behavior = "Protección celular mejorada y resistencia a infecciones."
        self.description = ("El azufre fortalece los enlaces disulfuro en proteínas, "
                            "reforzando la estructura celular y proporcionando mayor "
                            "resistencia frente a patógenos y estrés ambiental.")

class Hierro(Organismo):
    def __init__(self, pos_x, pos_y, tamaño):
        super().__init__(pos_x, pos_y, tamaño, (255, 0, 0))  # Color rojo
        self.fuerza = 5
        self.resistencia = 5
        self.regeneracion = 2
        self.crecimiento_adaptabilidad = 2
        self.detoxificacion_defensa = 3
        self.recuperacion = 3
        self.behavior = "Facilita el transporte de oxígeno y la formación de hemoglobina."
        self.description = ("El hierro es esencial para la producción de hemoglobina, "
                            "permitiendo el transporte eficiente de oxígeno y "
                            "promoviendo la respiración celular.")

class Nitrogeno(Organismo):
    def __init__(self, pos_x, pos_y, tamaño):
        super().__init__(pos_x, pos_y, tamaño, (0, 0, 255))  # Color azul
        self.fuerza = 3
        self.resistencia = 3
        self.regeneracion = 4
        self.crecimiento_adaptabilidad = 4
        self.detoxificacion_defensa = 2
        self.recuperacion = 3
        self.behavior = "Promueve el crecimiento y el desarrollo en organismos."
        self.description = ("El nitrógeno es crucial para la síntesis de proteínas y "
                            "ácidos nucleicos, apoyando el crecimiento y la reproducción.")

class Hidrogeno(Organismo):
    def __init__(self, pos_x, pos_y, tamaño):
        super().__init__(pos_x, pos_y, tamaño, (0, 255, 255))  # Color cian
        self.fuerza = 1
        self.resistencia = 2
        self.regeneracion = 5
        self.crecimiento_adaptabilidad = 3
        self.detoxificacion_defensa = 3
        self.recuperacion = 4
        self.behavior = "Facilita reacciones químicas y es esencial para el metabolismo."
        self.description = ("El hidrógeno juega un papel vital en las reacciones químicas "
                            "celulares, siendo una parte integral del metabolismo y la energía.")
