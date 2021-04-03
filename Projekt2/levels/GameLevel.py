import pygame
from pygame.locals import K_p, K_n

from Projekt2.Ball import Ball
from Projekt2.levels.Level import Level


class GameLevel(Level):
    def __init__(self, screen, bricks, player):
        super(GameLevel, self).__init__(screen, player)
        self.ball = Ball(315, 440)
        self.bricks = bricks

    def nextLoop(self):
        if self.gameIsPaused is False:
            pressed_keys = pygame.key.get_pressed()
            self.player.update(pressed_keys)
            self.draw()
            if self.ball is not None:
                self.handleCollision()
                self.ball.move()
        else:
            self.draw()
            self.drawPausedText()
        if len(self.bricks) == 0:
            self.deactivateLevel()

    def handleInput(self, key):
        if key == K_p:
            self.togglePause()
        if key == K_n:
            self.deactivateLevel()

    def handleCollision(self):
        self.handleCollisionWithWall()
        self.handleCollisionWithPlayer()
        self.handleCollisionWithBrick()

    def handleCollisionWithBrick(self):
        collidingObject = pygame.sprite.spritecollideany(self.ball, self.bricks)

        if collidingObject is not None:
            getDistanceX = abs(collidingObject.rect.x - self.ball.rect.x)
            if getDistanceX < collidingObject.rect.size[0] - 1:
                self.ball.bounceY()
            else:
                self.ball.bounceX()
            collidingObject.kill()
            self.player.addPoints()

    def handleCollisionWithPlayer(self):
        if self.ball.rect.colliderect(self.player.rect):
            self.ball.goUp()

    def handleCollisionWithWall(self):
        if self.ball.rect.y < 0:
            self.ball.goDown()
        if self.ball.rect.y > self.height:
            self.player.die()
            self.ball.reset()
        if self.ball.rect.x < 0 or self.ball.rect.x > self.width:
            self.ball.bounceX()

    def draw(self):
        self.screen.fill((0, 0, 0))
        if self.player is not None:
            self.screen.blit(self.player.surf, self.player.rect)
        for brick in self.bricks:
            self.screen.blit(brick.surf, brick.rect)
        if self.ball is not None:
            self.screen.blit(self.ball.surf, self.ball.rect)
        self.drawLifeAmount(0.05)
        self.drawPoints(0.05, 0.25)

    def drawPausedText(self):
        font = pygame.font.Font(pygame.font.get_default_font(), 36)
        text_surface = font.render('Paused', True, (155, 2, 155))
        text_rect = text_surface.get_rect(center=(self.width / 2, self.height / 2))
        self.screen.blit(text_surface, text_rect)

    def drawLifeAmount(self, offsetPercent):
        font = pygame.font.Font(pygame.font.get_default_font(), 36)
        text_surface = font.render('Your Lives: ' + str(self.player.getLives()), True, (155, 2, 155))
        text_rect = text_surface.get_rect(center=(self.width * offsetPercent, self.height * offsetPercent))
        self.screen.blit(text_surface, text_rect)

    def drawPoints(self, offsetPercentY, offsetPercentX):
        font = pygame.font.Font(pygame.font.get_default_font(), 36)
        text_surface = font.render('Your Points: ' + str(self.player.points), True, (155, 2, 155))
        text_rect = text_surface.get_rect(
            center=(self.width - self.width * offsetPercentX, self.height * offsetPercentY))
        self.screen.blit(text_surface, text_rect)
