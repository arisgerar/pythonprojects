import curses
import time
import random

def game(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(True)

    dino_y = 0
    jumping = False
    jump_time = 0

    cactus_x = 40
    score = 0

    while True:
        # Read key
        key = stdscr.getch()

        if key == ord(" ") and not jumping:
            jumping = True
            jump_time = 5

        # Jump physics
        if jumping:
            dino_y = jump_time
            jump_time -= 1

            if jump_time < 0:
                jumping = False
                dino_y = 0

        # Move cactus
        cactus_x -= 1

        if cactus_x <= 0:
            cactus_x = 40
            score += 1

        # Draw screen
        stdscr.clear()

        stdscr.addstr(0, 0, f"Score: {score}")

        # Draw dino
        stdscr.addstr(10 - dino_y, 5, "D")

        # Draw cactus
        stdscr.addstr(10, cactus_x, "#")

        # Ground
        stdscr.addstr(11, 0, "-" * 50)

        # Collision
        if cactus_x == 5 and dino_y == 0:
            stdscr.addstr(5, 15, "GAME OVER")
            stdscr.refresh()
            time.sleep(2)
            break

        stdscr.refresh() 
        time.sleep(0.1)

curses.wrapper(game) 