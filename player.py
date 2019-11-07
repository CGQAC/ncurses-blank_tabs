#!/usr/bin/env python

from curses import *
from curses.panel import *
from functions import *

class Player:

	def __init__(self, stdscr, p, foreground = None, background = None, attribute = 0):
		self.max_x = stdscr.getmaxyx()[1] - 1
		self.max_y = stdscr.getmaxyx()[0] - 1

		self.x = self.max_x/2
		self.y = self.max_y/2
		self.p = p

		del stdscr #screen only used for maxyx

		self.window = newwin(1, 1, self.y, self.x)
		# waddstr(self.window, p)
		self.window.bkgd( self.p )
		self.panel = new_panel(self.window)
		self.foreground = foreground
		self.background = background

		self.color = 0;

		self.attribute = attribute

		if (foreground != None and background != None):
			self.set_colors(foreground, background)

		self.show_changes()

	def show_changes(self):
		update_panels()
		doupdate()

	def set_colors(self, foreground, background):
		self.color = make_color(foreground, background)
		self.foreground = foreground
		self.background = background
		# waddstr(self.window, self.p, color_pair(self.color) + self.attribute)
		self.window.bkgd(self.p, color_pair(self.color) + self.attribute)
		self.show_changes()

	def move(self, key, motion = 1):
		moved = False
		if (key == KEY_UP):
			if ( self.y - motion >= 0):
				moved = True
				self.y -= motion
		if (key == KEY_DOWN):
			if ( self.y + motion <= self.max_y):
				moved = True
				self.y += motion
			# else:
			# 	self.y = self.max_y
		if (key == KEY_LEFT):
			if ( self.x - motion >= 0):
				moved = True
				self.x -= motion
		if (key == KEY_RIGHT):
			if ( self.x + motion <= self.max_x):
				moved = True
				self.x += motion

		if (moved == True):
			# move_panel(self.panel, self.y, self.x)
			self.panel.move(self.y, self.x)
			self.show_changes()