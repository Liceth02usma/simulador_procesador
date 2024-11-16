import pygame
from interfaces.interfaz_computador import InterfazComputador

def main():
    pygame.init()
    screen = pygame.display.set_mode((1024, 600))
    pygame.display.set_caption("Simulador de Procesador")

    # Crear la interfaz principal
    interfaz_computador = InterfazComputador(screen)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Dibujar la interfaz completa
        interfaz_computador.dibujar()

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
