from curses import KEY_LEFT, KEY_RIGHT, KEY_UP, KEY_DOWN
from AudioDownload import download_audiolist
from AudioPlayer import MpdAudioPlayer
from VkAudioPageLoader import VkFavePostLoader, VkMyAudiosLoader, VkMyWallPostLoader
from GUI import WallPostView

from itertools import cycle


class ChooseAndPlay:
    def __init__(self):
        self.audio_player = MpdAudioPlayer()

        self.page_loaders = cycle([
            VkFavePostLoader(),
            VkMyAudiosLoader(),
            # VkMyWallPostLoader()
        ])
        self.current_page_loader = self.page_loaders.next()

    def print_pages(self, count=1):
        for _ in range(count):
            print self.current_page_loader.current_page['text']
            for a in self.current_page_loader.current_page['audios']:
                print(a)
            self.current_page_loader.go_to_next_page()
            print('----------')

    def show_pages(self):
        gui = WallPostView()
        bye = 0
        while not bye:
            page_to_display = self.current_page_loader.current_page
            button_pressed = gui.display(page_to_display)
            if button_pressed == KEY_DOWN:
                self.current_page_loader = self.page_loaders.next()
            if button_pressed == KEY_LEFT:
                self.current_page_loader.go_to_prev_page()
            if button_pressed == KEY_RIGHT:
                self.current_page_loader.go_to_next_page()
            if button_pressed == ord('q'):
                break
            if button_pressed == ord('p'):
                self.audio_player.add_audio(page_to_display['audios'])
                self.audio_player.play()
            if button_pressed == ord('a'):
                self.audio_player.add_audio(page_to_display['audios'], need_clear=False)
            if button_pressed == ord('d'):
                download_audiolist(
                    page_to_display['audios'], page_to_display['text'])
                gui.display_text('Download Completed')
                break

        gui.close()
        self._exit()

    def _exit(self):
        self.audio_player.close()
