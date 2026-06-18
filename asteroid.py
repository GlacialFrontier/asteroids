import pygame
import random
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event

# asteroid class
class Asteroid(CircleShape):
    # constructor Method
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius) # brings in parent constructor

    # asteroid draw method which overrides from Circle Shape
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width = LINE_WIDTH)

    # set asteroid sprite update method
    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        pygame.sprite.Sprite.kill(self)
        if self.radius <= ASTEROID_MIN_RADIUS: # do nothing if it was a small asteroid
            return
        else:
            log_event("asteroid_split")
            rand_angle: float = random.uniform(20, 50) # generate a random angle
            vector_pos = self.velocity.rotate(rand_angle) # make a positive trajectory for new astroid
            vector_neg = self.velocity.rotate(-rand_angle) # make a negative trajectory for new astroid
            new_radius = self.radius - ASTEROID_MIN_RADIUS # make new size of asteroids

            # create new smaller asteroids
            asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)

            # asteroid 1 changes direction & goes faster
            asteroid_1.velocity = vector_pos * 1.2
            
            asteroid_2.velocity = vector_neg * 1.2

