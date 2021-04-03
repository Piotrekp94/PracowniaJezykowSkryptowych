import pygame
from pygame.locals import K_RETURN

from Projekt2.levels.Level import Level


class ScoreLevel(Level):
    def __init__(self, screen, loop, menu):
        super(ScoreLevel, self).__init__(screen, [])
        self.selectedButton = 0
        self.scores = self.prepareScores()
        self.gameLoop = loop
        self.menu = menu
        self.defaultColor = (155, 2, 155)
        self.selectedColor = (255, 255, 0)

    def nextLoop(self):
        self.draw()

    @staticmethod
    def prepareScores():
        file1 = open('leaderboard.txt', 'r')
        Lines = file1.readlines()
        scores = []
        # Strips the newline character
        for line in Lines:
            scores.append(int(line.strip()))
        scores.sort(reverse=True)
        if len(scores) < 6:
            return scores
        else:
            return scores[0:5]

    def draw(self):
        self.screen.fill((0, 0, 0))
        font = pygame.font.Font(pygame.font.get_default_font(), 36)
        text_surface = font.render('BACK', True, self.selectedColor)
        text_rect = text_surface.get_rect(center=(self.width / 2, self.height / 4 * 3))
        self.screen.blit(text_surface, text_rect)

        if len(self.scores) == 0:
            font = pygame.font.Font(pygame.font.get_default_font(), 36)
            text_surface = font.render('You have no records', True, self.defaultColor)
            text_rect = text_surface.get_rect(center=(self.width / 2, self.height / 2))
            self.screen.blit(text_surface, text_rect)
        else:
            count = 1
            for score in self.scores:
                font = pygame.font.Font(pygame.font.get_default_font(), 20)
                text_surface = font.render(str(score), True, self.defaultColor)
                text_rect = text_surface.get_rect(center=(self.width * 0.5, self.height * 0.10 * count))
                self.screen.blit(text_surface, text_rect)
                count = count + 1

    def handleInput(self, key):
        if key == K_RETURN:
            self.gameLoop.currentLevel = self.menu
