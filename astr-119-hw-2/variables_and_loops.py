import numpy as np		#we use numpy for lots of things. it is like a library of different functions that I can borrow in my own code

def main():
	i = 0 					#integers can be declared with number
	n = 10 					#here is a another integer
	x = 119.0 				#floating point nums are declared with a "." floats are decimal numbers

	#we can use numpy to declare arrays quickly

	y = np.zeros(n,dtype=float) #declares 10 zeros as floats (decimals) using np

	#we can use for loops to iterate (like a list) with a variable

	for i in range(n):		#i in range [0,n-1] i could be any variable as long as I define it consistently
		y[i] = 2.0 * float(i) + 1 		#set y = 2i+1 as floats

	#we can also simply iterate through a variable
	for y_element in y:
		print(y_element)

#execute the main function
if __name__== "__main__":
	main()

