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
        self.mask = pygame.mask.from_surface(self.image)
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


class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(black)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Telescope(pygame.sprite.Sprite):


    def __init__(self, x, y, flag, img='tele.png'):
        super().__init__()
        self.image = load_image(img)
        self.image = pygame.transform.scale(self.image, (100, 200))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = x
        self.rect.y = y
        self.flag = flag

    def contact(self):
        if self.flag:
            # мини-игра
            pass
        if not self.flag:
            # делаем чтобы не тыкалось
            pass

class Bed(pygame.sprite.Sprite):


    def __init__(self, x, y, flag, img='bed.png'):
        super().__init__()
        self.image = load_image(img)
        self.image = pygame.transform.scale(self.image, (200, 300))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = x
        self.rect.y = y
        self.flag = flag

    def contact(self):
        if self.flag:
            # мини-игра
            pass
        if not self.flag:
            # делаем чтобы не тыкалось
            pass


class Table(pygame.sprite.Sprite):


    def __init__(self, x, y, flag, img='table.png'):
        super().__init__()
        self.image = load_image(img)
        self.image = pygame.transform.scale(self.image, (220, 200))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = x
        self.rect.y = y
        self.flag = flag

    def contact(self):
        if self.flag:
            # мини-игра
            pass
        if not self.flag:
            # делаем чтобы не тыкалось
            pass


class Comp(pygame.sprite.Sprite):


    def __init__(self, x, y, flag, img='comp.png'):
        super().__init__()
        self.image = load_image(img)
        self.image = pygame.transform.scale(self.image, (130, 120))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = x
        self.rect.y = y
        self.flag = flag

    def contact(self):
        if self.flag:
            # мини-игра
            pass
        if not self.flag:
            # делаем чтобы не тыкалось
            pass


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



    telescope = Telescope(320, 170, True)
    bed = Bed(2, 220, True)
    comp = Comp(490, 160, True)
    table = Table(420, 210, True)
    player = Player(460, 560)
    player.walls = wall_list
    all_sprite_list.add(player)
    all_sprite_list.add(telescope)
    all_sprite_list.add(bed)
    all_sprite_list.add(table)
    all_sprite_list.add(comp)


    carpet = load_image('carpet.png')
    carpet = pygame.transform.scale(carpet, (370, 200))

    books = load_image('books.png')
    books = pygame.transform.scale(books, (80, 100))

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
            screen.blit(carpet, (180, 350))
            screen.blit(books, (80, 100))

            if not player.end:
                all_sprite_list.update()
                all_sprite_list.draw(screen)
            else:
                pygame.quit()
                return True
            if pygame.sprite.collide_rect(player, telescope):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    telescope.contact()
                else:
                    #нужно както написать чтобы не проходилось...
                    pass


#мяршрршршщр

        pygame.display.flip()
        clock.tick(24)


start()