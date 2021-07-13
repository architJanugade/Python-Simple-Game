import pygame
import random , sys , math , fractions

pygame.init()

red = (255 ,0 ,0)
white = (255,255,255)
black = (0,0,0)

display_width = 800
display_height = 600

radius = 50
diameter = radius * 2
randX = 370
randY = 300


#print(randX,randY)

#distance = randX - ousePos[]



clock = pygame.time.Clock()


gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.mouse.set_visible(True)
pygame.display.set_caption('AimBooster')




gameExit = False

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True

        
           
            
            
    gameDisplay.fill(white)
    pygame.draw.circle(gameDisplay , red , [randX ,randY] , radius)
    
    pygame.display.update()

    mousePos = pygame.mouse.get_pos()
    mouseX = mousePos[0]
    mouseY = mousePos[1]
    
    sq1 = (mouseX - randX) * (mouseX - randX)
    sq2 = (mouseY - randY) * (mouseY - randY)
    distance = math.sqrt(sq1 + sq2)
    print(mouseX,mouseY)
    print(randX,randY)

    if distance <= radius:
        for event in pygame.event.get():
            print('hey you are in')
            if event.type == pygame.MOUSEBUTTONUP:
                print('clicked')
                randX = random.randrange(diameter , display_width-radius)
                randY = random.randrange(diameter , display_height-radius)
                pygame.draw.circle(gameDisplay , red ,[randX ,randY] , radius)
        
    clock.tick(15)

pygame.quit()
quit()

    

