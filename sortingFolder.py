import os
import shutil
import sys


def createFolder(folder_name, path):
    _fold_name = folder_name.replace(':', ' ').replace('.', ' ')
    _path = path

    if not (os.path.exists(_path + "/" + _fold_name)):
        os.chdir(_path)
        os.mkdir(_fold_name)


def checkAndMove(arr, folder_name, path, filename):
    if filename.split('.')[-1] in arr[1:]:
        createFolder(folder_name, path)
        try:
            shutil.move(path + '/' + filename, path + '/' + folder_name)
        except:
            print(filename + ' Файл с таким именем уже существует')


def main(path):
    # Create arrays in format: [Folder_name, File extensions...]
    # and add this array to 'arrays'

    _pictures = ['Pictures', 'jpg', 'jpeg', 'png', 'gif', 'JPEG', 'JPG']
    _video = ['Video', 'avi', 'mkv', 'mpg4']
    _music = ['Music', 'mp3', 'wav']
    _exe = ['Программы', 'exe', 'msi']
    _torrents = ['Torrents', 'torrent']
    _archives = ['Архивы', 'zip', 'rar', '7z']
    _docs = ['Documents', 'doc', 'docx', 'txt', 'pdf']
    arrays = [_pictures, _video, _music, _exe, _torrents, _archives, _docs]

    for filename in os.listdir(path):
        for item in arrays:
            checkAndMove(item, item[0], path, filename)


_dir = ''
if len(sys.argv) > 1:
    _dir = sys.argv[1]
else:
    print('Enter the path to folder \nError')
    exit()

main(_dir)
