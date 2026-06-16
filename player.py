import pygame
from constants import *
from circleshape import *

class Player(CircleShape):
    def __init__(self, x: int, y: int):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

        # in the Player class
    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    # override draw from circleshape
    def draw(self, screen: object):
        pygame.draw.polygon(screen, "White", self.triangle(), width = LINE_WIDTH)

    # rotates player
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    # move player
    def move (self, dt):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector



    def update(self, dt: float) -> None:
        keys = pygame.key.get_pressed()

        # rotate counter-clockwise if 'a' is pressed
        if keys[pygame.K_a]:
            self.rotate(-dt)

        # rotate clockwise if 'd' is pressed
        if keys[pygame.K_d]:
            self.rotate(dt)

        # move forwards if 'w' is pressed
        if keys[pygame.K_w]:
            self.move(dt)

        # move backwards if 's' is pressed
        if keys[pygame.K_s]:
            self.move(-dt)

