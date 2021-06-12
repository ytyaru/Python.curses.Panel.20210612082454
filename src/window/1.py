#!/usr/bin/env python3
# coding: utf8
import os, curses, curses.panel

# stdscrのsubwin()をpanelにする。キーで階層を入れ替える。
class Main:
    def __init__(self, screen, msg, color_index=1):
        self.__screen = screen
        self.__msg = msg
        self.__color_index = color_index
        self.__init_cursor()
        self.__init_color_pair()
        self.__win1 = curses.newwin(10, 100)
        self.__win2 = curses.newwin(10, 100)
        self.__panel1 = curses.panel.new_panel(self.__win1)
        self.__panel2 = curses.panel.new_panel(self.__win2)
        self.__panel1.move(4,4)
        self.__panel2.move(8,8)
        curses.panel.update_panels()
        self.__draw()
        self.__input()
    def __init_cursor(self): curses.curs_set(0)
    def __init_color_pair(self):
        if not curses.has_colors(): raise Exception('このターミナルは色を表示できません。')
        if not curses.can_change_color(): raise Exception('このターミナルは色を変更できません。')
        curses.use_default_colors()
        for i in range(1, curses.COLORS):
            curses.init_pair(i, i, curses.COLOR_BLACK)
    def __draw(self):
        self.__win1.bkgd(' ', curses.A_REVERSE | curses.color_pair(3))
        self.__win2.bkgd(' ', curses.A_REVERSE | curses.color_pair(4))
        try:
            for i in range(1, curses.COLORS):
                self.__win1.addstr(str(i).rjust(3), curses.A_REVERSE | curses.color_pair(i))
        except curses.ERR: pass
        self.__win2.addstr(7, 0, self.__msg, curses.A_REVERSE | curses.color_pair(self.__color_index))
        curses.panel.update_panels()
        self.__screen.refresh()
    def __input(self):
        while True:
            key = self.__screen.getch()
            if curses.KEY_UP == key:
                y, x = self.__win2.getyx()
                y -= 1 if 0 < y else 0
                self.__panel2.move(y, x)
                curses.panel.update_panels()
                self.__screen.refresh()
            elif curses.KEY_DOWN == key:
                y, x = self.__win2.getyx()
                y += 1 if y < curses.LINES-self.__win2.getmaxyx()[0] else 0
#                y += 1
                self.__panel2.move(y, x)
#                self.__panel2.move(20, x)
                curses.panel.update_panels()
                self.__screen.refresh()
            elif curses.KEY_LEFT == key:
                y, x = self.__win2.getyx()
                x -= 1 if 0 < x else 0
                self.__panel2.move(y, x)
                curses.panel.update_panels()
                self.__screen.refresh()
            elif curses.KEY_RIGHT == key:
                y, x = self.__win2.getyx()
                x += 1 if x < curses.COLS-self.__win2.getmaxyx()[1] else 0
                self.__panel2.move(y, x)
                curses.panel.update_panels()
                self.__screen.refresh()
            elif curses.KEY_PPAGE == key or curses.KEY_NPAGE == key:
                if curses.panel.top_panel() == self.__panel1: self.__panel2.top()
                else: self.__panel1.top()
                curses.panel.update_panels()
                self.__screen.refresh()
            else: break
            curses.napms(10)

if __name__ == "__main__":
    curses.wrapper(Main, 'Hello', color_index=2)

