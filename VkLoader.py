from WallPostModel import WallPostModel
import vk

token = "df5761648d0e1e94e61255212f0022a20b6fa013b21b909aefebf654e98a6358056fb1608fc837b662c04"
vkapi = vk.API(access_token=token, timeout=5)


class VkPostLoader:
    def __init__(self):
        self.load_by = 5
        self.pages = []
        self.current_loaded_page = 0

    def load_more(self):
        vk_fave_posts = vkapi.fave.getPosts(count=self.load_by, offset=self.current_loaded_page * self.load_by)
        for vk_wall_post in vk_fave_posts['items']:
            wp = WallPostModel(vk_wall_post)
            if wp.is_audio():
                self.pages.append(wp)
        self.current_loaded_page += 1

    def get_page(self, ind):
        while ind >= len(self.pages):
            self.load_more()
        return self.pages[ind]
