from Tkinter import *
window = Tk()
canvas = Canvas(window, width=500, height=500, background="black")
canvas.pack()

def get_star_pixel_x(starstring):
	star_coordinates_string = starstring.split(',')
	x = 250 + (250*float(star_coordinates_string[0]))
	return x
def get_star_pixel_y(starstring):
	star_coordinates_string = starstring.split(',')
	y = 250 - (250*float(star_coordinates_string[1]))
	return y
def get_star_size(starstring):
	star_coordinates_string = starstring.split(',')
	size = 10/(float(star_coordinates_string[4])+2)
	return size
def get_star_name(starstring):
	star_coordinates_string = starstring.split(',')
	if len(star_coordinates_string) == 7:
		name = star_coordinates_string[6]
		return name
	else:
		name = ""
		return name	
def draw_star(starstring):
	x = get_star_pixel_x(starstring)
	y = get_star_pixel_y(starstring)
	size = get_star_size(starstring)
	left_x = float(x+(size/2))
	top_y = float(y+(size/2))
	right_x = float(x-(size/2))
	bottom_y = float(y-(size/2))
	star = canvas.create_rectangle(left_x, top_y, right_x, bottom_y, fill="white", width=0)
def draw_all_stars():	
	filename = "stars.txt"
	file = open(filename)
	text = file.read()
	lines = text.split('\n')
	for starstring in lines:
		draw_star(starstring)
def get_star_string(name):
	filename = "stars.txt"
	file = open(filename)
	text = file.read()
	lines = text.split('\n')
	name_found = True
	yname = ""
	for xline in lines:
		xname = get_star_name(xline)
		if xname == name:
			name_found = True
			yname = xline
			break
		else: 
			name_found = False		
	if name_found == True:
		#print yname
		return yname
	else:	
		print "ERROR: No star called " + name + " could be found."
		return ""
def draw_star_by_name(name):
	draw_star(get_star_string(name))
def draw_constellation_line(name1,name2):
	x1 = get_star_pixel_x(get_star_string(name1))
	y1 = get_star_pixel_y(get_star_string(name1))
	x2 = get_star_pixel_x(get_star_string(name2))
	y2 = get_star_pixel_y(get_star_string(name2))
	constellation = canvas.create_line(x1, y1, x2, y2, fill="yellow")
#draw_constellation_line("","")
#draw_star_by_name("")
#draw_star_by_name("")
def draw_constellation_file(filename):
	filename = filename
	file = open(filename)
	text = file.read()
	lines = text.split('\n')
	print lines
	#for zlines in lines:
		#zlines = lines.split(',')
		#draw_constellation_line(zlines[0],zlines[-1])
draw_constellation_file("BigDipper_lines.txt")

mainloop()