import json
import pygame
from utils import SpriteSheet
from constants import GREEN, RED, WHITE
import json
import pygame
from utils import SpriteSheet
from constants import GREEN, RED, WHITE


class Player(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()

        self.change_x = 0
        self.change_y = 0
        data = self.read_json()
        ss = SpriteSheet('assets/scorpion_red_sprites.png')
        self.standing = []
        for row in data['standing']:
            self.standing += self.append_img(ss.get_image(*row))

        self.appercot = []
        for row in data['appercot']:
            self.appercot += self.append_img(ss.get_image(*row))

        self.attack = False
        self.image = self.standing[0]
        self.mask = pygame.mask.from_surface(self.image)
        self.stand_indx = 1
        self.appercot_indx = 0
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.enemy = None
        self.hb = HealthBar(100, 20, 10, 350, 30, 40, 1)

    def read_json(self):
        with open('player.json', 'r') as f:
            data = json.load(f)
        return data

    def append_img(self, img):
        lst = []
        img = pygame.transform.scale2x(img)
        for _ in range(3):
            lst.append(img)
        return lst

    def update(self):
        if not self.attack:
            self.image = self.standing[self.stand_indx % len(self.standing)]
            self.stand_indx += 1
        else:
            self.image = self.appercot[self.appercot_indx % len(self.appercot)]
            self.appercot_indx += 1
            if self.appercot_indx >= len(self.appercot):
                self.attack = False
                self.appercot_indx = 0

        self.rect.x += self.change_x

        self.mask = pygame.mask.from_surface(self.image)
        hit_list = pygame.sprite.collide_mask(self, self.enemy)
        if hit_list:
            self.stop()
        self.hb.update()

    def go_left(self):
        self.change_x = -6

    def go_right(self):
        self.change_x = 6

    def stop(self):
        self.change_x = 0


class Enemy(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()

        self.change_x = 0
        self.change_y = 0
        data = self.read_json()
        self.hp = 100
        ss = SpriteSheet('assets/scorpion_sprites.png')

        self.standing = []
        for row in data['standing']:
            self.standing += self.append_img(ss.get_image(*row), flip=True)

        self.image = self.standing[0]
        self.mask = pygame.mask.from_surface(self.image)
        self.stand_indx = 1
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.hit_cooldown = 0
        self.enemy = None
        self.hb = HealthBar(100, 430, 10, 350, 30, 700, 1)

    def read_json(self):
        with open('enemy.json', 'r') as f:
            data = json.load(f)
        return data

    def append_img(self, img, flip=False):
        lst = []
        img = pygame.transform.scale2x(img)
        if flip:
            img = pygame.transform.flip(img, True, False)
        for _ in range(3):
            self.standing.append(img)
        return lst

    def update(self):
        self.image = self.standing[self.stand_indx % len(self.standing)]
        self.stand_indx += 1
        self.rect.x += self.change_x
        self.mask = pygame.mask.from_surface(self.image)
        hit_list = pygame.sprite.collide_mask(self, self.enemy)
        if hit_list:
            if self.enemy.attack and not self.hit_cooldown:
                self.hit_cooldown = 21
                self.hb.hp -= 10
            self.stop()

        if self.hit_cooldown:
            self.hit_cooldown -= 1
        self.hb.update()

    def go_left(self):
        self.change_x = -6

    def go_right(self):
        self.change_x = 6

    def stop(self):
        self.change_x = 0


class HealthBar:
    def __init__(self, hp, x, y, w, h, text_x, text_y):
        self.hp = hp
        self.h = h
        self.w = w
        self.x = x
        self.y = y
        self.text_x = text_x
        self.text_y = text_y
        self.max_w = w

    def update(self):
        if self.hp < 0:
            self.hp = 0
            return
        self.w = self.hp*3.5

    def draw(self, screen, font):
        square_r = pygame.Rect(self.x, self.y, self.max_w, self.h)
        square_g = pygame.Rect(self.x, self.y, self.w, self.h)
        pygame.draw.rect(screen, RED, square_r)
        pygame.draw.rect(screen, GREEN, square_g)
        text = font.render(str(self.hp), True, WHITE)
        screen.blit(text,  (self.text_x, self.text_y))
