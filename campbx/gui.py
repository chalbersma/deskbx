from tkinter import *
import datetime
import os

class GUI:
	def __init__(self, master):
		
		self.upfromme=master
		
		frame = Frame(master)
		frame.grid(column=0, row=0, columnspan=4)
		#frame.pack()
		
		#Menu
		self.menu = Menu(master)
		master.config(menu = self.menu)
		