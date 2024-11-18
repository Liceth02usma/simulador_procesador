import pygame

import  buses.control_bus as control_bus

class InterfazBus:
    def __init__(self, screen):
        #self.control_bus = control_bus()
        self.screen = screen
        self.white = (255, 255, 255) 

    def dibujar(self):
        # Dibujar líneas del bus
        sec3_x_start, sec3_y_start = 520, 20
        sec3_y_end = 580
        sec3_spacing = 50
        mem_prog_x = 660  # X de la memoria de programa

        for i in range(3):
        # Calculamos la posición X de cada línea
            line_x = sec3_x_start + i * sec3_spacing

        # Dibujar la línea vertical
            pygame.draw.line(self.screen, self.white, (line_x, sec3_y_start), (line_x, sec3_y_end), 4)

        # Conectar la parte inferior de cada línea con la memoria de programa
            pygame.draw.line(self.screen, self.white, (line_x, sec3_y_end + (i*-15)), (mem_prog_x, sec3_y_end + (i*-15)), 2)
        x_start, y_start, y_end = 520, 20, 580
        spacing = 50

        for i in range(3):
            x_pos = x_start + i * spacing
            pygame.draw.line(self.screen, (255, 255, 255), (x_pos, y_start), (x_pos, y_end), 4)

