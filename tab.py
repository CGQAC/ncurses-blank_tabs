# coding:utf-8
from unicurses import * 
import time

class Tab:

	def __init__(self, stdscr, name):
		self.name = name
		self.y, self.x = getmaxyx(stdscr)
		self.y -= 1
		self.window = newwin(self.y, self.x, 1, 0)
		self.panel = new_panel(self.window)
		box(self.window)
		wmove(self.window, 0, 1)
		self.bar = '┘' + (' ' * (len(self.name))) + '└'
		waddstr(self.window, self.bar)
		self.time = time.time()
		wmove(self.window, 1, 2)
		waddstr(self.window, self.name)

		self.show_changes()

	def updatebar(self, bar):
		self.bar = bar
		wmove(self.window, 0, 0)
		waddstr(self.window, self.bar)
		wmove(self.window, 0, 0)
		# a = init_pair(1, COLOR_CYAN, COLOR_BLACK)
		# b = init_pair(2, COLOR_WHITE, COLOR_BLACK)
		# for char in self.bar:
		# 	if char == '─' and char == '┌':
		# 		waddstr(self.window, char)
		# 	else:
		# 		waddstr(self.window, char, color_pair(1) + A_BOLD)

	def show_changes(self):
		update_panels()
		doupdate()