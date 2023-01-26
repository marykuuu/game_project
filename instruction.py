
import pygame

from main import terminate, load_image

def instruct():
    pygame.init()
    size = width, height = 1050, 600
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('meowgame')

    text = ["ВАМ НЕОБХОДИМО ВЫБРАТЬСЯ ИЗ КОМНАТЫ",
                  "для передвижения используйте клавиши-стрелки на клавиатуре",
                  "для взаимодействия с предметами - клавишу пробел",
                  "<нажмите ПРОБЕЛ, чтобы начать>"]

    fon = pygame.transform.scale(load_image('instr_fon.jpg'), (width, height))
    screen.blit(fon, (0, 0))

    for i in range(len(text)):
        if i == 0:
            size = 53
            font = pygame.font.Font(None, size)
            string_rendered = font.render(text[i], 1, (193, 0 ,0))
            intro_rect = string_rendered.get_rect()
            intro_rect.top = 50
            intro_rect.x = 150
            screen.blit(string_rendered, intro_rect)
        if i == 1:
            size = 35
            font = pygame.font.Font(None, size)
            string_rendered = font.render(text[i], 1, (255, 255, 255))
            intro_rect = string_rendered.get_rect()
            intro_rect.top = 200
            intro_rect.x = 200
            screen.blit(string_rendered, intro_rect)
        if i == 2:
            size = 35
            font = pygame.font.Font(None, size)
            string_rendered = font.render(text[i], 1, (255, 255, 255))
            intro_rect = string_rendered.get_rect()
            intro_rect.top = 300
            intro_rect.x = 200
            screen.blit(string_rendered, intro_rect)
        if i == 3:
            size = 60
            font = pygame.font.Font(None, size)
            string_rendered = font.render(text[i], 1, (200, 191,131))
            intro_rect = string_rendered.get_rect()
            intro_rect.top = 500
            intro_rect.x = 50
            screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:

                return 'play'
        pygame.display.flip()

if __name__ == '__main__':
    print(instruct())
