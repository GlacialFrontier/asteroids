import pygame
import sys
from constants import *
from logger import log_state, log_event
from player import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


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
    asteroids = pygame.sprite.Group() # Asteroids
    shots = pygame.sprite.Group() # Bullets

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (drawable, updatable, shots)
    player = Player(x, y)
    asteroid_field = AsteroidField()

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

        # collision check
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game Over!")
                sys.exit()

        # draw player
        for sprite in drawable:
            sprite.draw(screen)

        # refresh screen
        pygame.display.flip()

        dt = clock.tick(60) / 1000  
        
        
        
            
if __name__ == "__main__":
    main()
