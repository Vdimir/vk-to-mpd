
from curses import KEY_LEFT, KEY_RIGHT
import subprocess
from AudioManager import AudioPlayer
from VkLoader import VkPostLoader
from GUI import WallPostView


class ChooseAndPlay:
    def __init__(self):
        self.audio_player = AudioPlayer()
        self.gui = WallPostView()
        self.fave_posts_loader = VkPostLoader()
        self.current_page = 0

    def loop(self):
        bye = 0
        stastusbar_text = ""
        while not bye:
            page_to_display = self.fave_posts_loader.get_page(self.current_page)
            button_pressed = self.gui.display(page_to_display)
            if button_pressed == KEY_LEFT:
                self.dec_cur_page()
            if button_pressed == KEY_RIGHT:
                self.inc_cur_page()
            if button_pressed == ord('q'):
                break
            if button_pressed == ord('Q'):
                break
            if button_pressed == ord('p'):
                self.audio_player.add_audio(page_to_display.get_audios())
                self.audio_player.play()

    def inc_cur_page(self):
            self.current_page += 1

    def dec_cur_page(self):
            self.current_page = max(0, self.current_page-1)

    def exit(self):
        self.gui.close()
        self.audio_player.close()
        subprocess.call(["ncmpc"])
