import pygame
from pygame.locals import KEYDOWN, K_ESCAPE, K_UP, K_DOWN, K_LEFT, K_RIGHT, QUIT

from Projekt2.Ball import Ball
from Projekt2.Brick import Brick
from Projekt2.Player import Player

pygame.init()

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
clock = pygame.time.Clock()

isPlaying = True

pygame.display.set_caption("Arkanoid UJ")

player = Player(305, 450, SCREEN_WIDTH)
brick = Brick(20, 20)
ball = Ball(315, 440)

bricks = pygame.sprite.Group()
bricks.add(brick)


def generate_level():
    pass


def update_ball_position():
    pass


pygame.mixer.music.load("sounds/intro.mp3")
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1)

while isPlaying:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isPlaying = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                isPlaying = False

    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)

    screen.fill((0, 0, 0))

    for brick in bricks:
        screen.blit(brick.surf, brick.rect)
    screen.blit(player.surf, player.rect)
    screen.blit(ball.surf, ball.rect)

    if pygame.sprite.spritecollideany(ball, bricks):
        delete_klocek = pygame.sprite.spritecollideany(ball, bricks)
        delete_klocek.kill()
        # usuniecie klocka

    clock.tick(60)
    pygame.display.flip()

pygame.quit()
