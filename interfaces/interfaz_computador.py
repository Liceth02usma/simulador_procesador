from .interfaz_bus import InterfazBus
from .interfaz_cpu import InterfazCPU
from .interfaz_io import InterfazIO
from .interfaz_memoria import InterfazMemoria

class InterfazComputador:
    def __init__(self, screen):
        self.screen = screen
        self.io = InterfazIO(screen)
        self.cpu = InterfazCPU(screen)
        self.bus = InterfazBus(screen)
        self.memoria = InterfazMemoria(screen)

    def dibujar(self):
        self.screen.fill((60, 60, 60))  # Fondo gris oscuro
        self.io.dibujar()
        self.cpu.dibujar()
        self.bus.dibujar()
        self.memoria.dibujar()
