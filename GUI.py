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

    def display_text(self, text):
        self.myscreen.clear()
        self.myscreen.addstr(text)
        return self.myscreen.getch()

    def display(self, wall_post):
        self.myscreen.clear()
        title_string = "{number} {title}\n".format(number=10,
                                                   title=wall_post['text'][:150].replace("\n", " ")
                                                   .encode('utf_8'))
        self.myscreen.addstr(title_string, curses.A_BOLD)
        for ind, item in enumerate(wall_post['audios'], start=1):
            self.myscreen.addstr(u"[{i}] {artist} - {title}\n"
                                 .format(i=ind,
                                         title=item['title'],
                                         artist=item['artist'])
                                 .encode('utf_8'))

        self.myscreen.refresh()
        return self.myscreen.getch()

    def close(self):
        curses.echo()
        curses.nocbreak()
        curses.endwin()
