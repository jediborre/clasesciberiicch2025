import pygame

pygame.init()

ancho, alto = 500, 400
pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Prueba Pygame")

BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)

corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    pantalla.fill(BLANCO)
    pygame.draw.rect(pantalla, ROJO, (200, 150, 100, 100))
    pygame.display.flip()

pygame.quit()
