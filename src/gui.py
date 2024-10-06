import pygame
import sys
import time
import main

class Button:
    def __init__(self, x, y, width, height, image_path, text):
        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.text = text
        self.font = pygame.font.Font(None, 24)
        self.selected = False

    def draw(self, surface):
        color = BLUE if self.selected else GRAY
        pygame.draw.rect(surface, color, self.rect)
        surface.blit(self.image, self.rect)
        text_surf = self.font.render(self.text, True, BLACK)
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.selected = not self.selected
                return True
        return False

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Juego de Recursos Acuáticos")

# Colores
WHITE = (255, 255, 255)
BLUE = (0, 100, 255)
DARK_BLUE = (0, 50, 150)

# Fuentes
font_big = pygame.font.Font(None, 64)
font_small = pygame.font.Font(None, 32)
font = pygame.font.Font(None, 32)

# Textos
title_text = font_big.render("Changuapp", True, WHITE)
start_text = font_small.render("Presiona ESPACIO para comenzar", True, WHITE)
exit_text = font_small.render("Presiona ESC para salir", True, WHITE)

# Cargar imagen de fondo (asegúrate de tener una imagen llamada 'oceano.jpg' en el mismo directorio)
try:
    background = pygame.image.load("img/oceano.jpg")
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
except pygame.error:
    print("No se pudo cargar la imagen 'img/oceano.jpg'. Usando un fondo azul sólido.")
    background = pygame.Surface((WIDTH, HEIGHT))
    background.fill(BLUE)

# Función para dibujar botón
def draw_button(text, position, size):
    button_rect = pygame.Rect(position, size)
    pygame.draw.rect(screen, DARK_BLUE, button_rect)
    pygame.draw.rect(screen, WHITE, button_rect, 2)
    text_surf = font_small.render(text, True, WHITE)
    text_rect = text_surf.get_rect(center=button_rect.center)
    screen.blit(text_surf, text_rect)
    return button_rect

buttons = [
    Button(50, 150, 150, 150, "img/Azufre.jpg", "Azúfre"),
    Button(250, 150, 150, 150, "img/Hidrogeno.jpg", "Hidrógeno"),
    Button(450, 150, 150, 150, "img/Hierro.jpg", "Hierro"),
    Button(650, 150, 150, 150, "img/Nitrogeno.jpg", "Nitrogeno")
]
# Configuración de la pantalla
running = True
while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if (event.key == pygame.K_SPACE)or((event.type == pygame.MOUSEBUTTONDOWN)and(start_button.collidepoint(event.pos))):
                    print("¡Iniciando el juego!")
                    running = False
                    WIDTH, HEIGHT = 900, 900
                    screen = pygame.display.set_mode((WIDTH, HEIGHT))
                    pygame.display.set_caption("Menú de Opciones")

                    # Colores
                    WHITE = (255, 255, 255)
                    BLACK = (0, 0, 0)
                    GRAY = (200, 200, 200)
                    BLUE = (0, 0, 255)
                    runnin = True
                    selected_options=[]
                    while runnin:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                runnin = False
                            for button in buttons:
                                button.handle_event(event)
                        screen.fill((0, 150, 150))
                        font_inicio = pygame.font.Font(None, 64)
                        title_inicio= font_inicio.render("Selecciona tus bacterias", True, BLACK)
                        screen.blit(title_inicio, (150, 50))
                        # Dibujar botones
                        for button in buttons:
                            button.draw(screen)
                        
                        selected_options = [f"Opción {i+1}" for i, button in enumerate(buttons) if(button.selected)]
                        selected_text = "Opciones seleccionadas: " + ", ".join(selected_options)
                        print(selected_text)
                        text_surf = font.render(selected_text, True, BLACK)
                        screen.blit(text_surf, (50, 350))
                        pygame.display.flip()
                        if (len(selected_options)>=1):
                            text_surf = font.render(selected_text, True, BLACK)
                            screen.blit(text_surf, (50, 350))
                            main.main(selected_options) # Arreglo de las opciones seleccionadas
                            runnin = False 
                        pygame.display.flip()
                if exit_button.collidepoint(event.pos):
                    running = False

        # Dibujar fondo
        screen.blit(background, (0, 0))

        # Dibujar título
        screen.blit(title_text, (WIDTH//2 - title_text.get_width()//2, 50))

        # Dibujar instrucciones
        screen.blit(start_text, (WIDTH//2 - start_text.get_width()//2, HEIGHT - 100))
        screen.blit(exit_text, (WIDTH//2 - exit_text.get_width()//2, HEIGHT - 50))

        # Actualizar pantalla
        pygame.display.flip()

        #pygame.quit()
        #sys.exit()

# Salir del juego
pygame.quit()
sys.exit()