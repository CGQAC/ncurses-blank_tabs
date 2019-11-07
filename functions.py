# coding:utf-8
from curses import *

global_color_number = 1;

def make_color(foreground, background):

	global global_color_number
	print(global_color_number)
	color_number = global_color_number
	init_pair(color_number, foreground, background)

	global_color_number += 1

	return color_number

def logdata(data):
	f = open('logfile.txt', 'a')
	f.write('::' + str(data) + '::\n')
	f.close()