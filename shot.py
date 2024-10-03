from constants import SHOT_RADIUS, PLAYER_SHOOT_SPEED
from circleshape import CircleShape
import pygame

class Shot(CircleShape):
    def __init__(self, x,y):
        super().__init__(x, y, SHOT_RADIUS)
        self.x = x
        self.y = y
        self.radius = SHOT_RADIUS
        self.rotation = 0

    def draw(self,screen):
        pygame.draw.circle(screen,"red",self.position,SHOT_RADIUS)

    def update(self,dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SHOOT_SPEED * dt

