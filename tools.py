from platform import system
import os
import re

#根据平台设置路径
def judgePlatform():
    k = system()
    # mac系统
    if k == 'Darwin':
        music_dir = "/Users/lizaoji/Music/网易云音乐/"
    elif k == 'Windows':
        music_dir = "C:\\Users\\29076\\Music"
    return k, music_dir

#播放音乐，直接调用系统里面的播放器
def playMusic(index, search_result, music_dir, platform):
    if type(index) == str and index.isdigit():
        index = int(index)
    if index >= 1 and index <= len(search_result):
        index -= 1
        if platform == 'Windows':
            k = music_dir + "\\" + '"' + search_result[index]['file'] + '"'
            os.system(k)
        elif platform == 'Darwin':
            k = music_dir + '"' + search_result[index]['file'] + '"'
            os.system("open " + k)
        #播放成功，返回播放的音乐名字
        return search_result[index]['file']
    else:
        #播放失败，返回None
        return None


# 为当前的文件夹里面的音乐建立index,返回list
def indexMusic(music_dir, bool_NameFirst=True):
    music_library = []
    file_list = os.listdir(music_dir)
    for music_name in file_list:
        if re.match(pattern=re.compile(".*\.mp3"), string=music_name):
            if bool_NameFirst:
                name, singer = music_name.split(" - ")
                singer = singer.split('.')[0]
            else:
                singer, name = music_name.split(" - ")
                name = name.split('.')[0]
            music_library.append({
                'name': name,
                'singer': singer,
                'file': music_name})
    print("乐库曲目总数：" + str(len(music_library)))
    return music_library


# 通过关键字搜索音乐，返回一个list，并通过微信输出给用户搜索结果
def searchMusic(keyword, music_library, limit_num=10 ):
    search_result = []
    for music in music_library:
        if music['file'].find(keyword) >=0 and limit_num > 0:
            search_result.append(music)
            limit_num -= 1
    searchResultPrint(search_result)
    return search_result


# 通过微信输出给用户搜索结果，返回给用户的输出结果
def searchResultPrint(search_result):
    r = ""
    index = 1
    for music in search_result:
        r = r + str(index) + ": " + music['file'] + '\n'
        index += 1
    return r
