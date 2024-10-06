import pygame
import sys
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
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
LIGHT_BLUE = (173, 216, 230)



# Fuentes
font = pygame.font.Font(None, 32)

class DropdownMenu:
    def __init__(self, x, y, w, h, options):
        self.rect = pygame.Rect(x, y, w, h)
        self.options = options
        self.active = False
        self.current_option = options[0]

    def draw(self, surface):
        pygame.draw.rect(surface, WHITE, self.rect)
        pygame.draw.rect(surface, BLACK, self.rect, 2)
        text = font.render(self.current_option, True, BLACK)
        surface.blit(text, (self.rect.x + 5, self.rect.y + 5))
        
        if self.active:
            for i, option in enumerate(self.options):
                option_rect = pygame.Rect(self.rect.x, self.rect.y + self.rect.height * (i+1), self.rect.width, self.rect.height)
                pygame.draw.rect(surface, LIGHT_BLUE, option_rect)
                pygame.draw.rect(surface, BLACK, option_rect, 2)
                text = font.render(option, True, BLACK)
                surface.blit(text, (option_rect.x + 5, option_rect.y + 5))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            elif self.active:
                for i, option in enumerate(self.options):
                    option_rect = pygame.Rect(self.rect.x, self.rect.y + self.rect.height * (i+1), self.rect.width, self.rect.height)
                    if option_rect.collidepoint(event.pos):
                        self.current_option = option
                        self.active = False

# Crear menús desplegables
menus = [
    DropdownMenu(50, 350, 150, 40, ["Hidrógeno", "Azúfre", "Nitrogeno","Hierro"]),
    DropdownMenu(250, 350, 150, 40, ["Hidrógeno", "Azúfre", "Nitrogeno","Hierro"]),
    DropdownMenu(450, 350, 150, 40, ["Hidrógeno", "Azúfre", "Nitrogeno","Hierro"]),
    DropdownMenu(650, 350, 150, 40, ["Hidrógeno", "Azúfre", "Nitrogeno","Hierro"])
]


# Crear botón
button_rect = pygame.Rect(340, 290, 150, 50)
button_text = font.render("Leer Datos", True, BLACK)

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
    image11 = pygame.image.load('img/oceano.jpg')
    screen.blit(image11, (100, 100))
    background = pygame.image.load("img/oceano.jpg")
    background = pygame.transform.scale(background, (800, 600))
except pygame.error:
    print("No se pudo cargar la imagen 'img/oceano.jpg''. Usando un fondo azul sólido.")
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
    Button(50, 200, 150, 150, 'img/Azufre.jpg', "Opción 1"),
    Button(250, 200, 150, 150, 'img/Hidrogeno.jpg', "Opción 2"),
    Button(450, 200, 150, 150, 'img/Hierro.jpg', "Opción 3"),
    Button(650, 200, 150, 150, 'img/Nitrogeno.jpg', "Opción 4")
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
                    WIDTH, HEIGHT = 900, 500
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
                           
                           for menu in menus:
                               menu.handle_event(event)
                           
                           if event.type == pygame.MOUSEBUTTONDOWN:
                               if button_rect.collidepoint(event.pos):
                                   print("Datos seleccionados:")
                                   for i, menu in enumerate(menus):
                                       print(f"Menú {i+1}: {menu.current_option}")
                                       main.main()

                       # Dibujar fondo
                       screen.fill(LIGHT_BLUE)


                       image1 = pygame.image.load('img/Azufre.jpg')
                       image2 = pygame.image.load('img/Hierro.jpg')
                       image3 = pygame.image.load('img/Nitrogeno.jpg')

                        # Lista de imágenes
                       images = [image1, image2, image3]

                       scale_factor = 0.2  # Porcentaje de reducción (0.2 significa 20% del tamaño original)
                       scaled_images = [pygame.transform.scale(img, (int(img.get_width() * scale_factor), int(img.get_height() * scale_factor))) for img in images]

                        # Configurar posiciones
                       x_start = 100  # Coordenada X inicial
                       y_start = 100  # Coordenada Y inicial
                       spacing = 20   # Espacio entre las imágene

                       for index, img in enumerate(scaled_images):
                        x_pos = x_start + index * (img.get_width() + spacing)
                        screen.blit(img, (x_pos, y_start))




                       font_inicio = pygame.font.Font(None, 64)
                       title_inicio= font_inicio.render("Selecciona tus bacterias", True, BLACK)  
                       screen.blit(title_inicio, (170, 50))

                       # Dibujar menús
                       for menu in menus:
                           menu.draw(screen)
                        #imágenes
                        

                       # Dibujar botón
                       pygame.draw.rect(screen, WHITE, button_rect)
                       pygame.draw.rect(screen, BLACK, button_rect, 2)
                       screen.blit(button_text, (button_rect.x + 10, button_rect.y + 10))

                       # Actualizar pantalla
                       pygame.display.flip()

                   # Salir del juego
                   

            
                if exit_button.collidepoint(event.pos):
                    running = False

        # Dibujar fondo
        screen.blit(background, (0, 0))

        # Dibujar título
        screen.blit(title_text, (WIDTH//2 - title_text.get_width()//2, 50))

        # Dibujar botones
        

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