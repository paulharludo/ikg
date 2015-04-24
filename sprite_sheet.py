__author__ = 'JG'

import game_settings

import pygame

class SpriteSheet(object):
    """ Klasse zum laden von Spritesheets sowie zum extrahieren einzelner Bilder """
    sprite_sheet = None

    def __init__(self, file_name):
        """ Konstruktor zum Bilderladen """

        # Sheet laden
        self.sprite_sheet = pygame.image.load(file_name).convert()


    def get_image(self, x, y, width, height):
        """ Extrahieren eines einzelnen Sprites """

        # blanke oberfläche erstellen
        image = pygame.Surface([width, height]).convert()

        # sprite auf oberfläche kopieren
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))

        # zuweisung des colorkeys
        image.set_colorkey(game_settings.COLORCODE)

        # Bild ausgeben
        return image
