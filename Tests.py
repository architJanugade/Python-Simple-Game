import pygame

pygame.init()
pygame.display.set_mode([800,600])
pygame.mouse.set_visible(True)
gameExit = False
while not gameExit:
    for event in pygame.event.get():
        print(pygame.mouse.get_pos())
