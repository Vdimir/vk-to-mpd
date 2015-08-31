import curses
import locale


class WallPostView:
    def __init__(self):
        locale.setlocale(locale.LC_ALL, '')
        self.myscreen = curses.initscr()
        self.myscreen.keypad(1)
        curses.noecho()
        curses.cbreak()
        curses.curs_set(0)

    def display(self, wall_post):
        self.myscreen.clear()
        self.myscreen.addstr(" {title}\n".format(title=wall_post.get_title()),
                             curses.A_BOLD)
        for ind, item in enumerate(wall_post.get_playlist(), start=1):
            self.myscreen.addstr("[{i}] {text}\n".format(i=ind, text=item))

        self.myscreen.refresh()
        return self.myscreen.getch()

    def close(self):
        curses.echo()
        curses.nocbreak()
        curses.endwin()
