# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 17:49:50 2021

@author: natnael
"""
# how to move image to particular postion ; to move the objects from ther orgin
# 
# 


from tkinter import *
import tkinter.font as font
from PIL import ImageTk, Image
import random
import time


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


#this are the rectangles with the 18 cell 
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


#start of big rectangeles

canvas.create_rectangle(20, 105, 199, 284, fill='green')
canvas.create_rectangle(291, 105, 470, 284, fill='red')
canvas.create_rectangle(20, 375, 199,554 , fill='blue')
canvas.create_rectangle(291, 375, 470, 554, fill='yellow')
#end of the rectangeles


#start of the white rectanges
canvas.create_rectangle(50,135,169,254, fill='white')
canvas.create_rectangle(321,135,440,254, fill='white')
canvas.create_rectangle(321,405,440,524, fill='white')
canvas.create_rectangle(50,405,169,524, fill='white')
#end of white rectangles


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


#triangles
canvas.create_polygon(199, 284, 291, 284, 245, 330, fill="green")
canvas.create_polygon(199, 284, 199, 375, 245, 330, fill="red")
canvas.create_polygon(199, 375, 291, 375, 245, 330, fill="blue")
canvas.create_polygon(291, 284, 291, 375, 245, 330,  fill="yellow")
#end of triangles

#circle inside circle 26x26

def move(player,num):
	print(player,num)
	temp_state= [0,0,0,0]
	def make_normal(i):
			img_2 = ImageTk.PhotoImage(Image.open('logo.png'))
			player_obj[player][i].configure(image=img_2)
			player_obj[player][i].image = img_2
			player_obj[player][i]['state'] =NORMAL
	k = 0
	for i in obj_position[player]:
		print(obj_position[player][k])
		if int(num) == 6 and i <= 51:
			make_normal(k)
		elif int(num) == 5 and i <= 52 and i > 0:
			make_normal(k)
		elif int(num) == 4 and i <= 53 and i > 0:
			make_normal(k)
		elif int(num) == 3 and i <= 54 and i > 0:
			make_normal(k)
		elif int(num) == 2 and i <= 55 and i > 0:
			make_normal(k)
		elif int(num) == 1 and i <= 56 and i > 0:
			make_normal(k)
		k +=1		

def update(ind, ins):

	global cunt
	global rand_int
	frame = frames[ind]
	ind += 1
	if ind == frameCnt:
		ind=0
	if cunt > 40:
		# rand_int  = str(random.randint(1,6))
		rand_int= '6'
		img = 'd-' + rand_int +'.png'
		png2 = ImageTk.PhotoImage(Image.open(img))
		btns[ins].configure(image=png2)
		btns[ins].image = png2
		btns[ins]['state'] =NORMAL
		move(ins,rand_int)
		return
	btns[ins].configure(image=frame)
	btns[ins].after(20, update, ind, ins)
	btns[ins]['state'] =DISABLED
	cunt+=1

#moving

def move_obect(plyr, obj):
	rand = int(rand_int)
	print(plyr,'obj', obj)

	if plyr == 0:
		if obj_position[plyr][obj] == 0:
			if  rand == 6:
				canvas.move(player_obj_window[plyr][obj], 10, 10)
		else:
			x = True
			for i in range(rand):
				if obj_position[0][obj] in (0,5,11,13,18,24,26,31,37,39,49,50,51):
					x = False
				if x:
					canvas.move(player_obj_window[plyr][obj], 15, 0)
					root.update()
			else:
				canvas.move(player_obj_window[plyr][obj], 0, 15)
				root.update()
			time.sleep(0.1)
				

	
	
	else:
		pass
	

# x - 60 , y = 60
player_obj = [
['player1_obj_1','player1_obj_2','player1_obj_3','player1_obj_4'],
['player2_obj_1','player2_obj_2','player2_obj_3','player2_obj_4'],
['player3_obj_1','player3_obj_2','player3_obj_3','player3_obj_4'],
['player4_obj_1','player4_obj_2','player4_obj_3','player4_obj_4']
]

player_obj_window = [
['player1_obj_1_window','player1_obj_2_window','player1_obj_3_window','player1_obj_4_window'],
['player2_obj_1_window','player2_obj_2_window','player2_obj_3_window','player2_obj_4_window'],
['player3_obj_1_window','player3_obj_2_window','player3_obj_3_window','player3_obj_4_window'],
['player4_obj_1_window','player4_obj_2_window','player4_obj_3_window','player4_obj_4_window']
]

logo_img = ImageTk.PhotoImage(Image.open('logo.png'))

#objects of first player
player_obj[0][0]= Button(canvas, image=logo_img, command= lambda : move_obect(0,0))
player_obj_window[0][0] = canvas.create_window(67,152, anchor="nw", window=player_obj[0][0])

player_obj[0][1] = Button(canvas, image=logo_img, command= lambda : move_obect(0,1))
player_obj_window[0][1] = canvas.create_window(127,152, anchor="nw", window=player_obj[0][1])


player_obj[0][2] = Button(canvas, image=logo_img, command= lambda : move_obect(0,2))
player_obj_window[0][2] = canvas.create_window(67,212, anchor="nw", window=player_obj[0][2])

player_obj[0][3] = Button(canvas, image=logo_img, command= lambda : move_obect(0,3))
player_obj_window[0][3] = canvas.create_window(127,212, anchor="nw", window=player_obj[0][3])

#objects of second player

player_obj[1][0]= Button(canvas, image=logo_img, command= lambda : move_obect(1,0))
player_obj_window[1][0] = canvas.create_window(338,152, anchor="nw", window=player_obj[1][0])

player_obj[1][1] = Button(canvas, image=logo_img, command= lambda : move_obect(1,1))
player_obj_window[1][1] = canvas.create_window(398,152, anchor="nw", window=player_obj[1][1])


player_obj[1][2] = Button(canvas, image=logo_img, command= lambda : move_obect(1,2))
player_obj_window[1][2] = canvas.create_window(338,212, anchor="nw", window=player_obj[1][2])

player_obj[1][3] = Button(canvas, image=logo_img, command= lambda : move_obect(1,3))
player_obj_window[1][3] = canvas.create_window(398,212, anchor="nw", window=player_obj[1][3])

#objects of thrid player

obj_position = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

for x in range(2):
	for i in range(4):
		player_obj[x][i]['state'] = DISABLED



# dice image and its logic

#initailtion
frameCnt = 40
frames = [PhotoImage(file='gif.gif', format = 'gif -index %i' %(i)) for i in range(frameCnt)]
cunt =0
png = 'gif.gif'
img = ImageTk.PhotoImage(Image.open(png))




def roll():
    global cunt
    cunt = 0
    update(0,0)
    print('roll')

def roll2():
    global cunt
    cunt = 0
    update(1,1)
    print('roll')
def roll3():
    global cunt
    cunt = 0
    update(1,2)
    print('roll')
def roll4():
    global cunt
    cunt = 0
    update(1,3)
    print('roll')



btns = ['btn1', 'btn2', 'btn3', 'btn4']
btns[0] = Button(canvas, image=img, command=roll)
roll_btn_window = canvas.create_window(34,10, anchor="nw", window=btns[0])


btns[1] = Button(canvas, image = img, command=roll2)
roll_btn_window = canvas.create_window(390,10, anchor="nw", window=btns[1])

btns[2] = Button(canvas, image = img, command=roll3)
roll_btn_window = canvas.create_window(34,560, anchor="nw", window=btns[2])


btns[3] = Button(canvas, image = img, command=roll4)
roll_btn_window = canvas.create_window(390,560, anchor="nw", window=btns[3])

#end of dice image and its logics

root.mainloop()
