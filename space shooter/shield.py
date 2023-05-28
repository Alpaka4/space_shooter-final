from settings import *
import pygame
class Shield(pygame.sprite.Sprite):
    def __init__(self,player,screen):
        pygame.sprite.Sprite.__init__(self)
        self.player = player
        self.screen = screen
        self.image = pygame.image.load(SHIELD_NAME).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH
        self.rect.y = self.player.rect.y
        self.last_update = pygame.time.get_ticks()
        self.hide = True
        self.count = 0
    def update(self):
        now = pygame.time.get_ticks()
        if self.hide:
            self.rect.x = SCREEN_WIDTH
        else:
            self.rect.center = self.player.rect.center
            if now - self.last_update > 5000:
                self.hide = True
        if self.count >=3:
            self.hide = True
            self.count = 0
