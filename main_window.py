import pygame
from main import terminate, load_image, cut_sheet

black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 128, 0)
screen_width = 640
screen_height = 640

left = False
right = False
up = False
down = False
pos = 0


def animation(k, list):
    a = k
    if k == 0:
        pass
    if k + 1 >= 24:
        k = 0
    else:
        a = k
        k += 1
    return list[a // 2]



class Player(pygame.sprite.Sprite):

    def __init__(self, x, y, sheet, columns, rows):
        global player_image
        global walk_up
        super().__init__()
        # walk_down, walk_up, walk_right, walk_left
        self.walk_pos = [[], [], [], []]
        self.cut_sheet(sheet, columns, rows)
        self.image = self.walk_pos[1][0]
        self.k = 0
        self.stand = 'up'
        #self.image = pygame.transform.scale(self.image, (150, 200))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = x
        self.rect.y = y
        self.step_x = 0
        self.step_y = 0
        self.walls = None
        self.exit = None
        self.end = False
        self.pos = 0

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

    def cut_sheet(self, sheet, columns, rows):
        rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                           sheet.get_height() // rows)
        frames = []
        for j in range(rows):
            for i in range(columns):
                frame_location = (rect.w * i, rect.h * j)
                frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, rect.size)))



        for i in range(len(frames)):
            frame = pygame.transform.scale(frames[i], (150, 200))
            if i <= 6:
                self.walk_pos[0].append(frame)
            elif i <= 13:
                self.walk_pos[1].append(frame)
            elif i <= 20:
                self.walk_pos[2].append(frame)
            elif i <= 27:
                self.walk_pos[3].append(frame)
    def animation(self, left, right, up, down):
        #stand = 'up'

        if self.pos + 1 >= 28:
            self.pos = 0
        if right:
            self.image = pygame.transform.scale(self.walk_pos[2][self.pos // 4], (150, 200))
            self.pos += 1
            self.stand = 'right'
        elif left:
            self.image = pygame.transform.scale(self.walk_pos[3][self.pos // 4], (150, 200))
            self.pos += 1
            self.stand = 'left'
        elif up:
            self.image = pygame.transform.scale(self.walk_pos[1][self.pos // 4], (150, 200))
            self.pos += 1
            self.stand = 'up'
        elif down:
            self.image = pygame.transform.scale(self.walk_pos[0][self.pos // 4], (150, 200))
            self.pos += 1
            self.stand = 'down'
        else:
            if self.stand == 'up':
                self.image = pygame.transform.scale(self.walk_pos[1][0], (150, 200))
            elif self.stand == 'down':
                self.image = pygame.transform.scale(self.walk_pos[0][0], (150, 200))
            elif self.stand == 'right':
                self.image = pygame.transform.scale(self.walk_pos[2][0], (150, 200))
            elif self.stand == 'left':
                self.image = pygame.transform.scale(self.walk_pos[3][0], (150, 200))
            self.pos = 0







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


class Mini_table(pygame.sprite.Sprite):

    def __init__(self, x, y, flag, img='mini_table.png'):
        super().__init__()
        self.image = load_image(img)
        self.image = pygame.transform.scale(self.image, (150, 200))
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

    # walk_down, walk_up, walk_right, walk_left = [], [], [], []
    # pictures = cut_sheet(load_image('player.png'), 7, 4)
    #
    # for i in range(len(pictures)):
    #     if i <= 6:
    #         walk_down.append(pictures[i])
    #     elif i <= 13:
    #         walk_up.append(pictures[i])
    #     elif i <= 20:
    #         walk_right.append(pictures[i])
    #     elif i <= 27:
    #         walk_left.append(pictures[i])




    wall_coords = [
        [0, 640, 640, 1],
        [0, 1, 1, 640],
        [0, 270, 640, 1],
        [640, 0, 1, 640],
        [0, 310, 640, 1],
        [160, 270, 1, 150],
        [0, 420, 160, 1]
    ]
    for coord in wall_coords:
        wall = Wall(coord[0], coord[1], coord[2], coord[3])
        wall_list.add(wall)
        all_sprite_list.add(wall)



    telescope = Telescope(320, 170, True)
    bed = Bed(2, 220, True)
    comp = Comp(490, 160, True)
    table = Table(420, 210, True)
    minitable = Mini_table(160, 200, True)
    #img = pygame.transform.scale(walk_up[0], (150, 200))
    player = Player(360, 430, load_image('player.png'), 7, 4)
    player.walls = wall_list
    all_sprite_list.add(telescope)
    all_sprite_list.add(bed)
    all_sprite_list.add(table)
    all_sprite_list.add(comp)
    all_sprite_list.add(minitable)

    carpet = load_image('carpet.png')
    carpet = pygame.transform.scale(carpet, (370, 200))

    books = load_image('books.png')
    books = pygame.transform.scale(books, (80, 100))

    all_sprite_list.add(player)
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
                return False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.step_x = 0
                elif event.key == pygame.K_RIGHT:
                    player.step_x = 0
                elif event.key == pygame.K_UP:
                    player.step_y = 0
                elif event.key == pygame.K_DOWN:
                    player.step_y = 0
                left = False
                right = False
                up = False
                down = False
                player.animation(left, right, up, down)


        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT]:
            player.step_x = 5
            left = False
            right = True
            up = False
            down = False
            player.animation(left, right, up, down)

        if key[pygame.K_LEFT]:
            player.step_x = -5
            left = True
            right = False
            up = False
            down = False
            player.animation(left, right, up, down)

        if key[pygame.K_UP]:
            player.step_y = -5
            left = False
            right = False
            up = True
            down = False
            player.animation(left, right, up, down)

        if key[pygame.K_DOWN]:
            player.step_y = 5
            left = False
            right = False
            up = False
            down = True
            player.animation(left, right, up, down)

        # if key[pygame.KEYUP]:
        #     left = False
        #     right = False
        #     up = False
        #     down = False
        #     print(left, right, up, down)
        #     player.animation(left, right, up, down)


            # if pos + 1 >= 28:
            #     pos = 0
            # if down:
            #     player.image = pygame.transform.scale(walk_down[pos // 4], (150, 200))
            #     pos += 1
            # elif event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_LEFT:
            #         player.step_x = -20
            #         left = True
            #         right = False
            #         up = False
            #         down = False
            #     elif event.key == pygame.K_RIGHT:
            #         player.step_x = 20
            #         left = False
            #         right = True
            #         up = False
            #         down = False
            #     elif event.key == pygame.K_UP:
            #         player.step_y = -20
            #         left = False
            #         right = False
            #         up = True
            #         down = False
            #     elif event.key == pygame.K_DOWN:
            #         player.step_y = 20
            #         left = False
            #         right = False
            #         up = False
            #         down = True
            #     else:
            #         left = False
            #         right = False
            #         up = False
            #         down = False
            #         position_animation = 0
            #
            # if event.type == pygame.KEYUP:
            #     if event.key == pygame.K_LEFT:
            #         player.step_x = 0
            #     elif event.key == pygame.K_RIGHT:
            #         player.step_x = 0
            #     elif event.key == pygame.K_UP:
            #         player.step_y = 0
            #     elif event.key == pygame.K_DOWN:
            #         player.step_y = 0

        screen.blit(background_image, (0, 0))
        screen.blit(carpet, (180, 350))
        screen.blit(books, (80, 100))

        if not player.end:
            all_sprite_list.update()
            all_sprite_list.draw(screen)
        else:
            pygame.quit()
            return True
            # if pygame.sprite.collide_rect(player, telescope):
            #     if event.type == pygame.MOUSEBUTTONDOWN:
            #         telescope.contact()
            #     else:
            #         #нужно както написать чтобы не проходилось...
            #         pass


#мяршрршршщр

        pygame.display.flip()
        clock.tick(28)


start()
