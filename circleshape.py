import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    containers: tuple[pygame.sprite.Group, ...]

    def __init__(self, x: float, y: float, radius: float) -> None:
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(*self.containers)
        else:
            super().__init__()

        self.position: pygame.Vector2 = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen: pygame.Surface) -> None:
        # must override
        pass

    def update(self, dt: float) -> None:
        # must override
        pass

    # Method to check if objects are colliding with each other
    def collides_with(self, other: object) -> bool:
        obj_hit_dist = self.radius + other.radius
        obj_dist = self.position.distance_to(other.position)
        return obj_dist < obj_hit_dist