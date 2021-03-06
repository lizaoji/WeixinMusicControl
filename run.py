# coding=utf8
import itchat
from platform import system
from tools import *
from MusicControl import *

# 第三方包通过该命令安装：pip install itchat

HELP_MSG = u'''\
欢迎使用『微信音乐遥控器』
帮助: 显示帮助
关闭: 关闭歌曲
歌名: 按照引导播放音乐
随机: 随机开始播放
下: 播放下一首
上: 播放上一首\
'''


@itchat.msg_register(itchat.content.TEXT)
def music_player(msg):
    if msg['ToUserName'] != 'filehelper':
        return
    if msg['Text'] == u'关闭':
        itchat.send(u'音乐已关闭', 'filehelper')
    if msg['Text'] == u'帮助':
        itchat.send(HELP_MSG, 'filehelper')
    if msg['Text'] == u'随机':
        randMusic(music_library)
        itchat.send(u'随机播放歌曲', 'filehelper')
    if msg['Text'] == '上':
        beforeMusic(current_music,music_library)
    if msg['Text'] == '下':
        nextMusic(current_music,music_library)
    else:
        if msg['Text'].find(' ') >= 0:
            search_name, index = msg['Text'].split(' ')
        else:
            search_name = msg['Text']
            index = -1
        search_result = searchMusic(search_name, music_library, search_limit)
        itchat.send(searchResultPrint(search_result),'filehelper')
        # 只有搜索的结果，直接播放
        if len(search_result) == 1:
            current_music = chooseMusic(1, search_result)
            itchat.send('正在播放：' + current_music, 'filehelper')
        elif len(search_result) == 0:
            itchat.send('无匹配歌曲', 'filehelper')
        elif len(search_result) > 1:
            current_music = chooseMusic(index, search_result)
            if current_music:
                itchat.send('正在播放：' + current_music,'filehelper')
            else:
                itchat.send('未找到对应歌曲','filehelper')

search_limit = 10
current_music = ""
platform, music_dir = getSystemInfo()
music_library = indexMusic(music_dir, bool_NameFirst=True)
itchat.auto_login(True)
itchat.send(HELP_MSG, 'filehelper')
itchat.run()
