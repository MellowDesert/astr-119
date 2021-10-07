'''
python lets you deal with 
unexpected results
'''

try:
	print(a) 	#this will throw an exception since a is not defined
except:
	print("a is not defined!")

#there are specific errors to help with cases
try:
	print(a) 	#this will throw an exception since a is not defined
except NameError:
	print("a is still not defined!")
except:
	print("something else went wrong") 		#the green text is a string (str)

#this will break the program
#because a is not defined
print(a)