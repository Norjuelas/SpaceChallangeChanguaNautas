import pygame
import random
from organism import Azufre, Hierro, Nitrogeno, Hidrogeno
import os
print(os.getcwd())  # Para saber desde dónde se está ejecutando el programa

# Define colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)  # Color del botón

# Configuraciones de la grilla
WIDTH = 60  # Ancho de cada celda
HEIGHT = 60  # Altura de cada celda
MARGIN = 5   # Espacio entre celdas
GRID_SIZE = 10  # Tamaño de la grilla (20x20)

# Condiciones iniciales del sistema
nutrientes = 100  # Nutrientes iniciales
ph = 7.0  # Nivel de pH inicial (neutral)

class Grid:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = [[None for _ in range(cols)] for _ in range(rows)]

    def draw(self, screen):
        for row in range(self.rows):
            for col in range(self.cols):
                if self.grid[row][col] is not None:
                    screen.blit(self.grid[row][col].image, self.grid[row][col].rect)
                else:
                    pygame.draw.rect(screen, WHITE, 
                                     [(MARGIN + WIDTH) * col + MARGIN,
                                      (MARGIN + HEIGHT) * row + MARGIN,
                                      WIDTH, HEIGHT])

    def add_organism(self, row, col, organism):
        if self.grid[row][col] is None:
            self.grid[row][col] = organism

    def remove_organism(self, row, col):
        """Elimina el organismo en una posición específica"""
        if self.grid[row][col] is not None:
            self.grid[row][col] = None

    def get_empty_neighbors(self, row, col):
        """Devuelve una lista de posiciones (fila, col) vacías alrededor de la posición dada."""
        neighbors = []
        # Lista de posibles movimientos: arriba, abajo, izquierda, derecha
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            # Verificar si la nueva posición está dentro de los límites de la grilla
            if 0 <= new_row < self.rows and 0 <= new_col < self.cols:
                # Verificar si el vecino está vacío
                if self.grid[new_row][new_col] is None:
                    neighbors.append((new_row, new_col))

        return neighbors

class OrganismManager:
    def __init__(self):
        # Cargar imágenes de los organismos
        self.azufre_image = pygame.image.load('img/Azufre.jpg')
        self.hierro_image = pygame.image.load('img/Hierro.jpg')
        self.nitrogeno_image = pygame.image.load('img/Nitrogeno.jpg')
        self.hidrogeno_image = pygame.image.load('img/Hidrogeno.jpg')

        # Redimensionar las imágenes al tamaño de la celda
        self.azufre_image = pygame.transform.scale(self.azufre_image, (WIDTH, HEIGHT))
        self.hierro_image = pygame.transform.scale(self.hierro_image, (WIDTH, HEIGHT))
        self.nitrogeno_image = pygame.transform.scale(self.nitrogeno_image, (WIDTH, HEIGHT))
        self.hidrogeno_image = pygame.transform.scale(self.hidrogeno_image, (WIDTH, HEIGHT))

        self.organism_classes = [Azufre, Hierro, Nitrogeno, Hidrogeno]
        self.selected_organism_class = None  # Organismo seleccionado por el jugador

    def create_organism(self, row, col):
        if self.selected_organism_class is not None:
            organism = self.selected_organism_class(col * (WIDTH + MARGIN) + MARGIN, 
                                                    row * (HEIGHT + MARGIN) + MARGIN, WIDTH)
            # Asignar la imagen correcta al organismo
            if isinstance(organism, Azufre):
                organism.image = self.azufre_image
            elif isinstance(organism, Hierro):
                organism.image = self.hierro_image
            elif isinstance(organism, Nitrogeno):
                organism.image = self.nitrogeno_image
            elif isinstance(organism, Hidrogeno):
                organism.image = self.hidrogeno_image

            return organism
        return None

    def set_selected_organism(self, index):
        """Seleccionar un organismo basado en su índice"""
        if 0 <= index < len(self.organism_classes):
            self.selected_organism_class = self.organism_classes[index]

# Inicializar pygame
pygame.init()

# Definir las dimensiones de la pantalla (se añade espacio adicional para mostrar las condiciones del sistema)
WINDOW_SIZE = [GRID_SIZE * (WIDTH + MARGIN) + 200, GRID_SIZE * (HEIGHT + MARGIN) + 50]
screen = pygame.display.set_mode(WINDOW_SIZE, pygame.RESIZABLE)
pygame.display.set_caption("Organismos en Grilla Modularizada")

# Reloj para controlar la velocidad de actualización
clock = pygame.time.Clock()

# Instancias de la grilla y el manejador de organismos
grid = Grid(GRID_SIZE, GRID_SIZE)
organism_manager = OrganismManager()

