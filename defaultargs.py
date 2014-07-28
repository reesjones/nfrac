#Just a quick experiment with default arguments in python.
##########################################################

def default(x = 5, y = 5):
	print(x)
	print(y)


# Should print 5\n5
default()

#Prints 0\n5
default(0)

# Prints 0\n0
default(0, 0)
