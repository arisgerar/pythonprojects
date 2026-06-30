import curses
import time

def main(stdscr):
    text = ""
    stdscr.nodelay(True)

    while True:
        key = stdscr.getch()

        if key != -1:
            if key in (curses.KEY_BACKSPACE, 127, 8):
                text = text[:-1]  # delete last character
            else:
                text += chr(key)

        print("\r" + text + " " * 10, end="", flush=True)

        time.sleep(0.05)

curses.wrapper(main)