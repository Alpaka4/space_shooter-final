from settings import *
import pygame
import random
class Bonus(pygame.sprite.Sprite):
    def __init__(self,image_dict,center):
        pygame.sprite.Sprite.__init__(self)
        self.type = random.choice(["hp","gun","shield"])
        self.image = image_dict[self.type]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.speedy=3
    def update(self):
        self.rect.y+=self.speedy
        if self.rect.y>SCREEN_HEIGHT:
            self.kill()
