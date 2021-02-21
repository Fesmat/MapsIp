import pygame
import requests
import sys
import os
import pygame_widgets


def write_image():
    req = requests.get(f'https://static-maps.yandex.ru/1.x/?ll={coords}&z='
                       f'{zoom}&l={views[now]}')
    with open('map.png', 'wb') as file:
        file.write(req.content)
    im = pygame.image.load('map.png')
    screen.blit(im, (0, 0))


if __name__ == '__main__':
    coords = input("введите координаты объекта==>")
    zoom = int(input("введите масштаб карты==>"))
    left, right = None, None
    pygame.init()
    size = WIDTH, HEIGHT = 600, 450
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Map')
    font = pygame.font.SysFont('tahoma', 30)
    views = ['sat', 'map', 'sat,skl']
    now = 0


    def change_view():
        global now
        now = (now + 1) % 3
        write_image()


    button_play = pygame_widgets.Button(
        screen, 125, 320, 300, 50, text='Изменить тип',
        fontSize=50,
        inactiveColour=(255, 204, 219),
        pressedColour=(255, 204, 219),
        onClick=change_view,
        textColour=(0, 0, 0),
        hoverColour=(255, 204, 219),
        font=font,
        textHAlign='centre'
    )
    write_image()
    fps = 50
    clock = pygame.time.Clock()
    while True:
        events = pygame.event.get()
        for i in events:
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
            if i.type == pygame.KEYDOWN and i.key == pygame.K_LEFT:
                coords = list(map(float, coords.split(',')))
                coords[0] -= 10 / zoom
                if coords[0] < -180:
                    coords[0] += 10 / zoom
                coords = ','.join(map(str, coords))
                write_image()
            if i.type == pygame.KEYDOWN and i.key == pygame.K_RIGHT:
                coords = list(map(float, coords.split(',')))
                coords[0] += 10 / zoom
                if coords[0] > 180:
                    coords[0] -= 10 / zoom
                coords = ','.join(map(str, coords))
                write_image()
            if i.type == pygame.KEYDOWN and i.key == pygame.K_UP:
                coords = list(map(float, coords.split(',')))
                coords[1] += 10 / zoom
                if coords[1] > 90:
                    coords[0] -= 10 / zoom
                coords = ','.join(map(str, coords))
                write_image()
            if i.type == pygame.KEYDOWN and i.key == pygame.K_DOWN:
                coords = list(map(float, coords.split(',')))
                coords[1] -= 10 / zoom
                if coords[1] < -90:
                    coords[1] += 10 / zoom
                coords = ','.join(map(str, coords))
                write_image()
            button_play.listen(events)
            button_play.draw()
        clock.tick(50)
        pygame.display.flip()
