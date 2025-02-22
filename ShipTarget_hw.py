import itertools
import pgzrun
import pygame

WIDTH = 400
HEIGHT = 400

MEDALLION_POSITIONS = [
    (500,500),
    (500,230),
    (230,230),
    (230,500),
]
medallion_positions = itertools.cycle(MEDALLION_POSITIONS)

medallion = Actor('medallion', center= (500,500)) 

medallion.scale=0.01
medallion._surf = pygame.transform.scale(medallion._surf, (100,100))
medallion._update_pos()

def draw():
    screen.clear()
    medallion.draw()


def move_medallion():
    animate(
        medallion,
        'bounce_end',
        duration = 1,
        pos = next(medallion_positions)
    )



move_medallion()
clock.schedule_interval(move_medallion, 2)



pgzrun.go()