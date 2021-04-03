import pygame
from pygame.locals import K_UP, K_DOWN, K_RETURN

from Projekt2.levels.Level import Level
from Projekt2.levels.ScoreLevel import ScoreLevel


class MainMenu(Level):
    def __init__(self, screen, loop):
        super(MainMenu, self).__init__(screen, [])
        self.gameLoop = loop
        self.scoreLevel = ScoreLevel(screen, loop, self)
        self.selectedButton = 0

    def nextLoop(self):
        self.drawMenu()

    def drawMenu(self):
        defaultColor = (155, 2, 155)
        selectedColor = (255, 255, 0)
        self.screen.fill((0, 0, 0))
        font = pygame.font.Font(pygame.font.get_default_font(), 30)
        if self.selectedButton == 0:
            text_surface = font.render('Start', True, selectedColor)
        else:
            text_surface = font.render('Start', True, defaultColor)
        text_rect = text_surface.get_rect(center=(self.width / 2, self.height / 3))
        self.screen.blit(text_surface, text_rect)
        if self.selectedButton == 1:
            text_surface = font.render('Scores ', True, selectedColor)
        else:
            text_surface = font.render('Scores ', True, defaultColor)
        text_rect = text_surface.get_rect(center=(self.width / 2, self.height / 2))
        self.screen.blit(text_surface, text_rect)
        if self.selectedButton == 2:
            text_surface = font.render('Exit ', True, selectedColor)
        else:
            text_surface = font.render('Exit ', True, defaultColor)
        text_rect = text_surface.get_rect(center=(self.width / 2, self.height / 3 * 2))
        self.screen.blit(text_surface, text_rect)

    def handleInput(self, key):
        if key == K_UP and self.isActive:
            self.goUp()
        if key == K_DOWN:
            self.goDown()
        if key == K_RETURN:
            if not self.enter():
                pass

    def goUp(self):
        if self.selectedButton > 0:
            self.selectedButton = self.selectedButton - 1

    def goDown(self):
        if self.selectedButton < 2:
            self.selectedButton = self.selectedButton + 1

    def enter(self):
        if self.selectedButton == 0:
            self.deactivateLevel()
        if self.selectedButton == 1:
            self.gameLoop.currentLevel = self.scoreLevel
        if self.selectedButton == 2:
            pygame.quit()
