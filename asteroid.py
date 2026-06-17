import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH

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
