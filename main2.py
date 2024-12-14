import pygame
import random
import sys
from pygame import transform, image, time, font as _font
from pato_enemigo import PatoEnemigo
from pygame import sprite
from constants import WIN_WIDTH, WIN_HEIGHT
from table_score import TableScore
# Inicialización de Pygame
pygame.init()
_font.init()
font = _font.Font(None, 36)

# Dimensiones de la pantalla
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Caza Patos")
background = transform.scale(image.load("fondo.jpg"),(WIDTH, HEIGHT))
# Colores
WHITE = (255, 255, 255)
BLACK = (255, 255, 255)
GREEN = (0, 255, 0)

# Configuración del jugador
duck_size = 5
ducks = sprite.Group()
duck_count = 10
table_score = TableScore()
# Reloj para controlar la tasa de frames
clock = pygame.time.Clock()

# Cargar imagen de pato
duck_image = pygame.Surface((duck_size, duck_size))
duck_image.fill(GREEN)  # Cambia esto por una imagen real si quieres
image1 = transform.scale(
        image.load("./assets/pato 1.png").convert_alpha(), (75, 50)
)
image2 = transform.scale(
        image.load("./assets/pato 2.png").convert_alpha(), (75, 50)
)

# Generar patos
def spawn_ducks():
    pato_enemigo = PatoEnemigo(
        "./assets/pato 1.png",
        -40,
        random.randint(80, WIN_HEIGHT - 80),
        80,
        50,
        random.randint(1,5),
        1,
        1,
        table_score,
    )
    ducks.add(pato_enemigo)


def draw_ducks(screen):
    for duck in ducks:
        screen.blit(image1, duck.rect.topleft)

def main():

    while True:
        screen.blit(background, (0, 0))
        text = font.render("Puntaje: " + str(table_score.score), 1, WHITE)
        screen.blit(text, (10, 20))
        if random.randint(1,100) < 2:
            spawn_ducks()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for duck in ducks:
                    if duck.rect.collidepoint(mouse_pos):
                        screen.blit(image2, duck.rect.topleft)
                        clock.tick(6000)
                        ducks.remove(duck)
                        table_score.score += 1
        draw_ducks(screen)
        ducks.update()
        pygame.display.flip()
        clock.tick(60)
if __name__ == "__main__":
    main()