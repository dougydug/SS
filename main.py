import sys
import pygame
from User_Interface import UI
from User_Interface import PauseMenu
import asyncio
from pygame.sprite import Sprite, Group

from pygame.locals import *

clock = pygame.time.Clock()

WINDOW_SIZE = [1920,1080]

screen = pygame.display.set_mode(WINDOW_SIZE, pygame.FULLSCREEN, 32)

paused = False

interface = PauseMenu(screen)


while True:
    screen.fill((250, 250, 250))

    events = []

    for event in pygame.event.get():
        events.append(event)
        if event.type == QUIT or (event.type == pygame.KEYDOWN and event.key == K_p):
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:

            if event.key == K_ESCAPE:
                paused = not paused

        if paused and event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            interface.resolve_click(pos)

    if paused:
        interface.draw()
    pygame.display.flip()
    clock.tick(60)
