#!/usr/bin/env python3
# coding: utf8
import os, curses

# 複数のnewwin()をscreenへoverlay()した。screen.getch()でscreenが上書きされる。
#   getch()を呼び出したwindowによって画面が再描画されてしまう。なのでgetch()できるのは必ず１つのwindowのみ。描画されるのもgetch()したwindowのみ。けれどコードを分割して複数のwindowを組み合わせたいときがある。そんなときにoverlay()を使う。指定したwindowへ重ね書きする。
class Main:
    def __init__(self, screen, msg, color_index=1):
        self.__screen = screen
        self.__msg = msg
        self.__color_index = color_index
        self.__init_cursor()
        self.__init_color_pair()
        self.__win1 = curses.newwin(curses.LINES, curses.COLS, 0, 0)
        self.__win2 = curses.newwin(curses.LINES, curses.COLS, 0, 0)

        self.__draw()
        self.__screen.getch()
#        self.__input()

    def __init_cursor(self): curses.curs_set(0)
    def __init_color_pair(self):
        if not curses.has_colors(): raise Exception('このターミナルは色を表示できません。')
        if not curses.can_change_color(): raise Exception('このターミナルは色を変更できません。')
        curses.use_default_colors()
        for i in range(1, curses.COLORS):
            curses.init_pair(i, i, curses.COLOR_BLACK)
    def __draw(self):
        self.__screen.noutrefresh()
        self.__win1.noutrefresh()
        self.__win2.noutrefresh()

        self.__screen.clear()
        self.__screen.attron(curses.A_REVERSE | curses.color_pair(1))
        self.__screen.addstr(0, 0, 'screen')

        self.__win1.clear()
        self.__win1.attron(curses.A_REVERSE | curses.color_pair(2))
        self.__win1.addstr(1, 1, 'new1')
        self.__win1.overlay(self.__screen)

        self.__win2.clear()
        self.__win2.attron(curses.A_REVERSE | curses.color_pair(3))
        self.__win2.addstr(2, 1, 'new2')
        self.__win2.overlay(self.__screen)

        curses.doupdate()
    def __input(self):
        while True:
            self.__draw()
            key = self.__screen.getch()
            if ord('q') == key: break


if __name__ == "__main__":
    curses.wrapper(Main, 'Hello', color_index=2)

