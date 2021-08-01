import pygame
import player_artem as player
from constants import WIDTH, HEIGHT, FPS, RED, GREEN


class Game:
    def __init__(self):
        pygame.init()
        self.font = pygame.font.SysFont('Arial', 45)
        self.screen = pygame.display.set_mode([WIDTH, HEIGHT])
        pygame.display.set_caption('FIGHTER')
        self.bg = pygame.image.load('assets/bg3.png')
        self.player = player.Player(120, 85)
        self.enemy = player.Enemy(500, 85)
        self.all_sprite_list = pygame.sprite.Group()
        self.all_sprite_list.add(self.player)
        self.all_sprite_list.add(self.enemy)
        self.player.enemy = self.enemy
        self.enemy.enemy = self.player
        self.clock = pygame.time.Clock()

    def draw(self):
        self.screen.blit(self.bg, (0, 0))
        self.all_sprite_list.draw(self.screen)    
        

    def run(self):
        from player_artem import life
        done = False
        music = pygame.mixer.Sound('assets/mk3.wav')
        music.play()
        def draw_rect(screen, color, sqr):
             square = pygame.Rect(sqr['x'], sqr['y'], sqr['h'], sqr['w'])
             pygame.draw.rect(screen, color, square)
   
        sqr3 = {}
        sqr3['x'] = 20
        sqr3['y'] = 10
        sqr3['w'], sqr3['h'] = 30, 350
        sqr4 = {}
        sqr4['x'] = 20
        sqr4['y'] = 10
        sqr4['w'], sqr4['h'] = 30, 350
        while not done:
            sqr2 = {}
            sqr2['x'] = 430
            sqr2['y'] = 10
            sqr2['w'], sqr2['h'] = 30, life
            print(life)
            from player import life
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                elif  event.type == pygame.KEYDOWN:
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

                if event.type == pygame.KEYUP:
                    if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                        self.player.stop()
                    if event.key in [pygame.K_a, pygame.K_d]:
                        self.enemy.stop()

            self.draw()
            self.all_sprite_list.update()
            draw_rect(self.screen, RED, sqr)
            draw_rect(self.screen, GREEN, sqr2)
            draw_rect(self.screen, RED, sqr3)
            draw_rect(self.screen, GREEN, sqr4)
            pygame.display.flip()
            self.clock.tick(FPS)
        pygame.quit()


game = Game()
game.run()
