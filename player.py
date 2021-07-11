import pygame
from utils import SpriteSheet


class Player(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()

        self.change_x = 0
        self.change_y = 0
        ss = SpriteSheet('assets/scorpion_red_sprites.png')

        self.standing = []
        for _ in range(6):
            self.append_img(ss.get_image(0, 0, 46, 100))
            self.append_img(ss.get_image(48, 0, 45, 100))
            self.append_img(ss.get_image(96, 0, 45, 100))
            self.append_img(ss.get_image(142, 0, 46, 100))
            self.append_img(ss.get_image(189, 0, 47, 100))
            self.append_img(ss.get_image(239, 0, 45, 100))

        self.image = self.standing[0]
        self.stand_indx = 1
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def append_img(self, img):
        img = pygame.transform.scale2x(img)
        for _ in range(3):
            self.standing.append(img)

    def update(self):
        self.image = self.standing[self.stand_indx % len(self.standing)]
        self.stand_indx += 1
        # self.rect.x += self.change_x
        # if self.direction == "R":
        #     frame = self.rect.x % len(self.walking_frames_r)
        #     self.image = self.walking_frames_r[frame]
        # else:
        #     frame = self.rect.x % len(self.walking_frames_l)
        #     self.image = self.walking_frames_l[frame]

    def draw(self, screen):
        pass

    # Движение, управляемое игроком:
    def go_left(self):
        """ Вызывается, когда пользователь нажимает стрелку влево. """
        self.change_x = -6
        self.direction = "L"

    def go_right(self):
        """ Вызывается, когда пользователь нажимает стрелку вправо. """
        self.change_x = 6
        self.direction = "R"

    def stop(self):
        """Вызывается, когда пользователь отпускает клавиатуру. """
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

    def append_img(self, img, flip=False):
        img = pygame.transform.scale2x(img)
        if flip:
            img = pygame.transform.flip(img, True, False)
        for _ in range(3):
            self.standing.append(img)

    def update(self):
        self.image = self.standing[self.stand_indx % len(self.standing)]
        self.stand_indx += 1
        # self.rect.x += self.change_x
        # if self.direction == "R":
        #     frame = self.rect.x % len(self.walking_frames_r)
        #     self.image = self.walking_frames_r[frame]
        # else:
        #     frame = self.rect.x % len(self.walking_frames_l)
        #     self.image = self.walking_frames_l[frame]

    def draw(self, screen):
        pass

    # Движение, управляемое игроком:
    def go_left(self):
        """ Вызывается, когда пользователь нажимает стрелку влево. """
        self.change_x = -6
        self.direction = "L"

    def go_right(self):
        """ Вызывается, когда пользователь нажимает стрелку вправо. """
        self.change_x = 6
        self.direction = "R"

    def stop(self):
        """Вызывается, когда пользователь отпускает клавиатуру. """
        self.change_x = 0
