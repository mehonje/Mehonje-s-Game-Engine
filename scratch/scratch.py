import sys
import pygame
from sprite1 import Sprite1

class gameEngine:
    def __init__(self, gameName):
        pygame.init()
        print(f"Thanks for playing {gameName}!")
        print("You can find me at https://scratch.mit.edu/users/mehonje/ and https://github.com/mehonje")
        print("This game was made using Mehonje's Game Engine - https://github.com/mehonje/Mehonje-s-Game-Engine/tree/main")
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((480, 360))
        pygame.display.set_caption(gameName)
        self.setup()

    def setup(self):
        self.sprite1 = Sprite1(self, "costume1.png")

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
