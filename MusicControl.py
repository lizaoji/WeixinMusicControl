from tools import *

def nextMusic(current_music, music_library):
    current_music_index = music_library.index(current_music)
    if current_music_index >=0 and current_music_index < len(music_library):
        next_music_index = current_music_index + 1
        playMusic(next_music_index,
