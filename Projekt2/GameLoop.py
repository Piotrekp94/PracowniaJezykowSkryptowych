import pygame
from pygame.locals import KEYDOWN

from Projekt2.LevelManager import LevelManager
from Projekt2.levels.MainMenuLevel import MainMenu

class GameLoop:

    def __init__(self, width, height):
        self.gameIsPaused = False
        self.width = width
        self.height = height
        self.isPlaying = True
        self.screen = pygame.display.set_mode([width, height])
        self.levelManager = LevelManager(width, height, self.screen)
        self.clock = pygame.time.Clock()
        self.currentLevel = MainMenu(self.screen)

    def isGameOn(self):
        return self.isPlaying

    def mainLoop(self):
        self.handleGameInput()
        if self.currentLevel.isActive:
            self.currentLevel.nextLoop()
        else:
            self.currentLevel = self.levelManager.getNextLevel()

        self.clock.tick(60)
        pygame.display.flip()

    def handleGameInput(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.isPlaying = False
            elif event.type == KEYDOWN:
                self.currentLevel.handleInput(event.key)

    def handleCollision(self):
        # collidingObject = pygame.sprite.spritecollideany(self.ball, self.bricks)
        # if (collidingObject):
        #     if(collidingObject.rect.width / 2):
        #
        #     collidingObject.kill()
        pass


