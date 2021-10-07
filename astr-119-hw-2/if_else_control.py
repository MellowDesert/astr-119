#define the function
def flow_control(k):

	#define a string based on the value of k
	if(k==0):
		s="the variable k = %d equals 0." %k

	elif(k==1):
		s="the variable k = %d equals 1." %k

	else:
		s="the variable k = %d does not equal 0 or 1." %k

	#now we print the s
	print(s)

#define a main function
def main():

	#declare integer
	x=0

	#try flow control for 0, 1, 2 (basically, it is testing different integers in flow_control)
	flow_control(x)
	x=1
	flow_control(x)
	x=2
	flow_control(x)

#run code
if __name__=="__main__":
	main()