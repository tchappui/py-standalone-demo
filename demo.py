#!/usr/bin/env python3
# -*- coding: utf-8

""" This is a test pygame application."""

RECTANGLE = 'images/sprite.png'

import pygame as pg

class Application:
    """ Application represents our Pygame application.
    
    Application initialize the application and gives a method to start it."""

    def __init__(self):
        """ Constructor."""

        pg.init()

        # Set screen size
        self.width = 500
        self.height = 500
        self.screen = pg.display.set_mode((self.width, self.height))

        # Set background color
        white = (255, 255, 255)
        self.background = pg.Surface((self.width, self.height))
        self.background.fill(white)

        # Load sprite
        self.sprite = pg.image.load(RECTANGLE)

        # Sprite initially positioned at the center of screen
        self.sprite_rect = self.sprite.get_rect()
        self.sprite_rect.centerx = (self.width//2)
        self.sprite_rect.centery = (self.height//2)
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.sprite, self.sprite_rect)
        pg.display.flip()

    def run(self):
        """ Starts the application."""
        clock = pg.time.Clock()
        while 1:
            # Limit runtime speed to 30 frames/second
            clock.tick(30)

            pg.event.pump()

            # A key has been pressed
            keyinput = pg.key.get_pressed()

            # Exit on window corner x click
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    raise SystemExit

            # Check arrow keys and move sprite in direction of arrow by 2 pixels
            if keyinput[pg.K_LEFT]:
                self.sprite_rect.centerx -= 2
            elif keyinput[pg.K_RIGHT]:
                self.sprite_rect.centerx += 2
            elif keyinput[pg.K_UP]:
                self.sprite_rect.centery -= 2
            elif keyinput[pg.K_DOWN]:
                self.sprite_rect.centery += 2
            # update sprite position
            self.screen.blit(self.background, (0, 0))
            self.screen.blit(self.sprite, self.sprite_rect)
            # update display
            pg.display.flip()

def main():
    app = Application()
    app.run()

if __name__ == "__main__":
    main()

