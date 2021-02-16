import pygame
import requests
import sys
import os
req = requests.get(f'https://static-maps.yandex.ru/1.x/?ll={input("введите координаты объекта==>")}&spn='
                   f'{input("введите протяженность объекта==>")}&l=sat').content
with open('map.png', 'wb') as file:
    file.write(req)
if __name__ == '__main__':
    pygame.init()
    size = WIDTH, HEIGHT = 600, 450
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Map')
    im = pygame.image.load('map.png')
    os.remove('map.png')
    screen.blit(im, (0, 0))
    pygame.display.flip()
    while True:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
