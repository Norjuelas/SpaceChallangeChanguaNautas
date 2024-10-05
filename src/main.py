import pygame
import random

# Clase PantallaInicial para manejar la pantalla de inicio y la generación de maná
class PantallaInicial:
    def __init__(self, ancho, alto, filas, columnas, tamaño_celda):
        self.ancho = ancho
        self.alto = alto
        self.filas = filas
        self.columnas = columnas
        self.tamaño_celda = tamaño_celda
        self.grilla = self.generar_grilla_mana()
        
        # Inicializa la pantalla
        self.pantalla = pygame.display.set_mode((self.ancho, self.alto))
        pygame.display.set_caption("Pantalla Inicial con Maná Procedural")

    # Genera una grilla de maná proceduralmente (valores aleatorios)
    def generar_grilla_mana(self):
        grilla = []
        for fila in range(self.filas):
            fila_grilla = []
            for columna in range(self.columnas):
                # Genera un valor aleatorio de maná (por ejemplo, entre 0 y 255)
                mana_valor = random.randint(0, 255)
                fila_grilla.append(mana_valor)
            grilla.append(fila_grilla)
        return grilla

    # Dibuja la grilla en la pantalla
    def dibujar_grilla(self):
        for fila in range(self.filas):
            for columna in range(self.columnas):
                mana_valor = self.grilla[fila][columna]
                color = (0, mana_valor, 255 - mana_valor)  # Color en función del maná
                pygame.draw.rect(self.pantalla, color, 
                                 (columna * self.tamaño_celda, fila * self.tamaño_celda, 
                                  self.tamaño_celda, self.tamaño_celda))

    # Actualiza la pantalla
    def actualizar(self):
        self.pantalla.fill((0, 0, 0))  # Limpia la pantalla
        self.dibujar_grilla()  # Dibuja la grilla en la pantalla
        pygame.display.flip()  # Actualiza la pantalla de Pygame

    # Maneja el loop de eventos
    def ejecutar(self):
        corriendo = True
        while corriendo:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    corriendo = False

            self.actualizar()

# Inicialización de Pygame y de la pantalla
if __name__ == "__main__":
    pygame.init()

    # Parámetros de la pantalla
    ANCHO = 800
    ALTO = 600
    FILAS = 10
    COLUMNAS = 10
    TAMAÑO_CELDA = 40

    pantalla_inicial = PantallaInicial(ANCHO, ALTO, FILAS, COLUMNAS, TAMAÑO_CELDA)
    pantalla_inicial.ejecutar()

    pygame.quit()
