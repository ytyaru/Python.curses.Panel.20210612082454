#!/usr/bin/env python3
# coding: utf8
import os, curses

# 複数のnewwin()とsubwin()を使った。
# newwin()は明示的にoverlay()せねばならない。対してsubwin()は自動的にoverlay()してくれる。
# subwin()のoverlay()順序はaddstr()で描画した順である。
class Main:
    def __init__(self, screen, msg, color_index=1):
        self.__screen = screen
        self.__msg = msg
        self.__color_index = color_index
        self.__init_cursor()
        self.__init_color_pair()
        self.__win1 = curses.newwin(curses.LINES, curses.COLS, 0, 0)
        self.__win2 = curses.newwin(curses.LINES, curses.COLS, 0, 0)
        self.__win2_sub1 = self.__win2.subwin(curses.LINES, curses.COLS, 0, 0)
        self.__win2_sub2 = self.__win2.subwin(curses.LINES, curses.COLS, 0, 0)
        self.__draw()
        self.__screen.getch()

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
        self.__win2_sub1.noutrefresh()
        self.__win2_sub2.noutrefresh()

        self.__screen.attron(curses.A_REVERSE | curses.color_pair(1))
        self.__screen.addstr(0, 0, 'screen')

        self.__win1.attron(curses.A_REVERSE | curses.color_pair(2))
        self.__win1.addstr(1, 1, 'win1')
        self.__win1.overlay(self.__screen)

        self.__win2_sub1.attron(curses.A_REVERSE | curses.color_pair(4))
        self.__win2_sub1.addstr(3, 2, 'win2-sub1')

        self.__win2_sub2.attron(curses.A_REVERSE | curses.color_pair(5))
        self.__win2_sub2.addstr(4, 2, 'win2-sub2')

        self.__win2.attron(curses.A_REVERSE | curses.color_pair(3))
        self.__win2.addstr(2, 1, 'win2')
        self.__win2.overlay(self.__screen)

        curses.doupdate()


if __name__ == "__main__":
    curses.wrapper(Main, 'Hello', color_index=2)

