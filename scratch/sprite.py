import pygame

class Sprite:
    def __init__(self, gameEngine, costume):
        self.x, self.y = 0, 0
        self.dir = 0
        self.size = 100
        self.screen = gameEngine.screen
        self.screenBounds = gameEngine.screen.get_rect()
        self.setCostume(costume)
        self.rect = self.costumePath.get_rect()
        self.gameEngine = gameEngine

    def setCostume(self, costume):
        if costume != "":
            self.costumePath = pygame.image.load("costumes/" + costume).convert_alpha()
        else:
            self.costumePath = pygame.image.load("costumes/costume1.png").convert_alpha()

    def stamp(self, transparency, size):
        self.costume = pygame.transform.rotate(self.costumePath, -self.dir)
        self.rect = self.costume.get_rect()
        self.costume = pygame.transform.scale(self.costume, (self.rect.width * (size * (self.gameEngine.width / 480) * 0.01), self.rect.height * (size * (self.gameEngine.height / 360) * 0.01)))
        self.rect = self.costume.get_rect()
        self.rect.x, self.rect.y = convertCoords(self.x, self.y, self.rect, self.gameEngine.width, self.gameEngine.height)
        self.costume.set_alpha(255 * (1 - transparency / 100))
        self.screen.blit(self.costume, self.rect)

def convertCoords(x, y, rect, screenWidth, screenHeight):
    match rect:
        case "":
            x = (screenWidth / 2) + x
            y = (screenHeight / 2) - y
        case _:
            x = ((screenWidth / 2) + x) - (rect.width / 2)
            y = ((screenHeight / 2) - y) - (rect.height / 2)
    return int(x), int(y)
