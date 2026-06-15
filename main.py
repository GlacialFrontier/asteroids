import pygame
from constants import *
from logger import log_state

def main():
    # initialize pygame
    pygame.init()

    # initialize clock
    clock = pygame.time.Clock()
    dt = 0.0

    # draw the new GUI
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # game loop
    while True:

        # set logs
        log_state()

        # event queue start
        for event in pygame.event.get():
            pass

        # set screen to black
        screen.fill("black")

        # refresh screen
        pygame.display.flip()

        dt = clock.tick(60) / 1000  
        
        
        # make quit button active
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
if __name__ == "__main__":
    main()
