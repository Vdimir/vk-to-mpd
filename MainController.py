from curses import KEY_LEFT, KEY_RIGHT, KEY_UP, KEY_DOWN
from AudioManager import MpdAudioPlayer
from VkAudioPageLoader import VkFavePostLoader, VkMyAudiosLoader
from GUI import WallPostView


class ChooseAndPlay:
    def __init__(self):
        self.audio_player = MpdAudioPlayer()
        self.fave_page_loader = VkFavePostLoader()
        self.myaudio_page_loader = VkMyAudiosLoader()

        self.page_loader = self.fave_page_loader

    def print_page(self):
        print self.page_loader.current_page['text']
        for a in self.page_loader.current_page['audios']:
            print(a)

    def show_pages(self):
        gui = WallPostView()
        bye = 0
        while not bye:
            page_to_display = self.page_loader.current_page
            button_pressed = gui.display(page_to_display)
            if button_pressed == KEY_UP:
                self.page_loader = self.fave_page_loader
            if button_pressed == KEY_DOWN:
                self.page_loader = self.myaudio_page_loader
            if button_pressed == KEY_LEFT:
                self.page_loader.go_to_prev_page()
            if button_pressed == KEY_RIGHT:
                self.page_loader.go_to_next_page()
            if button_pressed == ord('q'):
                break
            if button_pressed == ord('p'):
                self.audio_player.add_audio(page_to_display['audios'])
                self.audio_player.play()
            if button_pressed == ord('a'):
                self.audio_player.add_audio(page_to_display['audios'], clear=False)
        gui.close()
        self._exit()

    def _exit(self):
        self.audio_player.close()
