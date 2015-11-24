import vk
import os



def pull_audio_from_wall_post(vk_wall_post):
    att_list = vk_wall_post.get('attachments')
    audio_list = []
    if att_list is not None:
        for attachment in att_list:
            audio = attachment.get('audio')
            if audio is not None:
                audio_list.append(audio)
    return audio_list


def load_access_token_from_file():
    file_path = "{dir}/{fname}".format(dir=os.path.dirname(os.path.abspath(__file__)),
                                       fname="access_token")
    fin = open(file_path)
    text_data = fin.read()
    fin.close()
    return text_data.strip()


token = load_access_token_from_file()
vkapi = vk.API(access_token=token, timeout=5)


class VkAudioPageLoader:
    def __init__(self):
        self._pages = []
        self._load_pages_by = 5
        self._current_loaded_page = 0
        self._current_showed_page = 0

    @property
    def current_page(self):
        while self._current_showed_page >= len(self._pages):
            self._load_more()
        return self._pages[self._current_showed_page]

    def go_to_next_page(self):
        self._current_showed_page += 1

    def go_to_prev_page(self):
        self._current_showed_page = max(0, self._current_showed_page - 1)

    def _load_more(self):
        raise NotImplementedError


class VkFavePostLoader(VkAudioPageLoader):
    def __init__(self):
        VkAudioPageLoader.__init__(self)

    def _load_more(self):
        vk_fave_posts = vkapi.fave.getPosts(count=self._load_pages_by,
                                            offset=self._current_loaded_page * self._load_pages_by)
        for vk_wall_post in vk_fave_posts['items']:
            wp = {
                'text': vk_wall_post['text'],
                'audios': pull_audio_from_wall_post(vk_wall_post)
            }
            if wp['audios']:
                self._pages.append(wp)
        self._current_loaded_page += 1


class VkMyWallPostLoader(VkAudioPageLoader):
    def __init__(self):
        VkAudioPageLoader.__init__(self)

    def _load_more(self):
        vk_fave_posts = vkapi.wall.get(count=self._load_pages_by,
                                       offset=self._current_loaded_page * self._load_pages_by,
                                       filter='all')
        for t in vk_fave_posts['items']:
            vk_wall_post_copy_hist = t.get('copy_history')
            if vk_wall_post_copy_hist is None:
                continue
            vk_wall_post = vk_wall_post_copy_hist[0]
            wp = {
                'text': vk_wall_post['text'],
                'audios': pull_audio_from_wall_post(vk_wall_post)
            }
            if wp['audios']:
                self._pages.append(wp)
        self._current_loaded_page += 1


class VkMyAudiosLoader(VkAudioPageLoader):
    def __init__(self):
        VkAudioPageLoader.__init__(self)

    def _load_more(self):
        loaded_data = vkapi.audio.get(count=self._load_pages_by,
                                      offset=self._current_loaded_page * self._load_pages_by)

        for vk_audio in loaded_data['items']:
            wp = {
                'text': '',
                'audios': [vk_audio]
            }
            self._pages.append(wp)

        self._current_loaded_page += 1
