import pygame

from entradaSalida import control_io

class InterfazIO:
    def __init__(self, screen):
        self.screen = screen
        self.control_io = control_io
        

    def dibujar(self):
        # Dibujar Input
        pygame.draw.rect(self.screen, (128, 128, 128), (20, 20, 180, 360))  # Gris medio
        self.draw_text2("Input", 110, 40, True)

        # Dibujar Output
        pygame.draw.rect(self.screen, (128, 128, 128), (20, 400, 180, 160))  # Gris medio
        self.draw_text2("Output", 110, 480, True)

    def draw_text2(self, text, x, y, bold=False):
        font = pygame.font.SysFont("Arial", 12, bold=bold)
        text_surface = font.render(text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(x, y))
        self.screen.blit(text_surface, text_rect)




