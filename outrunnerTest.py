import pygame
import math

pygame.init()

#define colors
BLACK = (0,0,0)
FLOORBLUE = (57,0,158)
ROADGRAY = (100, 100, 100)
TEXTPINK = (239,33,95)

size = (800, 600)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("A E S T H E T I C")

def drawSky(offset):
    #copy-pasted from drawFloor(), works exactly the same way
    colorOffset = 0
    for x in range(300):
        if(x % 20 == 0):
            pygame.draw.line(screen, (255, 255-colorOffset, 200), [0, x+15-offset], [800, x+15-offset], 2)
            colorOffset += 10

def drawSun():
    #an absolute nightmare. Still isnt a perfect semicircle, hours of math later.
    colorOffset = 0
    for len in range(0, 100, 10):
        circOff = (math.acos(len/100))/.0101
        pygame.draw.line(screen, BLACK, [400+circOff, 300-len], [400-circOff, 300-len], 5)
    for len in range(0, 100, 10):
        circOff = (math.acos(len/100))/.0101
        pygame.draw.line(screen, (255, 100+colorOffset, 40), [400+circOff, 295-len], [400-circOff, 295-len], 5)
        colorOffset+= 13

def drawFloor(offset):
    #designed to draw one single floor line at a time, movement is handled by the caller.
    dist = 300+offset                                                   #distance from horizon line
    pygame.draw.line(screen, FLOORBLUE, [0, dist], [800, dist], 3)      #draw the line at appropriate distance
    drawRoad()                                                          #overlay the asphalt
    for y in range(801):                                                #draw road guides for perspective
        if y%40 == 0:
            pygame.draw.line(screen, ROADGRAY, [400, 300], [y, 600], 1)

def drawRoad():
    #draws in asphalt to cover ground movement on road
    for z in range(801):
        pygame.draw.line(screen, BLACK, [400,300],[z,600], 2)           #just blacks everything out behind guides

def drawText(offset, sizemod, message):
    #desgined to print cool futuristic text to say 'Technology' or 'Computers' or something
    if offset < 0 or offset > 300:
        return
    else:
        font = pygame.font.SysFont('Lucidia Console', sizemod, True, False)
        text = font.render(str(message),True,TEXTPINK)
        screen.blit(text, [400, 300+offset])                            #draws text, movement handled by caller

done = False                                                            #game loop bookeeping
                                                                        #
clock = pygame.time.Clock()                                             #

runOffset = 0                                                           #keeps track of time for movement

while (not done) and runOffset < 300:                                   #runs for 50 seconds or until closed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True                                                 #application exit handling

    
    screen.fill(BLACK)                                                  #clear screen before render

    drawSky(runOffset/2 % 20)                                           #sky is backmost layer
    drawSun()                                                           #sun goes in sky (revolutionary, I know)
    
    runOffset += 1                                                      #advance time to separate ground from sky
    
    for x in range(301):
        if x%15 == 0:
            drawFloor(x+runOffset%15)                                   #draw groundlines, this handles movement

    #if runOffset % 150 == 0:                                           #failed experiment
        #if (runOffset/150)%3 == 0:
            #drawText(runOffset, 25, "Technology")
        #elif(runOffset/150)%3 == 1:
            #drawText(runOffset, 25, "Computers")
        #else:
            #drawText(runOffset, 25, "Cyberspace")
    drawText(runOffset, runOffset, "Technology")                        #cool 'Technology' moving text
    pygame.display.flip()                                               #show the frame

    clock.tick(60)                                                      #lock to 60 fps



pygame.quit()
