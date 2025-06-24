import sys
import pygame
from sprite1 import sprite1

class gameEngine:
    def __init__(self, gameName):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((480, 360))
        pygame.display.set_caption(gameName)
        self.setup()

    def setup(self):
        self.sprite1 = sprite1(self, "costume1.png")

    def runGame(self):
        self.running = True
        while self.running:
            self.tickGame()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            
            self.paintGame()

        pygame.quit()
        sys.exit()

    def tickGame(self):
        self.clock.tick(30)

    def paintGame(self):
        self.screen.fill((255, 255, 255))
        self.sprite1.paint()

        pygame.display.flip()

if __name__ == "__main__":
    game = gameEngine("Untitled")
    game.runGame()
