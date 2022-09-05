from tkinter import Y
import pygame 

# start pygame 
pygame.init()

# set demenisions of the screen/ surface
(width, height) = (900, 600)
screen = pygame.display.set_mode((width, height))

# title of screen 
pygame.display.set_caption('World War Z')

# new surface 
round1_surface = pygame.image.load("bg1.jpg")



# keeps game running until user hits "x" 
running = True
while running:
  for event in pygame.event.get():  # game runs as lone as its "TRUE"
    if event.type == pygame.QUIT: 
      running = False  
  
  
  screen.blit(round1_surface, (0,0))
  pygame.display.flip()
