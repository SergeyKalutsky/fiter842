import pygame
import player
from constants import WIDTH, HEIGHT, FPS, DARK_RED


class Game:
    def __init__(self):
        pygame.init()
        # Fonts
        self.font = pygame.font.SysFont('Arial', 40)
        self.font_timer = pygame.font.SysFont("Arial", 25)
        self.font_go = pygame.font.SysFont("Arial", 75)
        # Images
        self.bg = pygame.image.load('assets/images/bg3.png')
        # Music
        self.music = pygame.mixer.Sound('assets/sounds/mk3.wav')
        self.gong = pygame.mixer.Sound('assets/sounds/gong.mp3')
        self.laugh = pygame.mixer.Sound('assets/sounds/laugh.mp3')
        self.wd = pygame.mixer.Sound('assets/sounds/wd.mp3')
        # Init
        self.screen = pygame.display.set_mode([WIDTH, HEIGHT])
        self.clock = pygame.time.Clock()
        pygame.display.set_caption('FIGHTER')
        # Players
        self.player = player.Player(120, 85, 'player', 'scorpion_red_sprites', hb_x=20, hb_text_x=40, flip=False)
        self.enemy = player.Player(500, 85, 'enemy', 'scorpion_sprites', hb_x=430, hb_text_x=700, flip=True)
        self.all_sprite_list = pygame.sprite.Group()
        self.all_sprite_list.add(self.player)
        self.all_sprite_list.add(self.enemy)
        self.timer = player.Timer(378, 10, 1200)
        self.player.enemy = self.enemy
        self.enemy.enemy = self.player

    def draw(self):
        self.screen.blit(self.bg, (0, 0))
        self.all_sprite_list.draw(self.screen)
        self.enemy.hb.draw(self.screen, self.font)
        self.player.hb.draw(self.screen, self.font)
        self.timer.draw(self.screen, self.font_timer)

    def run(self):
        done = False
        self.music.play()
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.player.go_left()
                    elif event.key == pygame.K_RIGHT:
                        self.player.go_right()
                    elif event.key == pygame.K_a:
                        self.enemy.go_left()
                    elif event.key == pygame.K_d:
                        self.enemy.go_right()
                    elif event.key == pygame.K_SPACE:
                        self.player.attack = True
                    elif event.key == pygame.K_q:
                        self.enemy.attack = True

                if event.type == pygame.KEYUP:
                    if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                        self.player.stop()
                    if event.key in [pygame.K_a, pygame.K_d]:
                        self.enemy.stop()

            self.draw()
            self.timer.update()
            self.all_sprite_list.update()
            pygame.display.flip()
            self.clock.tick(FPS)
        pygame.quit()


game = Game()
game.run()
