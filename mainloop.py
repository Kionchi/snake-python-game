import pygame as pg
from random import randrange

def graj(points):
    window = 1000
    tile_size = 50
    range_vals = (tile_size // 2, window - tile_size // 2, tile_size)
    get_random_position = lambda: (randrange(*range_vals), randrange(*range_vals))

    snake = pg.Rect([0, 0], [tile_size-2, tile_size-2])
    snake.center = get_random_position()
    length = 1
    points = 0
    segments = [snake.copy()]
    snake_dir = (0, 0)
    time, time_step = 0, 110
    food = snake.copy()
    food.center = get_random_position()

    screen = pg.display.set_mode((window, window))
    clock = pg.time.Clock()
    dirs = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 1, pg.K_d: 1}
    game_over = False

    while not game_over:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_w and dirs[pg.K_w]:
                    snake_dir = (0, -tile_size)
                    dirs = {pg.K_w: 1, pg.K_s: 0, pg.K_a: 1, pg.K_d: 1}
                if event.key == pg.K_s and dirs[pg.K_s]:
                    snake_dir = (0, tile_size)
                    dirs = {pg.K_w: 0, pg.K_s: 1, pg.K_a: 1, pg.K_d: 1}
                if event.key == pg.K_a and dirs[pg.K_a]:
                    snake_dir = (-tile_size, 0)
                    dirs = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 1, pg.K_d: 0}
                if event.key == pg.K_d and dirs[pg.K_d]:
                    snake_dir = (tile_size, 0)
                    dirs = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 0, pg.K_d: 1}

        screen.fill('black')
        self_eat = pg.Rect.collidelist(snake, segments[:-1]) != -1
        if snake.left < 0 or snake.right > window or snake.top < 0 or snake.bottom > window or self_eat:
            snake.center, food.center = get_random_position(), get_random_position()
            game_over = True

        if snake.center == food.center:
            food.center = get_random_position()
            length += 1
            points += 1

        pg.draw.rect(screen, 'yellow', food)
        [pg.draw.rect(screen, 'pink', segment) for segment in segments]

        time_now = pg.time.get_ticks()
        if time_now - time > time_step:
            time = time_now
            snake.move_ip(snake_dir)
            segments.append(snake.copy())
            segments = segments[-length:]

        pg.display.flip()
        clock.tick(60)

    font = pg.font.Font("freesansbold.ttf", 72)
    game_over_text = font.render("Game Over", True, (255, 255, 255))
    game_over_rect = game_over_text.get_rect()
    game_over_rect.center = (window / 2, window / 2 - 100)

    points_text = font.render("Twoje punkty: " + str(points), True, (255, 255, 255))
    points_rect = points_text.get_rect()
    points_rect.center = (window / 2, window / 2)

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()
            elif event.type == pg.KEYDOWN:
                if event.key in (pg.K_w, pg.K_s, pg.K_a, pg.K_d):
                    return points

        screen.blit(game_over_text, game_over_rect)
        screen.blit(points_text, points_rect)
        pg.display.flip()
