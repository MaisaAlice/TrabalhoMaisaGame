#!/usr/bin/python
# -*- coding: utf-8 -*-
from tkinter.font import Font

import pygame
from pygame import Surface
from pygame.examples.grid import WINDOW_HEIGHT
from pygame.font import Font
from pygame.time import Clock

from code.const import WIN_WIDTH, MENU_OPTION
from code.const import COLOR_GREEN
from code.const import COLOR_WHITE


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuBg.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        pygame.mixer_music.load('asset/Menu.mp3.wav')
        pygame.mixer_music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(60, text="Destruição", text_color=COLOR_GREEN, text_center_pos=((WIN_WIDTH / 2), 70),
                           shadow=True)
            self.menu_text(60, text="Zumbi", text_color=COLOR_GREEN, text_center_pos=((WIN_WIDTH / 2), 120),
                           shadow=True)

            for i in range(len(MENU_OPTION)):
                self.menu_text(20, MENU_OPTION[i], text_color=COLOR_WHITE,
                               text_center_pos=((WIN_WIDTH / 2), 200 + 25 * i))

            pygame.display.flip()
            clock: Clock = pygame.time.Clock()

            while True:
                clock.tick(60)

            # Check for all events

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close Window
                    quit()  # end pygame

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple, shadow=False) -> None:
        text_font: Font = pygame.font.SysFont("Rockwell", text_size)

        if shadow:
            shadow_surf: Surface = text_font.render(text, True, (0, 0, 0)).convert_alpha()
            shadow_rect = shadow_surf.get_rect(center=(text_center_pos[0] + 2, text_center_pos[1] + 4))
            self.window.blit(shadow_surf, shadow_rect)

        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect = text_surf.get_rect(center=text_center_pos)

        self.window.blit(text_surf, text_rect)
