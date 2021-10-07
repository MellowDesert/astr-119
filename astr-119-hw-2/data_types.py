import numpy as np 

#integers

i=10
print(type(i)) 	#prints the data type of i

a_i=np.zeros(i,dtype=int) #declare an array of integers
print(type(a_i)) 		#returns ndarray
print(type(a_i[0])) 	#returns int64

#floats

x=119.0 		#float number (decimal)
print(type(x)) 	#print out data type of x

y=1.19e2 		#float 119 in scientific notation
print(type(y)) 	#print out the data type of y

z=np.zeros(i,dtype=float) 	#declare array of floats(decimals)
print(type(z)) 				#returns nd array
print(type(z[0])) 			#returns float64
