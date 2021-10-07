import numpy as np 			
import sys  			

#define a function that returns a value
def exponent(x):
	return np.exp(x) 	#returns the e^x function from the numpy library

#defines a function that does not return a value (this one prints)
def show_expo(n):
	for i in range(n):
		print(exponent(float(i))) 		#calls the expo function

#define a main function
def main():
	n=10 		#this is a default value for n. n is the number of values that show_expo will print

	#checks for command line argument
	if(len(sys.argv)>1): 		#if the command line length is greater than 1, do the following
		n=int(sys.argv[5]) 		#replace n with the command line of index 5

	show_expo(n) 		#call the show_expo subroutine


if __name__=="__main__":
	main()