import json
import pygame
from utils import SpriteSheet


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
        self.stand_indx = 1
        self.appercot_indx = 0
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.enemy = None
        self.hp = 100

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

        hit_list = pygame.sprite.collide_rect(self, self.enemy)
        if hit_list:
            self.stop()

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
        self.hp = 100
        ss = SpriteSheet('assets/scorpion_sprites.png')

        self.standing = []
        for i in range(6):
            self.append_img(ss.get_image(73, 0, 48, 100), flip=True)
            self.append_img(ss.get_image(133, 0, 47, 100), flip=True)
            self.append_img(ss.get_image(191, 0, 46, 100), flip=True)
            self.append_img(ss.get_image(250, 0, 47, 100), flip=True)
            self.append_img(ss.get_image(307, 0, 47, 100), flip=True)
            self.append_img(ss.get_image(365, 0, 47, 100), flip=True)
            self.append_img(ss.get_image(424, 0, 49, 100), flip=True)

        self.image = self.standing[0]
        self.stand_indx = 1
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.hit_cooldown = 0
        self.enemy = None
        self.hp = 100

    def append_img(self, img, flip=False):
        img = pygame.transform.scale2x(img)
        if flip:
            img = pygame.transform.flip(img, True, False)
        for _ in range(3):
            self.standing.append(img)

    def update(self):
        self.image = self.standing[self.stand_indx % len(self.standing)]
        self.stand_indx += 1
        self.rect.x += self.change_x
        hit_list = pygame.sprite.collide_rect(self, self.enemy)
        global life
        if hit_list:
            if self.enemy.attack and not self.hit_cooldown:
                self.hit_cooldown = 21
                life -= 35
            self.stop()

        if self.hit_cooldown:
            self.hit_cooldown -= 1

    def go_left(self):
        self.change_x = -6

    def go_right(self):
        self.change_x = 6

    def stop(self):
        self.change_x = 0
