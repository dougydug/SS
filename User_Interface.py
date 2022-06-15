import sys
import pygame


class UI:
    def __init__(self, screen):
        self.background = screen
        self.button_gap = 10
        self.active_surface = screen
        self.active_buttons = []

    def draw(self):
        self.background.blit(self.active_surface, self.background.get_rect())
        for x in self.active_buttons:
            self.active_surface.blit(x[1], x[0])

    def resolve_click(self, mouse_pos):
        for x in self.active_buttons:
            if x.collidepoint(mouse_pos):
                x.was_clicked(x[2])


class PauseMenu(UI):
    def __init__(self, screen):
        UI.__init__(self, screen)
        self.menu_button_size = (100, 50)
        self.button_surface = pygame.Surface(self.menu_button_size)
        self.exit_button_rect = pygame.Rect((self.background.get_width() - self.menu_button_size[0]) / 2,
                                            self.background.get_height() / 2, self.menu_button_size[0],
                                            self.menu_button_size[1])
        self.button_surface.fill((0, 0, 0))
        self.QUIT_EVENT = pygame.event.Event(pygame.QUIT)
        self.pause_menu_surface = pygame.Surface((self.background.get_width(), self.background.get_height()),
                                                 pygame.SRCALPHA, 32)
        self.pause_menu_surface.fill((200, 200, 200))
        self.pause_menu_surface.convert_alpha()

    def set_active(self):
        self.active_surface = self.pause_menu_surface
        self.active_buttons.clear()
        self.active_buttons.append({self.exit_button_rect, self.button_surface, 'exit'})

    def was_clicked(self, action):
        if action == 'exit':
            pygame.event.post(self.QUIT_EVENT)


