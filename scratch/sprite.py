import pygame

class sprite:
    def __init__(self, gameEngine, costume):
        self.x, self.y = 0, 0
        self.dir = 180
        self.screen = gameEngine.screen
        self.screenBounds = gameEngine.screen.get_rect()
        self.costumePath = pygame.image.load("C:/users/jack/onedrive/desktop/pywork/lemonoids/costumes/" + costume)
        self.rect = self.costumePath.get_rect()
        self.gameEngine = gameEngine

    def stamp(self):
        self.costume = pygame.transform.rotate(self.costumePath, self.dir)
        self.rect = self.costume.get_rect()
        self.rect.x, self.rect.y = convertCoords(self.x, self.y, self.rect)
        self.screen.blit(self.costume, self.rect)

def convertCoords(x, y, rect, screenWidth = 480, screenHeight = 360):
    #(0, 0) = (240, 180) = (screenWidth / 2, screenHeight / 2)

    x = ((screenWidth / 2) + x) - (rect.width / 2)
    y = ((screenHeight / 2) - y) - (rect.height / 2)
    return int(x), int(y)
