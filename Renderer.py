import pygame
import Point

class Renderer:
    def __init__(self):
        pygame.init()
        self.scale = 7
        self.screen = pygame.display.set_mode((100 * self.scale, 100 * self.scale))
        pygame.display.set_caption("Pirate Router")
        self.showing = True
        self.backColor = pygame.Color(0, 0, 255)
        self.start = []
        self.end = []
        self.route = []
        self.island = []

    def setIsland(self, islandPoints):
        for p in islandPoints:
            self.island.append([(p.x * self.scale), (p.y * self.scale)])

    def setRoute(self, routePoints):
        for p in routePoints:
            self.route.append([(p.x * self.scale), (p.y * self.scale)])

    def render(self):
        while (self.showing):
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    self.showing = False

            self.screen.fill(self.backColor)

            pygame.draw.polygon(self.screen, [0, 255, 0], self.island)
            pygame.draw.lines(self.screen, [255, 0, 0], False, self.route, 5)
            pygame.draw.circle(self.screen, [0] * 3, self.route[0], 3)
            pygame.draw.circle(self.screen, [0] * 3, self.route[-1], 3)

            pygame.display.flip()

#Added to run when only when called from main
if __name__ == '__main__':
    renderer = Renderer()
    renderer.setIsland([Point.Point(50, 40), Point.Point(20, 30), Point.Point(60, 50)])
    renderer.setRoute([Point.Point(50, 40), Point.Point(20, 30)])
    renderer.render()
