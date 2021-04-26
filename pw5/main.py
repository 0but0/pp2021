from domains.Menu import menu
import curses

if __name__ == "__main__":
    cu = curses.initscr()
    p = menu()
    p.engine()