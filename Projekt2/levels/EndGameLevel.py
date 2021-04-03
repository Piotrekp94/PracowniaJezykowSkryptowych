import pygame

from Projekt2.levels.GameLevel import GameLevel


class EndGameLevel(GameLevel):
    def nextLoop(self):
        if self.gameSaved is False:
            self.player.saveScore()
            self.gameSaved = True
        pressed_keys = pygame.key.get_pressed()
        self.player.update(pressed_keys)
        self.draw()

    def __init__(self, screen, player):
        super(EndGameLevel, self).__init__(screen, [], player)
        self.gameSaved = False

    def draw(self):
        self.screen.fill((0, 0, 0))
        if self.player is not None:
            self.screen.blit(self.player.surf, self.player.rect)
        font = pygame.font.Font(pygame.font.get_default_font(), 30)
        endGameText = 'Thank you for playing'
        if self.player.isDead():
            endGameText = 'You Died'
        text_surface = font.render(endGameText, True, (155, 2, 155))
        text_rect = text_surface.get_rect(center=(self.width / 2, self.height / 3))
        self.screen.blit(text_surface, text_rect)
        text_surface = font.render('Your Score is: ' + str(self.player.points), True, (155, 2, 155))
        text_rect = text_surface.get_rect(center=(self.width / 2, self.height / 3 * 2))
        self.screen.blit(text_surface, text_rect)
