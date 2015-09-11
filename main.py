#!/usr/bin/python
from MainController import ChooseAndPlay

import subprocess

if __name__ == '__main__':

    main_controller = ChooseAndPlay()
    main_controller.show_pages()
    # main_controller.print_page()

    subprocess.call(["ncmpc"])
    print('Done!')