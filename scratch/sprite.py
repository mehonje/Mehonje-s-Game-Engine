import pygame

class sprite:
    def __init__(self, gameEngine, costume):
        self.x, self.y = 0, 0
        self.dir = 0
        self.screen = gameEngine.screen
        self.screenBounds = gameEngine.screen.get_rect()
        self.setCostume(costume)
        self.rect = self.costumePath.get_rect()
        self.gameEngine = gameEngine

    def setCostume(self, costume):
        if costume != "":
            self.costumePath = pygame.image.load("costumes/" + costume)
        else:
            self.costumePath = pygame.image.load("costumes/costume1.png")

    def stamp(self, transparency):
        self.costume = pygame.transform.rotate(self.costumePath, self.dir)
        self.costume.set_alpha(255 * (1 - transparency / 100))
        self.rect = self.costume.get_rect()
        self.rect.x, self.rect.y = convertCoords(self.x, self.y, self.rect)
        self.screen.blit(self.costume, self.rect)

def convertCoords(x, y, rect, screenWidth = 480, screenHeight = 360):
    #(0, 0) = (240, 180) = (screenWidth / 2, screenHeight / 2)

    if rect != "":
        x = ((screenWidth / 2) + x) - (rect.width / 2)
        y = ((screenHeight / 2) - y) - (rect.height / 2)
    else:
        x = (screenWidth / 2) + x
        y = (screenHeight / 2) - y
    return int(x), int(y)
