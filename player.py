import pygame
from utils import SpriteSheet


class Player(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()

        self.change_x = 0
        self.change_y = 0
        ss = SpriteSheet('assets/scorpion_red_sprites.png')

        self.standing = []
        self.standing += self.append_img(ss.get_image(0, 0, 46, 100))
        self.standing += self.append_img(ss.get_image(48, 0, 45, 100))
        self.standing += self.append_img(ss.get_image(96, 0, 45, 100))
        self.standing += self.append_img(ss.get_image(142, 0, 46, 100))
        self.standing += self.append_img(ss.get_image(189, 0, 47, 100))
        self.standing += self.append_img(ss.get_image(239, 0, 45, 100))

        self.appercot = []
        self.appercot += self.append_img(ss.get_image(650, 450, 68, 130))
        self.appercot += self.append_img(ss.get_image(718, 450, 68, 130))
        self.appercot += self.append_img(ss.get_image(792, 450, 63, 130))
        self.appercot += self.append_img(ss.get_image(850, 450, 68, 130))
        self.appercot += self.append_img(ss.get_image(965, 450, 68, 130))
        self.appercot += self.append_img(ss.get_image(1036, 450, 68, 130))

        self.attack = False
        self.image = self.standing[0]
        self.stand_indx = 1
        self.appercot_indx = 0
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.enemy = None

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
        self.enemy = None

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
        if hit_list:
            self.stop()

    def go_left(self):
        self.change_x = -6

    def go_right(self):
        self.change_x = 6

    def stop(self):
        self.change_x = 0
