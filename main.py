import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys

def main():
    print(f"Starting asteroids!\nScreen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    xp = SCREEN_WIDTH / 2
    yp = SCREEN_HEIGHT / 2

    drawable = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots =  pygame.sprite.Group()

    AsteroidField.containers = (updatable)
    asteroid_field  = AsteroidField()

    Player.containers = (drawable, updatable)
    Shot.containers = (drawable, updatable, shots)
    player = Player(xp,yp)

    Asteroid.containers = (drawable, updatable, asteroids)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((1,1,0))
        for item_u in updatable:
            item_u.update(dt)

        for asteroid in asteroids:
            if asteroid.isColiding(player):
                print("GAME OVER!")
                sys.exit()

            for shot in shots:
                if asteroid.isColiding(shot):
                    shot.kill()
                    asteroid.split()
                

        for item_d in drawable:
            item_d.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()


