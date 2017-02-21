#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Netease Music UI

Created on 2017-02-21
@author: Mellcap
'''

import os


SONG_CATEGORIES = (
    '流行', '摇滚', '民谣', '说唱', '轻音乐', '乡村', '古典', 'R&B/Soul', '电子', '另类/独立',\
    '学习', '工作', '午休',\
    '华语', '欧美', '日语', '韩语', '粤语', '小语种',\
    '怀旧', '清新', '浪漫', '性感', '治愈', '放松', '兴奋', '快乐', '安静', '思念'
)

FORE_COLOR = {             # 前景色
    'default'      : 39,   #  默认
    'black'        : 30,   #  黑色
    'red'          : 31,   #  红色
    'green'        : 32,   #  绿色
    'yellow'       : 33,   #  黄色
    'blue'         : 34,   #  蓝色
    'purple'       : 35,   #  紫红色
    'cyan'         : 36,   #  青蓝色
    'white'        : 37,   #  白色
    'grey'         : 90,
    'light_red'    : 91,
    'light_green'  : 92,
    'light_yellow' : 93,
    'light_blue'   : 94,
    'light_magenta': 95,
    'light_cyan'   : 96
}

class UI(object):

    def __init__(self):
        self.category_lines = SONG_CATEGORIES
        self.mark_line = 0
        self.play_line = 0
        self.top_index = 0

    def display(self):
        display_lines = []
        terminal_size = os.get_terminal_size()
        self.screen_height, self.screen_width = terminal_size.lines, terminal_size.columns
        top_index = self.top_index
        bottom_index = self.screen_height + top_index - 3

        for index, category in enumerate(self.category_lines[top_index: bottom_index]):
            # mark_line
            is_markline = True if (index + self.top_index) == self.mark_line else False
            category = self.gen_category(category, is_markline)
            # play_line
            play_line = None
            is_playline = True if (index + self.top_index) == self.play_line else False
            if is_playline:
                play_line = self.gen_playline()

            complete_line = '%s %s' % (category, play_line)
            display_lines.append(complete_line)

        print('\n'.join(display_lines))

    def gen_category(self, category, is_markline=False):
        if is_markline:
            category = self.gen_mark(category)
            category = self.gen_color(data=category, color='light_blue')
        else:
            # fill 3 blanks
            category = '   %s' % category
            category = self.gen_color(data=category, color='')
        return category

    def gen_mark(self, category):
        return '⇝  %s' % category

    def gen_playline(self, play_data=None):
        return self.gen_color(data=play_data, color='')

    def gen_color(self, data, color):
        '''
        参考地址:http://blog.csdn.net/gatieme/article/details/45439671
        但是目前用不到这么多类型，目前只用前景色
        '''
        color_code = FORE_COLOR.get(color, 39)
        data = "\033[;%s;m%s\033[0m" % (color_code, data)
        return data



        
