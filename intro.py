import sqlite3
import pygame

from main import terminate, load_image


def intro(k=1):
    pygame.init()
    size = width, height = 1050, 600
    screen = pygame.display.set_mode(size)




    con = sqlite3.connect('introduction.sqlite')
    cur = con.cursor()
    result = cur.execute("""SELECT * FROM story
                                        WHERE num = ?""", (1,)).fetchall()[0]
    fon = pygame.transform.scale(load_image(result[1]), (width, height))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 50)
    string_rendered = font.render(result[2], 1, pygame.Color('white'))
    intro_rect = string_rendered.get_rect()
    intro_rect.x = 150
    text_coord = 400
    intro_rect.top = text_coord
    screen.blit(string_rendered, intro_rect)



    string_rendered = font.render(result[3], 1, pygame.Color('white'))
    intro_rect = string_rendered.get_rect()
    intro_rect.x = 260
    text_coord = 450
    intro_rect.top = text_coord
    screen.blit(string_rendered, intro_rect)



    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                k += 1
                if k < 4:

                    result = cur.execute("""SELECT * FROM story
                                        WHERE num = ?""", (k,)).fetchall()[0]
                    fon = pygame.transform.scale(load_image(result[1]), (width, height))
                    screen.blit(fon, (0, 0))
                if k == 2:
                    font = pygame.font.Font(None, 50)
                    string_rendered = font.render(result[2], 1, pygame.Color('white'))
                    intro_rect = string_rendered.get_rect()
                    intro_rect.x = 400
                    text_coord = 500
                    intro_rect.top = text_coord
                    screen.blit(string_rendered, intro_rect)
                if k == 3:
                    font = pygame.font.Font(None, 50)
                    string_rendered = font.render(result[2], 1, pygame.Color('white'))
                    intro_rect = string_rendered.get_rect()
                    intro_rect.x = 30
                    text_coord = 40
                    intro_rect.top = text_coord
                    screen.blit(string_rendered, intro_rect)

                    font = pygame.font.Font(None, 50)
                    string_rendered = font.render(result[3], 1, pygame.Color('white'))
                    intro_rect = string_rendered.get_rect()
                    intro_rect.x = 50
                    text_coord = 80
                    intro_rect.top = text_coord
                    screen.blit(string_rendered, intro_rect)

                    font = pygame.font.Font(None, 50)
                    string_rendered = font.render(result[4], 1, pygame.Color('white'))
                    intro_rect = string_rendered.get_rect()
                    intro_rect.x = 60
                    text_coord = 120
                    intro_rect.top = text_coord
                    screen.blit(string_rendered, intro_rect)

                    font = pygame.font.Font(None, 50)
                    string_rendered = font.render(result[5], 1, pygame.Color('white'))
                    intro_rect = string_rendered.get_rect()
                    intro_rect.x = 450
                    text_coord = 160
                    intro_rect.top = text_coord
                    screen.blit(string_rendered, intro_rect)

                if k == 4:
                    return 'play'

        pygame.display.flip()

intro()