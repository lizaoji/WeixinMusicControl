
import pygame,sys

pygame.init()
pygame.mixer.init()
screen=pygame.display.set_mode([640,480])
path = 'C:\\Users\\29076\\Music\\My Love - Westlife.mp3'
pygame.mixer.music.load(path)
pygame.mixer.music.play()
while 1:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()

