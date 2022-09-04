import pygame 
import sys 

pygame.init()
(width, height) = (640, 500)
screen = pygame.display.set_mode((width, height))
background = pygame.image.load("bg1.jpg")
background = pygame.transform.scale(background, (width,height))
pygame.display.set_caption('World War Z')
screen.fill(background, (0,0))
pygame.display.flip()
running = True
while running:
  screen.blit(background, (100,100))
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False