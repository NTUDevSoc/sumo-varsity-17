import pygame
import Point

class Renderer:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((200, 200))
        pygame.display.set_caption("Pirate Router")
        self.showing = True
        self.backColor = pygame.Color(0, 0, 255)
    
    def render(self):
        while (self.showing):
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    self.showing = False

            self.screen.fill(self.backColor)
            
            pygame.display.flip();

renderer = Renderer()
renderer.render()
