#!/usr/bin/python
from ChooseAndPlay import ChooseAndPlay

import sys

if __name__ == '__main__':
    sys.stderr = open('/tmp/vk_audio.log', 'w')
    main_controller = ChooseAndPlay()
    main_controller.show_pages()
    # main_controller.print_pages(2)

    print('Done!')
