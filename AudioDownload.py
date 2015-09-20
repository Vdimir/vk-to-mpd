# from gi.repository import Glib
import subprocess


def download_audiolist(audio_list, title_text):
    audio_path = get_save_path(title_text)

    command_list = []
    dload_script_name = '/tmp/dload.sh'
    dload_script_file = open(dload_script_name, 'w')

    dload_script_file.write("#!/bin/bash\n")
    dload_script_file.write("mkdir -p \"{audio_path}\"\n".format(audio_path=audio_path))

    for audio in audio_list:
        command = get_command_str(audio, audio_path)
        command_list.append(command)
        dload_script_file.write(command + '\n')

    dload_script_file.close()
    subprocess.Popen(['bash', dload_script_name]).wait()


def get_command_str(audio, audio_path):
    audio_name = u'{artist} - {title}'.format(
        title=audio['title'],
        artist=audio['artist'])\
        .replace('/', '')\
        .replace(' ', '_')

    url = audio['url'].split('?')[0]
    audio_ext = url[-3:]

    command = u'wget -O \"{audio_path}/{audio_name}.{audio_ext}\" \"{url}\"'.format(
        audio_path=audio_path,
        audio_name=audio_name,
        audio_ext=audio_ext,
        url=url).encode('utf-8')
    return command


def get_save_path(title_text):
    fpath_txt_name = '/tmp/vk_audio_path.txt'
    fpath_txt_file = open(fpath_txt_name, 'w')
    fpath_txt_file.write(title_text.encode('utf_8'))
    fpath_txt_file.close()

    subprocess.Popen(["vim", fpath_txt_name]).wait()

    fpath_txt_file = open(fpath_txt_name, 'r')
    audio_path = fpath_txt_file.readline()
    fpath_txt_file.close()
    audio_path = audio_path.strip()
    audio_path = audio_path.replace('\n', '')\
        .replace(' ', '_')\
        .replace('.', '_')
    # print(repr(audio_path))
    # audio_path = '/home/deffe/MyDoc/Music/'
    # audio_path = './foo/'
    return '/home/deffe/MyDoc/Music/' + audio_path
