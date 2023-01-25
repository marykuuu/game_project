
import pygame

from main import terminate, load_image

def instruct():
    pygame.init()
    size = width, height = 1050, 600
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('meowgame')

    intro_text = ["ВАМ НЕОБХОДИМО ВЫБРАТЬСЯ ИЗ КОМНАТЫ", "для воссоединения с другом",
                  "для передвижения используйте клавиши-стрелки на клавиатуре",
                  "для взаимодействия с предметами - клавишу пробел",
                  "<нажмите ПРОБЕЛ, чтобы начать>"]

    # fon = pygame.transform.scale(load_image('fon.jpg'), (width, height))
    # screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
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
