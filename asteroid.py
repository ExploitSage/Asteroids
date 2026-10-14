import random
import pygame
from logger import log_event
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
    
    def split(self) -> None:
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        log_event("asteroid_split")

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_angle = random.uniform(20, 50)
        a1_velocity = self.velocity.rotate(new_angle)
        a2_velocity = self.velocity.rotate(-new_angle)

        a1 = Asteroid(self.position.x, self.position.y, new_radius)
        a2 = Asteroid(self.position.x, self.position.y, new_radius)

        a1.velocity = a1_velocity*1.2
        a2.velocity = a2_velocity*1.2



    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position+=self.velocity * dt
