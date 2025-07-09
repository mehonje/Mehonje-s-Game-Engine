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
        self.rect.x, self.rect.y = self.convertCoords(self.x, self.y, self.rect)
        self.costume.set_alpha(255 * (1 - transparency / 100))
        self.screen.blit(self.costume, self.rect)

    def convertCoords(self, x, y, rect):
        match rect:
            case "":
                x = (self.gameEngine.width / 2) + (x * (self.gameEngine.width / 480))
                y = (self.gameEngine.height / 2) - (y * (self.gameEngine.height / 360))
            case _:
                x = ((self.gameEngine.width / 2) + (x * (self.gameEngine.width / 480))) - (rect.width / 2)
                y = ((self.gameEngine.height / 2) - (y * (self.gameEngine.height / 360))) - (rect.height / 2)
        return int(x), int(y)
