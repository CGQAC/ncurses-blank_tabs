#!/usr/bin/env python
# coding:utf-8

from unicurses import *
from tabmanager import *
import time

def main():

	start = time.time()
	stdscr = initscr()

 	start_color()
 	noecho()
 	curs_set(False)
	keypad(stdscr, True)

 	tm = TabManager(stdscr)
 	tm.add('Game')
 	tm.add('Stats')
 	tm.add('Map')
 	tm.add('Paperclips')
 	tm.add('Settings')
	move(0,0)
	while(True):
		key = stdscr.getch()
		if(key == 101):
			tm.top('up')
		if(key == 113):
			tm.top('down')
		if(key == 49) or (key == 50) or (key == 51) or (key == 52) or (key == 53):
			tm.top(key - 49)
		if(key == 27):
			break
	endwin()

	return 0

if __name__ == '__main__':
	main()