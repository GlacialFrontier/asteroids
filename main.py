import pygame
from constants import *
from logger import log_state
from player import *


def main():
    # initialize pygame
    pygame.init()

    # initialize clock
    clock = pygame.time.Clock()
    dt = 0.0

    # draw the new GUI
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    
    # player info
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    
    # groups
    updatable = pygame.sprite.Group() # Sprites that can be updated
    drawable = pygame.sprite.Group() # Sprites that can be drawn
    Player.containers = (updatable, drawable)
    player = Player(x, y)

    # game loop
    while True:

        # set logs
        log_state()

        # make quit button active
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # event queue start
        for event in pygame.event.get():
            pass

        # set screen to black
        screen.fill("black")

        # check rotation
        updatable.update(dt)

        # draw player
        for sprite in drawable:
            sprite.draw(screen)

        # refresh screen
        pygame.display.flip()

        dt = clock.tick(60) / 1000  
        
        
        
            
if __name__ == "__main__":
    main()
