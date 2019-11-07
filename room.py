from curses import * 
from curses.panel import *
from functions import *

class Room:

	def __init__(self, y, x, h, w, character = ' ', foreground = None, background = None, attribute = 0):

		self.window = newwin(h, w, y, x)
		self.panel = new_panel(self.window)
		self.character = character
		self.attribute = attribute

		self.window.bkgd(self.character, self.attribute)
		self.foreground = foreground
		self.background = background
		self.color = 0

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
		self.window.bkgd(self.character, color_pair(self.color) + self.attribute)
		self.show_changes()