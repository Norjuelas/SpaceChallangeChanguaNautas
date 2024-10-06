import pygame

# Clase para un organismo quimiosintético
class organism(pygame.sprite.Sprite):

    def __init__(self, pos_x, pos_y, tamaño, color):

        super().__init__()
        
        self.image = pygame.Surface((tamaño, tamaño))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (pos_x, pos_y)
        
        # Atributos adicionales del organismo
        self.energia = 100  # Energía inicial del organismo
        self.velocidad = 2   # Velocidad de movimiento
        self.quimico = 0     # Cantidad de sustancia química para su quimiosíntesis

    # Método para mover al organismo
    def mover(self, direction):
        if direction == 'up':
            self.rect.y -= self.velocidad
        elif direction == 'down':
            self.rect.y += self.velocidad
        elif direction == 'left':
            self.rect.x -= self.velocidad
        elif direction == 'right':
            self.rect.x += self.velocidad

    # Método para realizar quimiosíntesis
    def realizar_quimiosintesis(self):
        if self.quimico > 0:
            self.energia += 10  # Aumenta energía por realizar quimiosíntesis
            self.quimico -= 1   # Se consume parte de la sustancia química
        else:
            self.energia -= 1   # Si no hay quimico disponible, pierde energía

    # Método para detectar colisiones con otras entidades
    def colision(self, otros_sprites):
        if pygame.sprite.spritecollide(self, otros_sprites, False):
            self.energia -= 5  # Pierde energía en colisión, por ejemplo

    # Actualización del organismo
    def update(self):
        self.realizar_quimiosintesis()
        if self.energia <= 0:
            self.kill()  # Elimina el organismo si se queda sin energía

