import pygame

from cpu.unidad_control import unidad_control


class InterfazCPU:
    def __init__(self, screen):
        self.screen = screen
        self.control_cpu = unidad_control()
        # Colores
        self.background_color = (60, 60, 60)  # Gris oscuro
        self.frame_color = (217, 217, 217)    # Gris claro
        self.text_color = (0, 0, 0)           # Negro
        self.white = (255, 255, 255)          # Blanco
        self.gray = (128, 128, 128)           # Gris medio

        # Fuente
        self.font = pygame.font.SysFont("Arial", 12)
        self.font_bold = pygame.font.SysFont("Arial", 12, bold=True)
        self.font_large = pygame.font.SysFont("Arial", 18, bold=True)


    def dibujar(self):
        alu_top_y = 100
        pygame.draw.polygon(self.screen, self.frame_color, [(300, alu_top_y), (400, alu_top_y), (350, alu_top_y + 80)])
        self.draw_text("ALU", 350, alu_top_y + 40, self.font_bold, self.text_color, center=True)

        # Etiquetas de A y B encima de la ALU
        self.draw_text("A: 00", 300, alu_top_y - 20, self.font_bold, self.white, center=True)
        self.draw_text("B: 00", 400, alu_top_y - 20, self.font_bold, self.white, center=True)

        # Unidad de Control (UC)
        uc_x, uc_y = 220, 200
        pygame.draw.rect(self.screen, self.frame_color, (uc_x, uc_y, 120, 50))
        self.draw_text("UC", uc_x + 60, uc_y + 25, self.font_bold, self.text_color, center=True)

        # Listado de Registros (PC, MBR, MAR, IR, PSW)
        registros = ["PC: 00", "MBR: 00", "MAR: 00", "IR: 00", "PSW: 00"]
        registro_x, registro_y = 400, 200

        # Dibujar registros y conectar con líneas
        for i, reg in enumerate(registros):
            reg_y = registro_y + i * 40
            pygame.draw.rect(self.screen, self.frame_color, (registro_x, reg_y, 80, 30))
            self.draw_text(reg, registro_x + 40, reg_y + 15, self.font_bold, self.text_color, center=True)


        alu_top_y = 100
        # Ejemplo de líneas usando draw_line

        #Buses
        self.draw_line((uc_x + 120, uc_y + 34), (520 + 100, uc_y + 34))
        self.draw_line((registro_x + 80, registro_y + 40 + 15), (520 + 50, registro_y + 40 + 15))
        self.draw_line((registro_x + 80, registro_y + 80 + 15), (520, registro_y + 80 + 15))


        #Pc a UC
        self.draw_line((uc_x + 120, uc_y + 15), (registro_x, registro_y + 15))


        # Líneas PC a PC
        self.draw_line((registro_x + 30, registro_y), (registro_x + 30, registro_y - 40))
        self.draw_line((registro_x + 30, registro_y - 40), (registro_x + 50, registro_y - 40))
        self.draw_line((registro_x + 50, registro_y - 40), (registro_x + 50, registro_y))


        # UC a MBR
        self.draw_line((uc_x + 60, uc_y + 50), (uc_x + 60, uc_y + 55))
        self.draw_line((uc_x + 60, uc_y + 55), (registro_x, registro_y + 55))


        # UC a MAR
        self.draw_line((uc_x + 60, uc_y + 50), (uc_x + 60, uc_y + 95))
        self.draw_line((uc_x + 60, uc_y + 95), (registro_x, registro_y + 95))


        # UC a IR
        self.draw_line((uc_x + 60, uc_y + 50), (uc_x + 60, uc_y + 135))
        self.draw_line((uc_x + 60, uc_y + 135), (registro_x, registro_y + 135))


        # UC a PSW
        self.draw_line((uc_x + 60, uc_y + 50), (uc_x + 60, uc_y + 175))
        self.draw_line((uc_x + 60, uc_y + 175), (registro_x, registro_y + 175))

        
        # UC a ALU
        self.draw_line((uc_x + 120, uc_y + 15), (uc_x + 130, uc_y + 15))
        self.draw_line((uc_x + 130, uc_y + 15), (uc_x + 130, alu_top_y + 80))
        

        # Cuadro de Registros Generales
        general_reg_x, general_reg_y = 220, 410
        headers = ["Registro", "General"]
        data = [["R0", "R5"], ["R1", "R6"], ["R2", "R7"], ["R3", "R8"], ["R4", "R9"]]
        self.draw_table(general_reg_x, general_reg_y, len(data), len(headers), 90, 30, headers, data)

        # Línea de conexión UC a Registros Generales
        pygame.draw.line(self.screen, self.white, (uc_x + 60, uc_y + 50), (general_reg_x +60, general_reg_y), 2)  # Línea vertical

    def draw_text(self,text, x, y, font, color, center=False):
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(center=(x, y) if center else None)
        if center:
            self.screen.blit(text_surface, text_rect)
        else:
            self.screen.blit(text_surface, (x, y))

    def draw_table(self,x, y, rows, cols, cell_width, cell_height, headers, data):
        for row in range(rows + 1):  # +1 para incluir la fila de encabezados
            for col in range(cols):
                rect_x = x + col * cell_width
                rect_y = y + row * cell_height
                pygame.draw.rect(self.screen, self.white, (rect_x, rect_y, cell_width, cell_height), 1)
                
                # Dibujar texto (encabezados o datos)
                if row == 0:  # Encabezados
                    self.draw_text(headers[col], rect_x + cell_width // 2, rect_y + cell_height // 2, self.font_bold, self.white, center=True)
                else:  # Datos
                    self.draw_text(data[row - 1][col], rect_x + cell_width // 2, rect_y + cell_height // 2, self.font, self.white, center=True)


    def draw_line(self, start, end, color=None, width=2):
        """
        Dibuja una línea en la pantalla.
        
        :param start: Tuple (x1, y1) con las coordenadas de inicio de la línea.
        :param end: Tuple (x2, y2) con las coordenadas de fin de la línea.
        :param color: Color de la línea. Si no se proporciona, usa blanco.
        :param width: Grosor de la línea.
        """
        if color is None:
            color = self.white  # Usa blanco por defecto si no se especifica color.
        pygame.draw.line(self.screen, color, start, end, width)




