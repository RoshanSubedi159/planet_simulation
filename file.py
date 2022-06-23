from ast import While
import pygame
import math

pygame.init()

WIDTH, HEIGHT = 600, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Planet Simulation")

WHITE = (255, 255, 255)


class Planet:
    AU = 149.6e6 * 1000
    G = 6.67428e-11
    SCALE = 250 / AU  # 1AU = 100px
    TIMESTEP = 3600 * 24  # 1 day

    def __init__(self, x, y, radius, color, mass):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass

        self.orbit = []
        self.sun = False
        self.distance_to_sun = 0

        self.x_vel = 0
        self.y_vel = 0


def main():
    run = True
    clock = pygame.time.Clock()

    while(run):
        clock.tick(60)
        # WIN.fill(WHITE)
        # pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    pygame.quit()


main()
