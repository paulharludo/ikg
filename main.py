__author__ = 'JG'
import pygame, sys                                       #die imports von pygame und syos
from pygame.locals import *
from sprite_sheet import *
from game_settings import *

def main():
    """ Main Program """
    pygame.init()

    size = [game_settings.SCREEN_WIDTH, game_settings.SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("IKG Simulator")

    fps_ticker = pygame.time.Clock()

    sprites = SpriteSheet("sprites\erstes_spritesheet.gif")   # \ bei linux durch / ersetzen

    oben_links = sprites.get_image(0, 0, 49, 49)
    oben_mitte = sprites.get_image(0,49,49,49)

    while True:
        screen.fill(BGCOLOR)
        screen.blit(oben_links, (0, 0))
        screen.blit(oben_mitte, (0, 49))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.flip()

        fps_ticker.tick(FPS)




if __name__ == "__main__":
    main()
