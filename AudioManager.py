import mpd


class MpdAudioPlayer:
    def __init__(self):
        self.mpd_client = mpd.MPDClient()
        self.mpd_client.connect("localhost", 6600)

    def add_audio(self, audio_list):
        """
        :param audio_list: dict contains 'url', 'title', 'artist'
        :return:
        """
        self.mpd_client.clear()
        for song in audio_list:
            url = song['url'].split('?')[0]
            songid = self.mpd_client.addid(url)
            self.mpd_client.addtagid(songid, 'title', song['title'])
            self.mpd_client.addtagid(songid, 'artist', song['artist'])

    def play(self):
        self.mpd_client.play()

    def pause(self):
        self.mpd_client.pause()

    def close(self):
        self.mpd_client.close()
        self.mpd_client.disconnect()

