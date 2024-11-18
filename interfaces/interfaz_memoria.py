import pygame

#from memoria.control_memoria import control_memoria

class InterfazMemoria:
    def __init__(self, screen):
        self.screen = screen
        #self.control_memoria = control_memoria()
        self.white = (255, 255, 255) 

    def dibujar(self):

        # Dibujar memoria de programa
        pygame.draw.rect(self.screen, (217, 217, 217), (660, 20, 170, 560))  # Gris claro
        self.draw_text("Memoria Programa", 745, 40, True)

        # Dibujar memoria de datos
        pygame.draw.rect(self.screen, (217, 217, 217), (840, 20, 170, 560))  # Gris claro
        self.draw_text("Memoria de Datos", 925, 40, True)

    def draw_text(self, text, x, y, bold=False):
        font = pygame.font.SysFont("Arial", 12, bold=bold)
        text_surface = font.render(text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=(x, y))
        self.screen.blit(text_surface, text_rect)
