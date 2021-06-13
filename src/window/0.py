#!/usr/bin/env python3
# coding: utf8
import os, curses, curses.panel

# newwinをpanelにして重ね合わせる。
class Main:
    def __init__(self, screen, msg, color_index=1):
        self.__screen = screen
        self.__msg = msg
        self.__color_index = color_index
        self.__init_cursor()
        self.__init_color_pair()
#        self.__win1 = curses.newwin(curses.LINES, curses.COLS)
#        self.__win2 = curses.newwin(curses.LINES, curses.COLS)
        self.__win1 = curses.newwin(10, 100)
        self.__win2 = curses.newwin(10, 100)
        self.__panel1 = curses.panel.new_panel(self.__win1)
        self.__panel2 = curses.panel.new_panel(self.__win2)
        self.__panel1.move(4,4)
        self.__panel2.move(8,8)
#        self.__panel2.top()
#        self.__panel1.top()
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
        self.__screen.getkey()
#        self.__win1.getkey()
#        self.__win2.getkey()
#        curses.napms(2000)
        pass

if __name__ == "__main__":
    curses.wrapper(Main, 'Hello', color_index=2)

