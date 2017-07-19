# 控制音乐播放的module
from tools import *
import random


def nextMusic(current_music, music_library):
    current_music_index = music_library.index(current_music)
    # 如果能找到歌曲
    if current_music_index >= 0 and current_music_index < len(music_library):
        # 下一首歌的序号，要特殊处理如果是最后一首歌的情况
        if current_music_index == len(music_library) - 1:
            next_music_index = 0
        else:
            next_music_index = current_music_index + 1
        playMusic(music_library[next_music_index]['file'])
    # 如果找不到歌，则从乐库里面随机挑一首播放
    else:
        randMusic(music_library)


def beforeMusic(current_music, music_library):
    current_music_index = music_library.index(current_music)
    # 如果能找到歌曲
    if current_music_index >= 0 and current_music_index < len(music_library):
        # 上一首歌的序号，要特殊处理如果是第一首歌的情况
        if current_music_index == 0:
            next_music_index = len(music_library) - 1
        else:
            next_music_index = current_music_index - 1
        playMusic(music_library[next_music_index]['file'])
    # 如果找不到歌，则从乐库里面随机挑一首播放
    else:
        randMusic(music_library)


def randMusic(music_library):
    playMusic(music_library[random.randint(0, len(music_library))]['file'])
