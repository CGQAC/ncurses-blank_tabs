# coding:utf-8
from unicurses import * 
from tab import *
from functions import logdata
import time

class TabManager:

	def __init__(self, stdscr):
		self.stdscr = stdscr
		_, self.navlen = getmaxyx(self.stdscr)
		self.index = -1
		self.tabs = []
		self.title = '.'
		self.time = time.time()

	def add(self, name):
		tab = Tab(self.stdscr, name)
		self.tabs.append(tab)
		tnlist = []
		for tab in self.tabs:
			tnlist.append(tab.name)
		self.index += 1

		length = 1
		i = 0
		move(0,0)
		a = init_pair(1, COLOR_CYAN, COLOR_BLACK)
		b = init_pair(2, COLOR_WHITE, COLOR_BLACK)
		self.title = '.'
		addstr('.')
		for tab in self.tabs:
			b = '┍|' + str(tab.name) + '|┑.'
			if i == self.index:
				addstr('┍|', color_pair(1) + A_BOLD)
				addstr(str(tab.name), color_pair(2) + A_BOLD)
				addstr('|┑.', color_pair(1) + A_BOLD)
			else:
				addstr('┍|', color_pair(1))
				addstr(str(tab.name), color_pair(2))
				addstr('|┑.', color_pair(1))
			self.title += '┍|' + str(tab.name) + '|┑.'
			length += len(tab.name) + 2
			i += 1
		temp = self.title.replace('.', 'a').replace('┍', 'b').replace('┑', 'c')
		logdata('temp:' + str(temp))
		ind = temp.index(name)
		mx = len(temp) - 1
		i = 1
		bar = '┌'
		while i < ind - 2:
			bar += '─'
			i += 1
		bar += '┴' + ('═' * (len(name) + 2 )) + '┴'
		logdata(bar)
		tab.updatebar(bar)
	 	self.top()

	def show_changes(self):
		update_panels()
		doupdate()
		self.checkpanelforupdates()

	def checkpanelforupdates(self):
		if self.tabs[self.index].name == 'Paperclips':
			w = self.tabs[self.index].window
			mvwaddstr(w, 3, 2, str(time.time() - self.time))

	def top(self, dir = None):
		if(dir == 'up'):
			if(self.index + 1 > len(self.tabs) - 1):
				self.index = 0
			else:
				self.index += 1
		elif(dir == 'down'):
			if(self.index - 1 < 0):
				self.index = len(self.tabs) - 1
			else:
				self.index -= 1
		elif(dir == None):
			self.index = len(self.tabs) -1
		else:
			self.index = dir
		logdata('index::::' + str(self.index))
		top_panel(self.tabs[self.index].panel)
		self.show_changes()