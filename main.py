import pygame
import requests
import sys
import os


def write_image():
    req = requests.get(f'https://static-maps.yandex.ru/1.x/?ll={coords}&z='
                       f'{zoom}&l=sat')
    with open('map.png', 'wb') as file:
        file.write(req.content)
    im = pygame.image.load('map.png')
    screen.blit(im, (0, 0))


if __name__ == '__main__':
    coords = input("введите координаты объекта==>")
    zoom = int(input("введите масштаб карты==>"))
    pygame.init()
    size = WIDTH, HEIGHT = 600, 450
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Map')
    write_image()
    fps = 50
    clock = pygame.time.Clock()
    while True:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                os.remove('map.png')
                pygame.quit()
                sys.exit()
            if i.type == pygame.KEYDOWN and i.key == pygame.K_PAGEUP:
                if zoom < 13:
                    zoom += 1
                write_image()
            if i.type == pygame.KEYDOWN and i.key == pygame.K_PAGEDOWN:
                if zoom > 1:
                    zoom -= 1
                write_image()
        clock.tick(50)
        pygame.display.flip()
