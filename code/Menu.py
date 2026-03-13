#!/usr/bin/python
# -*- coding: utf-8 -*-
from tkinter.font import Font

import pygame
from pygame import Surface
from pygame.examples.grid import WINDOW_HEIGHT
from pygame.font import Font
from pygame.time import Clock

from code.Const import WIN_WIDTH, MENU_OPTION
from code.Const import COLOR_GREEN
from code.Const import COLOR_WHITE
from code.Const import COLOR_GREEN1


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuBg.png') # Fundo janela
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        menu_option: int = 0
        pygame.mixer_music.load('asset/Theme.wav') # Music
        pygame.mixer_music.play(-1)
        while True: # Nome do jogo
            # DRAWN IMAGES
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(60, text="Destruição", text_color=COLOR_GREEN, text_center_pos=((WIN_WIDTH / 2), 70),
                           shadow=True)
            self.menu_text(60, text="Zumbi", text_color=COLOR_GREEN, text_center_pos=((WIN_WIDTH / 2), 120),
                           shadow=True)

            for i in range(len(MENU_OPTION)): # Menu
                if i == menu_option:
                    self.menu_text(20, MENU_OPTION[i], text_color=COLOR_GREEN1,
                                   text_center_pos=((WIN_WIDTH / 2), 200 + 25 * i))
                else:
                    self.menu_text(20, MENU_OPTION[i], text_color=COLOR_WHITE,
                                   text_center_pos=((WIN_WIDTH / 2), 200 + 25 * i))
            pygame.display.flip()

            clock: Clock = pygame.time.Clock()

            # Check for all events

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close Window
                    quit()  # end pygame

                pygame.key.set_repeat(200, 100) # Segurar tecla

                if event.type == pygame.KEYDOWN: # Tecla para baixo
                    if event.key == pygame.K_UP:
                        menu_option -= 1
                        if menu_option < 0:
                            menu_option = len(MENU_OPTION) - 1

                    if event.key == pygame.K_DOWN: # Tecla para cima
                        menu_option += 1
                        if menu_option >= len(MENU_OPTION):
                            menu_option = 0
                    if event.key == pygame.K_RETURN: # ENTER
                        return MENU_OPTION [menu_option]
                    if event.key == pygame.K_KP_ENTER:
                        return MENU_OPTION [menu_option]

            pygame.display.flip()

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple, shadow=False) -> None:
        text_font: Font = pygame.font.SysFont("Rockwell", text_size) # Texto/Centralizar

        if shadow: # Sombra no texto
            shadow_surf: Surface = text_font.render(text, True, (0, 0, 0)).convert_alpha()
            shadow_rect = shadow_surf.get_rect(center=(text_center_pos[0] + 2, text_center_pos[1] + 4))
            self.window.blit(shadow_surf, shadow_rect)

        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect = text_surf.get_rect(center=text_center_pos) # Fonte/Características

        self.window.blit(text_surf, text_rect)
