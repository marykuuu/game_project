import pygame
from main import terminate, load_image

black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 128, 0)
screen_width = 640
screen_height = 640


class Player(pygame.sprite.Sprite):

    def __init__(self, x, y, img='aaa.jpg'):
        super().__init__()
        self.image = load_image(img, colorkey=-1)
        self.image = pygame.transform.scale(self.image, (50, 80))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.step_x = 0
        self.step_y = 0
        self.walls = None
        self.exit = None
        self.end = False

    def update(self):
        self.rect.x += self.step_x
        blocks_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in blocks_list:
            if self.step_x > 0:
                self.rect.right = block.rect.left
            else:
                self.rect.left = block.rect.right

        self.rect.y += self.step_y
        blocks_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in blocks_list:
            if self.step_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom

            # if pygame.sprite.spritecollide(self, self.exit, True):
            #     self.end = True


# class Exit(pygame.sprite.Sprite):
#     def __init__(self, x, y, img='exit.png'):
#         super().__init__()
#         self.image = pygame.image.load(img).convert_alpha()
#         self.image.set_colorkey((255, 255, 255))
#         self.image = pygame.transform.scale(self.image, (60, 60))
#         self.rect = self.image.get_rect()
#         self.rect.x = x
#         self.rect.x = y


class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(black)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


def start():
    pygame.init()
    screen = pygame.display.set_mode([screen_width, screen_height])
    background_image = load_image('fonn.png')
    pygame.display.set_caption('game')

    all_sprite_list = pygame.sprite.Group()
    wall_list = pygame.sprite.Group()

    wall_coords = [
        [0, 640, 640, 1],
        [0, 1, 1, 640],
        [0, 270, 640, 1],
        [640, 0, 1, 640]
    ]
    for coord in wall_coords:
        wall = Wall(coord[0], coord[1], coord[2], coord[3])
        wall_list.add(wall)
        all_sprite_list.add(wall)

    # exit_list = pygame.sprite.Group()
    # exit_coords = [[540, 0]]
    # for coord in exit_coords:
    #     exit = Exit(coord[0], coord[1])
    #     exit_list.add(exit)
    #     all_sprite_list.add(exit)

    player = Player(400, 560)
    player.walls = wall_list
    all_sprite_list.add(player)
    # player.exit = exit_list

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
                return False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.step_x = -20
                elif event.key == pygame.K_RIGHT:
                    player.step_x = 20
                elif event.key == pygame.K_UP:
                    player.step_y = -20
                elif event.key == pygame.K_DOWN:
                    player.step_y = 20

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.step_x = 0
                elif event.key == pygame.K_RIGHT:
                    player.step_x = 0
                elif event.key == pygame.K_UP:
                    player.step_y = 0
                elif event.key == pygame.K_DOWN:
                    player.step_y = 0

            screen.blit(background_image, (0, 0))

            if not player.end:
                all_sprite_list.update()
                all_sprite_list.draw(screen)
            else:
                pygame.quit()
                return True

        pygame.display.flip()
        clock.tick(24)


start()