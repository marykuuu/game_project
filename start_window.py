import pygame
from main import terminate, load_image


def start_screen():
    pygame.init()
    size = width, height = 1050, 600
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('meowgame')
    intro_text = ["TRY TO ESCAPE", "<нажмите, чтобы продолжить>"]

    fon = pygame.transform.scale(load_image('back.jpg'), (width, height))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 100)
    string_rendered = font.render(intro_text[0], 1, pygame.Color('white'))
    intro_rect = string_rendered.get_rect()
    intro_rect.x = 90
    text_coord = 80
    intro_rect.top = text_coord
    screen.blit(string_rendered, intro_rect)
    font = pygame.font.Font(None, 50)
    string_rendered = font.render(intro_text[1], 1, pygame.Color('pink'))
    intro_rect = string_rendered.get_rect()
    intro_rect.x = 350
    text_coord = 180
    intro_rect.top = text_coord
    screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:#event.type == pygame.KEYDOWN or
                return 'play'
        pygame.display.flip()

if __name__ == '__main__':
    print(start_screen())
