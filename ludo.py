# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 20:27:38 2021

@author: natnael
"""

from tkinter import *
import tkinter.font as font
from PIL import ImageTk, Image

root = Tk()
root.title("Ludo King")

width_of_window = 500
height_of_window = 650

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_coordinate = (screen_width/2) - (width_of_window/2) 
y_coordinate = (screen_height/2) - (height_of_window/2)

root.geometry("%dx%d+%d+%d" % (width_of_window, height_of_window, x_coordinate, y_coordinate))


middleFrame = Frame(root)
middleFrame.pack(side='top' )



canvas = Canvas(middleFrame,  borderwidth=1, width="500", height="660", bg='white')
canvas.pack(side='left', fill=X, expand=True)






def draw_board(canvas):
	for r in range(6):
		for c in range(3):
			if c == 1 and r > 0:
				fill = 'blue'
			else:
				fill='white'	
			coords = (199+(c*30), 105+(r*30), 199+(c*30+30), 105+(r*30+30))
			canvas.create_rectangle(coords, fill=fill,)
draw_board(canvas)

def draw_board(canvas):
	for r in range(3):
		for c in range(6):
			if (r == 1 and c > 0) or (r == 0 and c == 1) :
				fill = 'green'
			else:
				fill='white'	
			coords = (20+(c*30), 284+(r*30), 20+(c*30+30), 284+(r*30+32))
			canvas.create_rectangle(coords, fill=fill,)
draw_board(canvas)

def draw_board(canvas):
	for r in range(6):
		for c in range(3):
			if c == 1 and r > 0:
				fill = 'blue'
			else:
				fill='white'	
			coords = (200+(c*30), 374+(r*30), 200+(c*30+30), 374+(r*30+32))
			canvas.create_rectangle(coords, fill=fill,)
draw_board(canvas)

def draw_board(canvas):
	for r in range(3):
		for c in range(6):
			if c == 1 and r > 0:
				fill = 'blue'
			else:
				fill='white'	
			coords = (291+(c*30), 284+(r*30), 291+(c*30+30), 284+(r*30+32))
			canvas.create_rectangle(coords, fill=fill,)
draw_board(canvas)



canvas.create_rectangle(20, 105, 199, 284, fill='green')
canvas.create_rectangle(291, 105, 470, 284, fill='red')
canvas.create_rectangle(20, 375, 199,554 , fill='blue')
canvas.create_rectangle(291, 375, 470, 554, fill='yellow')


canvas.create_rectangle(50,135,169,254, fill='white')
canvas.create_rectangle(321,135,440,254, fill='white')
canvas.create_rectangle(321,405,440,524, fill='white')
canvas.create_rectangle(50,405,169,524, fill='white')

img = canvas.create_oval(60,145,100,185, fill='green')
img = canvas.create_oval(120,145,160,185, fill='green')
img = canvas.create_oval(60,205,100,245, fill='green')
img = canvas.create_oval(120,205,160,245, fill='green')

canvas.create_oval(60,415,100,455, fill='blue')
canvas.create_oval(120,415,160,455, fill='blue')
canvas.create_oval(60,475,100,515, fill='blue')
canvas.create_oval(120,475,160,515, fill='blue')

canvas.create_oval(331,145,371,185, fill='red')
canvas.create_oval(391,145,431,185, fill='red')
canvas.create_oval(331,205,371,245, fill='red')
canvas.create_oval(391,205,431,245, fill='red')

canvas.create_oval(331,415,371,455, fill='yellow')
canvas.create_oval(391,415,431,455, fill='yellow')
canvas.create_oval(331,475,371,515, fill='yellow')
canvas.create_oval(391,475,431,515, fill='yellow')



canvas.create_polygon(199, 284, 291, 284, 245, 330, fill="green")
canvas.create_polygon(199, 284, 199, 375, 245, 330, fill="red")
canvas.create_polygon(199, 375, 291, 375, 245, 330, fill="blue")
canvas.create_polygon(291, 284, 291, 375, 245, 330,  fill="yellow")






root.mainloop()
