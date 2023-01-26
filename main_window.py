import pygame
from main import terminate, load_image
from slidepuzzle import puzzle
from game import memory_stars
from maze import labirint

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

IRON_KEY = False
SILVER_KEY = False
GOLDEN_KEY = False

MESSAGES = [[('Кажется, на экране', 'видна головоломка..'), 'серебряный ключ уже у вас!'], ['Может взгянуть в телескоп..?', 'золотой ключ уже у вас!'], [('Под кроватью такой бардак,', 'словно лабиринт..'), 'железный ключ уже у вас!']]


def show_message(screen, sms, key='small'): #выводит на экран сообщение при взаимодействии
    if key == 'small':
        font = pygame.font.Font(None, 30)
        pygame.draw.rect(screen, (177, 162, 219), [30, 500, 300, 100])

        # Рисуем текст. "True" означает использовать сглаживание
        # Black -- цвет текста. Следующая строка создает образ текста
        # но не рисует его на экране.
        text = font.render(sms, True, 'white')
        screen.blit(text, [35, 535])
    elif key == 'big':
        font = pygame.font.Font(None, 30)
        pygame.draw.rect(screen, (177, 162, 219), [30, 500, 300, 100])
        coord = 530
        for el in sms:


            text = font.render(el, True, 'white')
            screen.blit(text, [35, coord])
            coord += 20




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
        self.image.set_alpha(0)
        self.rect.x = x
        self.rect.y = y


class Furniture(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, img, name):

        super().__init__()
        self.image = load_image(img)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = x
        self.rect.y = y
        self.flag = True
        self.k = 0
        self.name = name
        self.mess = -1

    def contact(self):
        global GOLDEN_KEY, SILVER_KEY, IRON_KEY

        if self.flag:
            if self.k == 0:
                self.k = 1
            elif self.k == 1:
                if self.name == 'comp':#silver
                    result = puzzle()
                    if result == 1:
                        SILVER_KEY = True
                elif self.name == 'tele':#golden
                    result = memory_stars()
                    if result == 1:
                        GOLDEN_KEY = True
                elif self.name == 'bed':#iron
                    result = labirint()
                    if result == 1:
                        IRON_KEY = True
                else:
                    result = 0

                if result == 1:
                    self.flag = False
                    self.k = 2
        else:
            self.k = 3

            self.mess = -self.mess









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
            if puzzle() == 1:
                self.flag = False
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

class Door1(pygame.sprite.Sprite):

    def __init__(self, x, y, wight, height, img='door1.jpg'):
        super().__init__()
        self.image = load_image(img)
        self.image = pygame.transform.scale(self.image, (wight, height))# 40 115
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = x
        self.rect.y = y
        self.flag = False
        self.mess = -1


    def contact(self):
        if not(IRON_KEY and GOLDEN_KEY and SILVER_KEY):
            self.mess = -self.mess
        # else:
        #     self.flag = True


class Door2(pygame.sprite.Sprite):

    def __init__(self, x, y, flag, img='door.png'):
        super().__init__()
        self.image = load_image(img)
        self.image = pygame.transform.scale(self.image, (300, 50))
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

    tablee = 0

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
        [0, 660, 640, 1],
        [-50, 0, 1, 640],
        [690, 0, 1, 640],
        [610, 200, 1, 100],
        [0, 200, 640, 1],
        [0, 310, 100, 1]
    ]
    for coord in wall_coords:
        wall = Wall(coord[0], coord[1], coord[2], coord[3])
        wall_list.add(wall)
        all_sprite_list.add(wall)



    telescope = Furniture(320, 170, 100, 200, 'tele.png', 'tele')
    bed = Furniture(2, 220, 200, 300, 'bed.png', 'bed')
    comp = Furniture(490, 160, 130, 120, 'comp.png', 'comp')
    table = Table(420, 210, True)
    minitable = Mini_table(160, 200, True)
    door_out = Door1(620, 405, 20, 115)
    door_in = Door1(365, 620, 150, 20)
    #img = pygame.transform.scale(walk_up[0], (150, 200))
    player = Player(360, 430, load_image('player.png'), 7, 4)
    player.walls = wall_list
    all_sprite_list.add(telescope)
    all_sprite_list.add(bed)
    all_sprite_list.add(table)
    all_sprite_list.add(comp)
    all_sprite_list.add(minitable)
    all_sprite_list.add(door_out)
    all_sprite_list.add(door_in)

    carpet = load_image('carpet.png')
    carpet = pygame.transform.scale(carpet, (370, 200))

    books = load_image('books.png')
    books = pygame.transform.scale(books, (80, 100))

    all_sprite_list.add(player)
    clock = pygame.time.Clock()

    while True:
        pygame.display.set_caption('game')
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
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # if door_out.flag == True:
                    #     return 1
                    if pygame.sprite.collide_rect(player, comp):
                        comp.contact()
                        print('tab')
                    else:
                        comp.k = 0


                        #table.contact()
                    if pygame.sprite.collide_rect(player, telescope):
                        print('tele')
                        telescope.contact()
                    else:
                        telescope.k = 0
                    if pygame.sprite.collide_rect(player, bed):
                        print('bed')
                        bed.contact()
                    else:
                        bed.k = 0
                    if pygame.sprite.collide_rect(player, door_out):
                        print(SILVER_KEY, GOLDEN_KEY,  IRON_KEY)
                        if (SILVER_KEY and GOLDEN_KEY and IRON_KEY):
                            return 1
                        else:
                            door_out.contact()
                    else:
                        door_out.mess = -1


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

        #door = pygame.draw.rect(screen, (84, 44, 33), [620, 400, 20, 140])


        # font = pygame.font.Font(None, 25)
        #
        # # Рисуем текст. "True" означает использовать сглаживание
        # # Black -- цвет текста. Следующая строка создает образ текста
        # # но не рисует его на экране.
        # text = font.render("My text", True, black)
        #
        # # Рисуем изображение текста на экран в точке (250, 250)
        # screen.blit(text, [250, 250])
        #
        # # Рисуем прямоугольник
        # pygame.draw.rect(screen, 'black', [20, 20, 250, 100])
        # if pygame.sprite.spritecollideany(player, door):
        #     print(1)

        if not player.end:
            all_sprite_list.update()
            all_sprite_list.draw(screen)
            # if door_out.mess == 1:
            #     show_message(screen, 'НЕДОСТАТОЧНО КЛЮЧЕЙ')
            if telescope.k == 1:
                show_message(screen, MESSAGES[1][0])
            if bed.k == 1:
                show_message(screen, MESSAGES[2][0], key='big')
            if comp.k == 1:
                show_message(screen, MESSAGES[0][0], key='big')
            if telescope.k == 3 and telescope.mess == 1:
                print(telescope.mess)
                show_message(screen, MESSAGES[1][1])
            if bed.k == 3 and bed.mess == 1:
                show_message(screen, MESSAGES[2][1])
            if comp.k == 3 and comp.mess == 1:
                show_message(screen, MESSAGES[0][1])

        else:
            terminate()


#мяршрршршщр

        pygame.display.flip()
        clock.tick(28)


if __name__ == '__main__':
    print(start())
