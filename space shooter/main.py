import pygame
import sys
import random
from settings import *
from player import Player
from sky import Sky
from asteroid import Asteroid
from bullet import Bullet
from bonus import Bonus
from shield import Shield

def show_game_over():
    game_over =f3.render(("GAME OVER"), True,(WHITE))
    screen.blit(game_over, (0, SCREEN_HEIGHT/2))
    pygame.display.update()
    while 1:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
def show_you_win():
    you_win =f3.render(("YOU WIN"), True,(WHITE))
    screen.blit(you_win, (200, SCREEN_HEIGHT/2))
    pygame.display.update()
    while 1:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
def spawn_meteors(meteors,all_sprites):
    asteroid = Asteroid(screen,meteor_image_list)
    meteors.add(asteroid)
    all_sprites.add(asteroid)
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode( (SCREEN_WIDTH, SCREEN_HEIGHT))
all_sprites = pygame.sprite.Group()
meteors = pygame.sprite.Group()
bullets = pygame.sprite.Group()
bonuses = pygame.sprite.Group()
player=Player("images/Ship.png",screen,(SCREEN_WIDTH)//2,(SCREEN_HEIGHT)//2)
sky=Sky("images/Sky.jpg",screen,0,0)
sky_2=Sky("images/Sky.jpg",screen,0,-1000)
shield = Shield(player,screen)
all_sprites.add(shield)
meteor_filename_list = ["images/meteorGrey_big1.png","images/meteorGrey_big2.png","images/meteorGrey_med1.png","images/meteorGrey_med2.png",
                        "images/meteorGrey_small1.png","images/meteorGrey_small2.png","images/meteorGrey_tiny1.png","images/meteorGrey_tiny2.png"]
bonus_image_dict = {}
bonus_image_dict["gun"] = pygame.image.load("images/bolt_gold.png").convert_alpha()
bonus_image_dict["hp"] = pygame.image.load("images/pill_yellow.png").convert_alpha()
bonus_image_dict["shield"] = pygame.image.load("images/shield_gold.png").convert_alpha()
meteor_image_list = []
for filename in meteor_filename_list:
    meteor_image = pygame.image.load(filename).convert()
    meteor_image_list.append(meteor_image)
all_sprites.add(player)
for i in range(METEORS_QTY):
    asteroid = Asteroid(screen,meteor_image_list)
    meteors.add(asteroid)
    all_sprites.add(asteroid)
for i in range(METEORS_QTY):
    asteroid = Asteroid(screen,meteor_image_list)
    meteors.add(asteroid)
    all_sprites.add(asteroid)
f1 = pygame.font.SysFont('algerian', 50)
f2 = pygame.font.SysFont('algerian', 50)
f3 = pygame.font.SysFont('algerian', 180)
while 1:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
            bullet = Bullet(player.rect.centerx - 6,player.rect.top)
            all_sprites.add(bullet)
            bullets.add(bullet)
            if player.gun_bonus:
                bullet = Bullet(player.rect.left,player.rect.centery)
                all_sprites.add(bullet)
                bullets.add(bullet)
                bullet = Bullet(player.rect.right,player.rect.centery)
                all_sprites.add(bullet)
                bullets.add(bullet)
    
    if shield.hide == False:
        shield_defend_player = pygame.sprite.spritecollide(shield,meteors,True)
        for d in shield_defend_player:
            spawn_meteors(meteors,all_sprites)
            shield.count +=1
    else:
        player_hits_meteors = pygame.sprite.spritecollide(player,meteors,True)
        for hit in player_hits_meteors:
            player.hp -= hit.damage
            player.score -= hit.point
            spawn_meteors(meteors,all_sprites)
    player_hits_meteors = pygame.sprite.groupcollide(meteors,bullets,True,True)
    for hit in player_hits_meteors:
        player.score += hit.point
        spawn_meteors(meteors,all_sprites)
        if random.randint(0,100) < 10:
            bonus = Bonus(bonus_image_dict,hit.rect.center)
            bonuses.add(bonus)
            all_sprites.add(bonus)
    player_hits_bonuses = pygame.sprite.spritecollide(player,bonuses,True)
    for hit in player_hits_bonuses:
        if hit.type == "hp":
            player.hp += random.randint(20,50)
            if player.hp > 100:
                player.hp = 100
        elif hit.type == "gun":
            player.gun_bonus = True
            player.gun_bonus_timer = pygame.time.get_ticks()
        elif hit.type == "shield":
            shield.hide = False
            shield.last_update = pygame.time.get_ticks()
            
            
        
    
        
    
    sky.update()
    sky_2.update()
    all_sprites.update()
    
    screen.fill(BLACK)
    sky.draw()
    sky_2.draw()
    hp=f2.render("Hp " + str(player.hp), True,(WHITE))
    score=f2.render("score " + str(player.score), True,(WHITE))
    all_sprites.draw(screen)
    
    screen.blit(hp, (800,50))
    screen.blit(score, (700,150))
    if player.hp<=0:
        show_game_over()
    if player.score>=20000:
        show_you_win()
    pygame.display.update()
    clock.tick(FPS)
