class WallPostModel:
    def __init__(self, vk_wall_post):

        self.title = vk_wall_post['text']
        att_list = vk_wall_post.get('attachments')
        self.audios = []
        if att_list is None:
            return
        for attachment in att_list:
            audio = attachment.get('audio')
            if audio is not None:
                self.audios.append(audio)

    def is_audio(self):
        if self.audios:
            return True
        return False

    def get_audios(self):
        return self.audios

    def get_playlist(self):
        result = []
        for song in self.audios:
            result.append(u"{artist} - {title}".format(title=song['title'], artist=song['artist']).encode('utf_8'))
        return result

    def get_title(self):
        return self.title[:150].replace("\n", " ").encode('utf_8')