# Función para dibujar el botón de iteración
def draw_button(screen):
    button_rect = pygame.Rect(WINDOW_SIZE[0] // 2 - 50, WINDOW_SIZE[1] - 40, 100, 30)
    pygame.draw.rect(screen, BLUE, button_rect)
    font = pygame.font.SysFont(None, 24)
    text = font.render("Iterar", True, WHITE)
    screen.blit(text, (button_rect.x + 25, button_rect.y + 5))
    return button_rect

# Función para manejar la iteración
def handle_iteration():
    global nutrientes
    global ph
    print("Iteración activada")
    nutrientes -= 5  # Los nutrientes disminuyen con cada iteración
    ph = max(0, ph - 0.1)  # El pH baja ligeramente en cada iteración

    new_organisms = []  # Almacenar los organismos que se multiplican
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            organism = grid.grid[row][col]
            if organism is not None:
                if nutrientes <= 0:
                    # Si no hay suficientes nutrientes, el organismo muere
                    grid.remove_organism(row, col)
                else:
                    # Expansión de organismos
                    empty_neighbors = grid.get_empty_neighbors(row, col)
                    if empty_neighbors:
                        new_row, new_col = random.choice(empty_neighbors)
                        new_organism = organism_manager.create_organism(new_row, new_col)
                        if new_organism:
                            new_organisms.append((new_row, new_col, new_organism))
    
    # Agregar los nuevos organismos a la grilla
    for row, col, organism in new_organisms:
        grid.add_organism(row, col, organism)

# Función para dibujar el panel de condiciones del sistema
def draw_system_conditions(screen, nutrientes, ph):
    font = pygame.font.SysFont(None, 36)
    small_font = pygame.font.SysFont(None, 24)

    # Dibujar el panel de condiciones
    text_surface = font.render("Condiciones del Sistema", True, WHITE)
    screen.blit(text_surface, (GRID_SIZE * (WIDTH + MARGIN) + 20, 20))

    # Nutrientes
    nutrientes_text = small_font.render(f"Nutrientes: {nutrientes}", True, WHITE)
    screen.blit(nutrientes_text, (GRID_SIZE * (WIDTH + MARGIN) + 20, 70))

    # pH
    ph_text = small_font.render(f"Nivel de pH: {ph:.1f}", True, WHITE)
    screen.blit(ph_text, (GRID_SIZE * (WIDTH + MARGIN) + 20, 100))

# Función para dibujar los botones de selección de organismos en la derecha
def draw_organism_selection_buttons(screen):
    buttons = []
    organism_names = ['Azufre', 'Hierro', 'Nitrogeno', 'Hidrogeno']
    for i, name in enumerate(organism_names):
        # Dibujar los botones debajo de los indicadores de nutrientes y pH
        button_rect = pygame.Rect(GRID_SIZE * (WIDTH + MARGIN) + 20, 150 + i * 50, 100, 30)
        pygame.draw.rect(screen, BLUE, button_rect)
        font = pygame.font.SysFont(None, 24)
        text = font.render(name, True, WHITE)
        screen.blit(text, (button_rect.x + 10, button_rect.y + 5))
        buttons.append((button_rect, i))  # Guardar el rectángulo del botón y su índice
    return buttons

# Bucle principal del programa
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if iter_button.collidepoint(pos):
                handle_iteration()
            else:
                # Detectar si se hizo clic en algún botón de organismo
                for button_rect, organism_index in organism_buttons:
                    if button_rect.collidepoint(pos):
                        organism_manager.set_selected_organism(organism_index)

                # Añadir organismo al hacer clic en la grilla
                column = pos[0] // (WIDTH + MARGIN)
                row = pos[1] // (HEIGHT + MARGIN)
                if row < GRID_SIZE and column < GRID_SIZE:  # Si se hace clic dentro de la grilla
                    organism = organism_manager.create_organism(row, column)
                    if organism:
                        grid.add_organism(row, column, organism)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_i:  # Detecta si se presiona la tecla 'i'
                handle_iteration()

    # Fondo de la pantalla
    screen.fill(BLACK)

    # Dibujar la grilla
    grid.draw(screen)

    # Dibujar el botón de iteración
    iter_button = draw_button(screen)

    # Dibujar las condiciones del sistema
    draw_system_conditions(screen, nutrientes, ph)

      # Dibujar los botones de selección de organismos
    organism_buttons = draw_organism_selection_buttons(screen)

    # Limitar la actualización a 60 FPS
    clock.tick(60)
    
    # Actualizar la pantalla
    pygame.display.flip()

# Salir del programa
pygame.quit()

