from __future__ import division #Autocasts ints into floats when needed to avoid integer division's loss of significance
import Image
import math
import numpy as np
import random


# Mathematical Variables
########################


#Max iterations of newton's method
itermax = 30

#List of all roots
roots = {}

# Tolerance
#tolerance = complex(.001, 0)
tolerance = .001






# Graphics Variables
####################



# List of colors
colors = []

colors.append(("#d7260b"))
colors.append(("#26327e"))
colors.append(("#18f70a"))
colors.append(("#78e48a"))
colors.append(("#7858cf"))
colors.append(("#d10eee"))
colors.append(("#fbe19a"))
colors.append(("#51831f"))
colors.append(("#356ad1"))
colors.append(("#ff8c00"))
colors.append(("#ffff00"))


#Top left corner of graphing window
left = -10
upper = 10

#Bottom right corner of graphing window
right = 10
lower = -10

#Screen width and height (px)
width = 50
height = 50

#delta x and y
xStep = abs((right - left)/width)
yStep = abs((upper - lower)/height)



#####################
# Library Functions #
#####################

# Must return tuple of R G B hex values
def getColor(x, f, tol):
	rand = random.randint(0, 10)
	newRoot = getRoot(x, f, tol)
	if(newRoot == None):
		return "#ffffff"
	print newRoot
	if(len(roots) == 0):
		roots[newRoot] = colors[rand]
		del colors[rand]
		return roots[newRoot]
	for root in roots:
		if(abs(complexDistance(newRoot, root)) < 10*tol):
			#return color already in roots
			return roots[root]
	# No roots have matched generated root based on x, so add it to roots
	roots[newRoot] = colors[rand]
	del colors[rand]
			
# returns distance from complex root x to complex root b
def complexDistance(x, y):
	a = x.real
	b = x.imag
	c = y.real
	d = y.imag
	
	return math.sqrt((a-c)**2 + (b-d)**2)

# Returns an approximation of a root of function f by using
# Newton's Method with initial value x and precision threshold tol
# Returns: double
def getRoot(x,f, tol, iters = 0, xOld = None): # iters = 0 is default to save arguments 
	df = np.polyder(f)
	if(xOld == None):
		xOld = complex(x + tol, 0) # to make the (x-xOld) < tol evaluate to false
	if iters < itermax:
		if(abs(x - xOld) < tol and abs(f(x)) < tol):
			return complex(round(x.real, 4), round(x.imag, 4))
		if(not df(x) == 0):
			xNew = x-(f(x)/df(x))
			return getRoot(xNew, f, tol, iters+1, x)
	else:
		if f(x) < tol:
			return complex(round(x.real, 4), round(x.imag, 4))
	#Implied that if df(x) == 0, return None and 
	#the getColor() function will return a white color



# Rewrites image model based on changed graphing window
# Returns: void
def updateImage():
	# TODO implement
	print("updateImage()")


# Redraws image model on screen
# Returns: void
def redraw():
	# TODO implement
	print("redraw()")



#########################
# End Library Functions #
#########################


f = np.poly1d([3,15,-12,-60]) # 3x^3 + 15x^2 - 12x - 60
#f = np.poly1d([1, 0, 1]) #x^2 + 1


#guess = complex(0, 1) # 0 + 1i




img = []
pic = Image.new( 'RGB', (255,255), "black")

pixels = pic.load()



for i in range(width):
	img.append([])
	for j in range(height):
		img[i].append(getColor(complex(left + xStep*i, lower + yStep*j), f, tolerance))

print img




#print "\n=======\n"

#print complex(left + xStep*width, lower + yStep*height)
#print getRoot(complex(left + xStep*width, lower + yStep*height), f, tolerance)


print "==========="

print(f)
print(np.polyder(f))
print("==========")


#for x in range(len(img)):
#	for y in range(len(img[0])):
#		print img[x][y] == -5.0

