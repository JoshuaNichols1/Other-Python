import pygame
import os
import time
import random

pygame.init()
WIDTH, HEIGHT = 750, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Space Shooter Tutorial')

RED_SPACE_SHIP = pygame.image.load(os.path.join('assets', 'pixel_ship_red_small.png'))
GREEN_SPACE_SHIP = pygame.image.load(os.path.join('assets', 'pixel_ship_green_small.png'))
BLUE_SPACE_SHIP = pygame.image.load(os.path.join('assets', 'pixel_ship_blue_small.png'))

#Player Ship
YELLOW_SPACE_SHIP = pygame.image.load(os.path.join('assets', 'pixel_ship_yellow.png'))

#Lasers
RED_LASERS = pygame.image.load(os.path.join('assets', 'pixel_laser_red.png'))
GREEN_LASERS = pygame.image.load(os.path.join('assets', 'pixel_laser_green.png'))
BLUE_LASERS = pygame.image.load(os.path.join('assets', 'pixel_laser_blue.png'))
YELLOW_LASERS = pygame.image.load(os.path.join('assets', 'pixel_laser_yellow.png'))

BG = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'background-black.png')), (WIDTH, HEIGHT))

class Ship:
    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.lasers = []
        self.cool_down_counter = 0
    
    def draw(self, window):
        window.blit(self.ship_img, (self.x, self.y))
    
    def get_width(self):
        return self.ship_img.get_width()
    
    def get_height(self):
        return self.ship_img.get_height()

class Player(Ship):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.ship_img = YELLOW_SPACE_SHIP
        self.laser_img = YELLOW_LASERS
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health

class Enemy(Ship):
    COLOR_MAP = {
        "red": (RED_SPACE_SHIP, RED_LASERS),
        "green": (GREEN_SPACE_SHIP, GREEN_LASERS),
        "blue": (BLUE_SPACE_SHIP, BLUE_LASERS)
    }
    
    def __init__(self, x, y, color, health=100):
        super().__init__(x, y, health)
        self.ship_img, self.laser_img = self.COLOR_MAP[color]
        self.mask = pygame.mask.from_surface(self.ship_img)
    
    def move(self, vel):
        self.y += vel

def main():
    FPS = 144
    run = True
    level = 0
    lives = 3
    main_font = pygame.font.SysFont('arial', 50)
    lost_font = pygame.font.SysFont('arial', 60)
    
    enemies = []
    wave_length = 5
    enemy_vel = 1
    
    player_vel = 5
    
    player = Player(300, 650)
    
    clock = pygame.time.Clock()
    
    lost = False
    lost_count = 0
    
    def redraw_window():
        WIN.blit(BG, (0,0))
        
        for enemy in enemies:
            enemy.draw(WIN)
        
        player.draw(WIN)
        
        lives_lable = main_font.render(f'Lives: {lives}', 1, (255, 255, 255))
        level_lable = main_font.render(f'Level: {level}', 1, (255, 255, 255))
        
        WIN.blit(lives_lable, (10, 10))
        WIN.blit(level_lable, (WIDTH-level_lable.get_width() - 10, 10))
        
        if lost:
            lost_lable = lost_font.render("You lost!!", 1, (255, 255, 255))
            WIN.blit(lost_lable, (WIDTH/2 - lost_lable.get_width()/2, 350))
        
        pygame.display.update()
    
    while run:
        clock.tick(FPS)
        redraw_window()
        
        if lives <= 0 or player.health <= 0:
            lost = True
        
        if lost:
            if lost_count > FPS * 3:
                run = False
            else:
                continue
            time.sleep(FPS*3)
            run = False
        
        if len(enemies) == 0:
            level += 1
            wave_length += 5
            for i in range(wave_length):
                enemy = Enemy(random.randrange(50, WIDTH-100), random.randrange(-1500, -100), random.choice(["red", "green", "blue"]))
                enemies.append(enemy)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and player.y - player_vel > 0: #forward
            player.y -= player_vel
        if keys[pygame.K_s] and player.y + player_vel + player.get_height() < HEIGHT: #backwards
            player.y += player_vel
        if keys[pygame.K_a] and player.x - player_vel > 0: #left
            player.x -= player_vel
        if keys[pygame.K_d] and player.x + player_vel + player.get_width() < WIDTH: #right
            player.x += player_vel
        
        for enemy in enemies[:]:
            enemy.move(enemy_vel)
            if enemy.y + enemy.get_height() > HEIGHT:
                lives -= 1
                enemies.remove(enemy)
main()