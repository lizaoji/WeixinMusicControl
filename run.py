#coding=utf8
import os

import itchat
from NetEaseMusicApi import interact_select_song
# 第三方包通过该命令安装：pip install itchat, NetEaseMusicApi

HELP_MSG = u'''\
欢迎使用微信网易云音乐
帮助： 显示帮助
关闭： 关闭歌曲
歌名： 按照引导播放音乐
查看:  查看歌曲列表\
'''

with open('stop.mp3', 'w') as f: pass
def close_music():
    os.startfile('stop.mp3')

music_path  = "C:\\Users\\29076\\PycharmProjects\\myOwnToy\\PlayMusicViaWechat\\"
@itchat.msg_register(itchat.content.TEXT)
def music_player(msg):
    if msg['ToUserName'] != 'filehelper': return
    if msg['Text'] == u'关闭':
        close_music()
        itchat.send(u'音乐已关闭', 'filehelper')
    if msg['Text'] == u'帮助':
        itchat.send(HELP_MSG, 'filehelper')
    if msg['Text'] == u'查看':
        itchat.send(u'test','filehelper')
    else:
        #itchat.send(interact_select_song(msg['Text']), 'filehelper')
        os.system(music_path + msg['Text']+".mp3")

itchat.auto_login(True)
itchat.send(HELP_MSG, 'filehelper')
itchat.run()