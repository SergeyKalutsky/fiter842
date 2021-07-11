import pygame
import player
from constants import *


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
        pygame.display.set_caption('FIGHTER')
        self.bg = pygame.image.load('assets/bg3.jpeg')
        self.player = player.Player(120, 85)
        self.enemy = player.Enemy(500, 85)
        self.all_sprite_list = pygame.sprite.Group()
        self.all_sprite_list.add(self.player)
        self.all_sprite_list.add(self.enemy)
        self.clock = pygame.time.Clock()

    def draw(self):
        self.screen.blit(self.bg, (0, 0))
        self.all_sprite_list.draw(self.screen)

    def run(self):
        done = False
        music = pygame.mixer.Sound('assets/mk3.wav')
        music.play()
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.player.go_left()
                    elif event.key == pygame.K_RIGHT:
                        self.player.go_right()
                    elif event.key == pygame.K_a:
                        self.enemy.go_left()
                    elif event.key == pygame.K_d:
                        self.enemy.go_right()

                elif event.type == pygame.KEYUP:
                    if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                        self.player.stop()
                    if event.key in [pygame.K_a, pygame.K_d]:
                        self.enemy.stop()

            self.draw()
            self.all_sprite_list.update()
            pygame.display.flip()
            self.clock.tick(FPS)
        pygame.quit()


game = Game()
game.run()
