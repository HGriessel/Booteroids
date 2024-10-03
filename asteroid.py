import circleshape
import pygame
from constants import ASTEROID_MIN_RADIUS,ASTEROID_SPAWN_RATE,ASTEROID_MAX_RADIUS
import random

class Asteroid(circleshape.CircleShape):
    def __init__(self, x,y,raduis):
        super().__init__(x, y, raduis)
        self.x = x
        self.y = y
        self.radius = raduis

    def draw(self,screen):
        pygame.draw.circle(screen,"green",self.position,self.radius,width=2)

    def update(self,dt):
        forward = pygame.Vector2(0, 1)
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return 
        else:
            split_angle = random.uniform(20,50)

            rotation_1 = self.velocity.rotate(split_angle)
            asteroid_1 = Asteroid(
                            self.position.x,
                            self.position.y,
                            self.radius - ASTEROID_MIN_RADIUS
                            )
            asteroid_1.velocity = rotation_1 * 1.3

            rotation_2 = self.velocity.rotate(-split_angle)
            asteroid_2 = Asteroid(
                            self.position.x,
                            self.position.y,
                            self.radius - ASTEROID_MIN_RADIUS
                            )
            asteroid_2.velocity = rotation_2 * 1.3
