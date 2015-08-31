from WallPostModel import WallPostModel
import vk
import os

def get_acces_token_from_file():
    ac_file = "{dir}/{fname}".format(dir=os.path.dirname(os.path.abspath(__file__)), fname="access_token")
    fin = open(ac_file)
    token = fin.read()
    fin.close()
    return token

token = get_acces_token_from_file()
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
