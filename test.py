from MainController import ChooseAndPlay
from VkAudioPageLoader import VkFavePostLoader

__author__ = 'deffe'

import unittest


class VkFavePostLoaderTestCase(unittest.TestCase):
    def setUp(self):
        self.fave_posts = VkFavePostLoader()

    def test_first_of_faves(self):
        self.fave_posts.go_to_prev_page()
        self.fave_posts.go_to_prev_page()
        self.assertEqual(self.fave_posts.current_page['audios'][3]['artist'],
                         'Electric Wizard')

    def test_few_next(self):
        for i in range(16):
            self.fave_posts.go_to_next_page()
        self.assertEqual(self.fave_posts.current_page['audios'][0]['artist'],
                         'Whiplash')


if __name__ == '__main__':
    unittest.main()
