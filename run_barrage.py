import requests
import pygame
import sys

from config import Config
import const


class RunBarrage:

    def __init__(self):
        """
        代码初始化
        """
        self._check_valid()

        pygame.init()
        self.response = requests.post(url=Config.url, headers=Config.headers, data=Config.data)

        self.screen = pygame.display.set_mode(Config.screen_size)
        self.clock = pygame.time.Clock()
        self.clock.tick(Config.frame_rate)

        pygame.display.set_caption('弹幕基')
        # 动画循环计数
        self.frame = 0
        # 选择输出字体
        self.font = pygame.font.SysFont(Config.font, Config.font_size)
        self.screen.fill(Config.background_color)
        # 长度检测
        self.word_length = int(Config.screen_size(0) / Config.font_size)
        self.v = 2 * (Config.font_size * 1.5) / Config.end_frame
        self.standard = ''
        print('初始化完成')

    def run(self):
        while True:
            self._get_barrage()

    def _check_valid(self):
        """
        检测配置参数是否合法
        """
        edge_judge(Config.font_size, const.FONT_SIZE_MAX, const.FONT_SIZE_MIN, 'font_size')
        edge_judge(Config.barrage_remain_num, const.BARRAGE_MAX, const.BARRAGE_MIN, 'barrage_remain_num')
        for value in Config.font_color:
            edge_judge(value, const.RGB_MAX, const.RGB_MIN, 'font_color')
        for value in Config.screen_size:
            edge_judge(value, const.WINDOW_SIZE_MAX, const.WINDOW_SIZE_MIN, 'window_size')
        for value in Config.background_color:
            edge_judge(value, const.RGB_MAX, const.RGB_MIN, 'window_color')

    def _get_barrage(self):
        """
        原来代码while true里的东西，运行一个获取代码输出的过程？
        """
        response_dict = self.response.json()
        text_dict = [item['text'] for item in response_dict['data']['room']]
        if len(text_dict) < 7:
            text_dict = ['0', '1', '2', '3', '4', '5', '6', '7']
        # 弹幕计数
        barrage_count = 0
        # 高度计数
        barrage_height = 1
        if self.standard != text_dict[0]:
            while self.frame <= Config.end_frame:
                barrage_height = -2
                for index in range(1, Config.barrage_remain_num):
                    barrage_count, barrage_height = self._move(barrage_count, barrage_height, self.frame)
                self.frame += 1
                pygame.display.update()
                self.clock.tick(Config.frame_rate)
            self.standard = text_dict[1]
            self.frame = 0
        else:
            barrage_count = 1
            for index in range(1, Config.barrage_remain_num):
                barrage_count, barrage_height = self._judge(barrage_count, barrage_height, text_dict)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)
            pygame.display.update()
            self.clock.tick(1)

    def _put_out(self, m, barrage_height, barrage_count, text_dict):
        """
        第一种输出的方法，我也不知道是什么
        :param m: 不知道是什么
        :param barrage_height: 高度计数
        :param barrage_count: 弹幕计数
        :param text_dict: 获取到的文本？原程序参数"b[]"
        :return: m ++, barrage_height ++ 这个流程控制有问题
        """
        n_1 = self.font.render(text_dict[-barrage_count][m * self.word_length:((m + 1) * self.word_length)],
                               True, Config.font_color)
        h = int(barrage_height * 1.5 * Config.font_size)
        self.screen.blit(n_1, (0, h))
        return m + 1, barrage_height + 1

    def _put_out_2(self, m, barrage_height, barrage_count, text_dict, frame):
        """
        第二种输出的方法，我也不知道是什么
        :param m: 不知道是什么
        :param barrage_height: 高度计数
        :param barrage_count: 弹幕计数
        :param text_dict: 获取到的文本？原程序参数"b[]"
        :param frame: 帧位
        :return: m ++, barrage_height ++ 这个流程控制有问题
        """
        n_1 = self.font.render(text_dict[-barrage_count - 1][m * self.word_length:((m + 1) * self.word_length)],
                               True, Config.font_color)
        h = int(barrage_height * 1.5 * Config.font_size + self.v * frame)
        self.screen.blit(n_1, (0, h))
        return m + 1, barrage_height + 1

    def _move(self, barrage_count, barrage_height, text_dict, frame):
        """
        不知道要移动啥，m和w_n是什么也不知道

        :param barrage_count: 弹幕计数
        :param barrage_height: 高度计数
        :param text_dict: 获取到的文本？原程序参数"b[]"
        :param frame: 帧位
        :return: barrage_weight ++, barrage_height ++ 不要用return做+1了，浪费系统资源
        """
        m = 0
        w_n = len(text_dict[-barrage_count - 1])
        if w_n < self.word_length:
            m, barrage_height = self._put_out_2(m, barrage_height, barrage_count, text_dict, frame)
        elif w_n < 2 * self.word_length:
            m, barrage_height = self._put_out_2(m, barrage_height, barrage_count, text_dict, frame)
            m, barrage_height = self._put_out_2(m, barrage_height, barrage_count, text_dict, frame)
        else:
            m, barrage_height = self._put_out_2(m, barrage_height, barrage_count, text_dict, frame)
            m, barrage_height = self._put_out_2(m, barrage_height, barrage_count, text_dict, frame)
            m, barrage_height = self._put_out_2(m, barrage_height, barrage_count, text_dict, frame)
        return barrage_count + 1, barrage_height + 1

    def _judge(self, barrage_count, barrage_height, text_dict):
        """
        我也不知要判断啥，m和w_n是什么也不知道

        :param barrage_count: 弹幕计数
        :param barrage_height: 高度计数
        :param text_dict: 获取到的文本？原程序参数"b[]"
        :return: barrage_weight ++, barrage_height ++ 不要用return做+1了，浪费系统资源
        """

        m = 0
        w_n = len(text_dict[-barrage_count])
        if w_n < self.word_length:
            m, barrage_height = self._put_out(m, barrage_height, barrage_count, text_dict)
        elif w_n < 2 * self.word_length:
            m, barrage_height = self._put_out(m, barrage_height, barrage_count, text_dict)
            m, barrage_height = self._put_out(m, barrage_height, barrage_count, text_dict)
        else:
            m, barrage_height = self._put_out(m, barrage_height, barrage_count, text_dict)
            m, barrage_height = self._put_out(m, barrage_height, barrage_count, text_dict)
            m, barrage_height = self._put_out(m, barrage_height, barrage_count, text_dict)
        return barrage_count + 1, barrage_height + 1


def edge_judge(value, max_value, min_value, name):
    """
    判断参数数值范围是否合法，如果不合法直接抛出ValueError

    :param value: 要判断的数值
    :param max_value: 数值最大允许值
    :param min_value: 数值最小允许值
    :param name: 参数名字，用于抛出时快速找到不合法参数
    """
    if value > max_value or value < min_value:
        raise ValueError(name + '参数范围不合法')


