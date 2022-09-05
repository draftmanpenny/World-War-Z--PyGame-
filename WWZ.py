import pygame 

# start pygame 
pygame.init()

# set demenisions of the screen/ surface
(width, height) = (900, 600)
screen = pygame.display.set_mode((width, height))

# title of screen 
pygame.display.set_caption('World War Z')

# new surface 
round1_surface = pygame.image.load('bg1.jpg').convert_alpha()
soldier_surface = pygame.image.load('soldier.png').convert_alpha()
zombie1_surface = pygame.image.load('zombie1.png').convert_alpha()
bullet = pygame.image.load('bullet.png').convert_alpha()
bullet_x_postion = 375


zombie1_x_pos = 900  # the starting postion of the zombie... width is the refrence for postion on screen 
#zombie2_surface = pygame.image.load('zombie2.png')


# game loop - keeps game running until user hits "x" 
running = True
while running:
  for event in pygame.event.get():  # game runs as lone as its "TRUE"
    if event.type == pygame.QUIT: 
      running = False  
  
  # places images on screen  
  screen.blit(round1_surface, (0,0))
  screen.blit(soldier_surface, (300,400))
  screen.blit(bullet, (bullet_x_postion,416))
  screen.blit(zombie1_surface, (zombie1_x_pos,400))
  zombie1_x_pos -= 1.5  # adjust the width postion of the zombie creating movement
  if zombie1_x_pos < -100:
     zombie1_x_pos = 900
  else: 
    pass
  if event.type == pygame.KEYDOWN: 
    if event.key == pygame.K_SPACE: 
        bullet_x_postion -= 2
    else: 
        pass

  #screen.blit(zombie2_surface, (700,400))
  pygame.display.flip()
