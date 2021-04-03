import pygame
from pygame.locals import K_LEFT, K_RIGHT


class Player(pygame.sprite.Sprite):

    def __init__(self, x, y, width):
        pygame.sprite.Sprite.__init__(self)
        self.points = 0
        self.startingPosition = (x, y)
        self.surf = pygame.Surface((30, 10))
        self.surf.fill((255, 0, 0))
        self.surf = pygame.image.load("images/belka.png").convert()
        self.rect = self.surf.get_rect(center=self.startingPosition)
        self.screenWidth = width
        self.lives = 3

    def update(self, pressed_keys):
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-3, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(3, 0)

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > self.screenWidth:
            self.rect.right = self.screenWidth

    def getLives(self):
        return self.lives

    def isDead(self):
        return self.lives <= 0

    def die(self):
        self.lives = self.lives - 1
        self.rect = self.surf.get_rect(center=self.startingPosition)
        if self.lives == 0:
            self.saveScore()

    def addPoints(self):
        self.points += 10

    def saveScore(self):
        file_object = open('leaderboard.txt', 'a')
        # Append 'hello' at the end of file
        file_object.write(str(self.points) + "\n")
