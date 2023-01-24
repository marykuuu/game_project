import pygame

black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 128, 0)
screen_width = 780
screen_height = 720


class Player(pygame.sprite.Sprite):

    def __init__(self, x, y, img='man.png'):
        super().__init__()
        self.image = pygame.image.load(img).convert_alpha()
        self.image.set_colorkey((255, 255, 255))
        self.image = pygame.transform.scale(self.image, (40, 40))
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

            if pygame.sprite.spritecollide(self, self.exit, True):
                self.end = True


class Exit(pygame.sprite.Sprite):
    def __init__(self, x, y, img='exit.png'):
        super().__init__()
        self.image = pygame.image.load(img).convert_alpha()
        self.image.set_colorkey((255, 255, 255))
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.x = y


class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, windth, height):
        super().__init__()

        self.image = pygame.Surface([windth, height])
        self.image.fill(black)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


def start():
    pygame.init()
    screen = pygame.display.set_mode([screen_width, screen_height])
    pygame.display.set_caption('Maze')

    all_sprite_list = pygame.sprite.Group()
    wall_list = pygame.sprite.Group()

    wall_coords = [
        [0, 60, 240, 1],
        [60, 180, 1, 180],
        [0, 0, 780, 1],
        [780, 0, 1, 720],
        [0, 720, 780, 1],
        [0, 0, 1, 720],
        [60, 120, 120, 1],
        [60, 120, 1, 60],
        [60, 180, 180, 1],
        [240, 180, 1, 120],
        [240, 300, 60, 1],
        [300, 300, 1, 60],
        [300, 360, 120, 1],
        [420, 240, 1, 120],
        [420, 240, 60, 1],
        [300, 60, 60, 1],
        [300, 60, 1, 180],
        [300, 240, 60, 1],
        [360, 180, 1, 60],
        [360, 180, 60, 1],
        [0, 540, 60, 1],
        [60, 420, 1, 120],
        [60, 420, 300, 1],
        [360, 420, 1, 60],
        [240, 480, 120, 1],
        [240, 480, 1, 60],
        [240, 540, 180, 1],
        [120, 240, 60, 1],
        [180, 240, 1, 120],
        [120, 360, 120, 1],
        [120, 360, 1, 60],
        [120, 480, 1, 60],
        [120, 480, 60, 1],
        [180, 480, 1, 60],
        [180, 540, 60, 1],
        [0, 600, 60, 1],
        [540, 0, 1, 300],
        [540, 300, 180, 1],
        [60, 660, 1, 60],
        [60, 660, 120, 1],
        [180, 660, 1, 60],
        [120, 600, 1, 60],
        [240, 600, 1, 120],
        [180, 600, 60, 1],
        [420, 660, 1, 60],
        [420, 660, 300, 1],
        [720, 600, 1, 60],
        [540, 600, 180, 1],
        [300, 600, 1, 120],
        [360, 120, 1, 180],
        [600, 0, 1, 60],
        [600, 60, 120, 1],
        [240, 60, 60, 1],
        [720, 60, 1, 60],
        [660, 120, 60, 1],
        [660, 120, 1, 60],
        [720, 180, 60, 1],
        [360, 600, 1, 60],
        [360, 600, 120, 1],
        [480, 540, 1, 60],
        [480, 540, 60, 1],
        [540, 480, 1, 60],
        [420, 480, 120, 1],
        [420, 360, 1, 120],
        [600, 540, 120, 1],
        [600, 420, 1, 120],
        [600, 420, 120, 1],
        [420, 60, 1, 60],
        [420, 60, 60, 1],
        [480, 60, 1, 300],
        [480, 60, 60, 1],
        [660, 300, 1, 60],
        [480, 360, 1, 60],
        [480, 420, 120, 1],
        [600, 120, 1, 120],
        [600, 240, 120, 1],
        [720, 360, 60, 1],
        [660, 480, 120, 1],
        [60, 300, 60, 1],
        [240, 120, 1, 60]
    ]
    for coord in wall_coords:
        wall = Wall(coord[0], coord[1], coord[2], coord[3])
        wall_list.add(wall)
        all_sprite_list.add(wall)

    exit_list = pygame.sprite.Group()
    exit_coords = [[540, 0]]
    for coord in exit_coords:
        exit = Exit(coord[0], coord[1])
        exit_list.add(exit)
        all_sprite_list.add(exit)

    player = Player(300, 660)
    player.walls = wall_list
    all_sprite_list.add(player)
    player.exit = exit_list

    clock = pygame.time.Clock()
    # done = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.step_x = -40
                elif event.key == pygame.K_RIGHT:
                    player.step_x = 40
                elif event.key == pygame.K_UP:
                    player.step_y = -40
                elif event.key == pygame.K_DOWN:
                    player.step_y = 40

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.step_x = 0
                elif event.key == pygame.K_RIGHT:
                    player.step_x = 0
                elif event.key == pygame.K_UP:
                    player.step_y = 0
                elif event.key == pygame.K_DOWN:
                    player.step_y = 0

            screen.fill(white)

            if not player.end:
                all_sprite_list.update()
                all_sprite_list.draw(screen)
            else:
                pygame.quit()
                return True

        pygame.display.flip()
        clock.tick(24)

    # pygame.quit()
start()