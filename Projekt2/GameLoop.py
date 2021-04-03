import pygame
from pygame.locals import KEYDOWN

from Projekt2.LevelManager import LevelManager
from Projekt2.Player import Player
from Projekt2.levels.MainMenuLevel import MainMenu


class GameLoop:

    def __init__(self, width, height):
        self.gameIsPaused = False
        self.width = width
        self.height = height
        self.isPlaying = True
        self.screen = pygame.display.set_mode([width, height])
        self.player = Player(305, 450, self.width)

        self.levelManager = LevelManager(width, height, self.screen, self.player)
        self.clock = pygame.time.Clock()
        self.currentLevel = MainMenu(self.screen, self)

    def isGameOn(self):
        return self.isPlaying

    def mainLoop(self):
        self.handleGameInput()
        if self.player.isDead():
            self.currentLevel = self.levelManager.levels[len(self.levelManager.levels) - 1]
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
