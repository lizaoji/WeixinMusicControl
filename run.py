#coding=utf8
import os
import re

import itchat
# 第三方包通过该命令安装：pip install itchat

HELP_MSG = u'''\
欢迎使用『微信音乐遥控器』
帮助: 显示帮助
关闭: 关闭歌曲
歌名: 按照引导播放音乐
随机: 随机开始播放
next: 播放下一首
before: 播放上一首\
'''

music_dir  = "C:\\Users\\29076\\Music"
music_index= {}
search_limit = 10
#wait_choose = False


@itchat.msg_register(itchat.content.TEXT)
def music_player(msg):
    if msg['ToUserName'] != 'filehelper': return
    if msg['Text'] == u'关闭':
        #close_music()
        itchat.send(u'音乐已关闭', 'filehelper')
    if msg['Text'] == u'帮助':
        itchat.send(HELP_MSG, 'filehelper')
    if msg['Text'] == u'随机':
        itchat.send(u'test','filehelper')
    else:
        if msg['Text'].find(' ') >= 0:
            search_name, index = msg['Text'].split(' ')
        else:
            search_name = msg['Text']
            index = -1
        search_result = searchMusic(search_name, search_limit)
        # 只有搜索的结果，直接播放
        if len(search_result) == 1:
            playMusic(1,search_result)
        elif len(search_result) == 0:
            itchat.send('无匹配歌曲','filehelper')
        elif len(search_result) > 1:
            playMusic(index,search_result)

def playMusic(index,search_result):
    if type(index)==str and index.isdigit():
        index = int(index)
    if index >=1 and index <= search_limit:
        index -= 1
        k = music_dir + "\\" + '"' + str(search_result[index]) + " - " + music_index[search_result[index]]['singer'] + ".mp3\""
        os.system(k)
        itchat.send('开始播放：' + str(search_result[index]) + " - " + music_index[search_result[index]]['singer'],'filehelper')
    else:
        itchat.send('输入非法，未播放成功','filehelper')


#为当前的文件夹里面的音乐建立index
def indexMusic(path):
    file_list = os.listdir(music_dir)
    for music_name in file_list:
        if re.match(pattern=re.compile(".*\.mp3"),string=music_name):
            name, singer = music_name.split(" - ")
            singer = singer.split('.')[0]
            music_index[name] = {'singer':singer,'file':music_name}
    print("乐库曲目总数：" + str(len(music_index)))

#通过关键字搜索音乐，返回一个list，并通过微信输出给用户搜索结果
def searchMusic(keyword, limit_num=search_limit):
    search_result = []
    for music_info in music_index.keys():
        if re.match(string=music_index[music_info]['file'],pattern=keyword) and limit_num > 0:
            search_result.append(music_info)
            limit_num -= 1
    searchResultPrint(search_result)
    return search_result

#通过微信输出给用户搜索结果，无返回
def searchResultPrint(search_result):
    r = ""
    index = 1
    for i in search_result:
        r = r + str(index) + ": " + i + "-" + music_index[i]['singer'] + '\n'
        index += 1
    itchat.send(r,'filehelper')

indexMusic(music_dir)
itchat.auto_login(True)
itchat.send(HELP_MSG, 'filehelper')
itchat.run()